%% ========================================================================
% BMES-477/710: Neural Signals
% Lab 3: Models of action potential generation
% Part 2: The Hodgkin-Huxley model
% Description: run the initial simulation, the modify the desired values to
% understand how the system works
%% ========================================================================

function result = runHH(varargin)
    %% Parse inputs
    params = struct('Imag', 0.1, ...
                    'currType', 1, ...
                    'plot', false, ...
                    'TTX', false, ...
                    'TEA', false);

    % Parse Name, Value pairs.
    if nargin > 0
        if rem(nargin,2) ~= 0
            error('Parameters should be in ''Name'', Value pairs');
        end
        for i = 1:2:nargin
            if isfield(params, varargin{i})
                params.(varargin{i}) = varargin{i+1};
            else
                error('Unknown parameter: %s', varargin{i});
            end
        end
    end

    % Unpack params
    Imag = params.Imag;
    currType = params.currType;

    %% DEFINING CONSTANTS:
    Cm = 0.01;      % Membrane Capacitance uF/cm^2 default: 0.01
    dt = 0.04;      % Time step, ms default: 0.04
    t = 0:dt:25;    % Time array, ms default 0:dt:25
    
    ENa = 55.17;    % Na reversal potential, mV default: 55.17
    EK = -72.14;    % K reversal potential, mV default: -72.14
    El = -49.42;    % Leakage reversal potential, mV: -49.42
    
    gbarNa = 1.2;   % maximum Na conductance, mS/cm^2 default: 1.2
    gbarK = 0.36;   % maximum K conductance, mS/cm^2 default: 0.36
    gbarl = 0.003;  % maximum leakage conductance, mS/cm^2 default: 0.003

    % Treatments (TEA or TTX)
    if params.TTX
        gbarNa = 0;
    end
    if params.TEA
        gbarK = 0;
    end
    %% ========================================================================
    % Alpha and beta as anonymous functions
    %%=========================================================================
    % Alpha function for variable m
    am = @(v)...
	    0.1*(v+35)/(1-exp(-(v+35)/10));
    
    % Beta function for variable m
    bm = @(v)... 
	    4.0*exp(-0.0556*(v+60));
    
    % Alpha function for variable n
    an = @(v)...
	    0.01*(v+50)/(1-exp(-(v+50)/10));
    
    % Beta function for variable n
    bn = @(v)... 
	    0.125*exp(-(v+60)/80);
    
    % Alpha function for variable h
    ah = @(v)...
        0.07*exp(-0.05*(v+60));
    
    % Beta function for variable h
    bh = @(v)... 
	    1/(1+exp(-(0.1)*(v+30)));
    %% ========================================================================
    % Solving the HH equations
    %%=========================================================================
    % V(1) = -60;     % Initial membrane voltage (rest), mV
    % m(1) = am(V(1))/(am(V(1))+bm(V(1))); % Initial m-value
    % n(1) = an(V(1))/(an(V(1))+bn(V(1))); % Initial n-value
    % h(1) = ah(V(1))/(ah(V(1))+bh(V(1))); % Initial h-value
    
    % (FOR ODE45 Method)
    V = -60; % Initial membrane voltage (rest), mV
    m = am(V)/(am(V)+bm(V)); % Initial m-value
    n = an(V)/(an(V)+bn(V)); % Initial n-value
    h = ah(V)/(ah(V)+bh(V)); % Initial h-value
    
    %% ========================================================================
    % Define current input, 4 different types:
    % 1) Constant current of magnitude Imag injected throughout the simulation.
    % 2) Constant current of magnitude Imag injected at t=ton
    % 3) Constant current step of mag. Imag injected at t=ton for t=tdur
    % 4) Hyperpolarizing current of -Imag from t=0:ton
    % 5) Hyperpolarizing current of -Imag from t=0:ton followed by step of Imag
    % 6) "Noisy" input current throughout w/mean=Imag, stdev=Imag/3;
    % First, define Imag, ton, tdur:
    % Imag = 0.1; % Depolarizing current magnitude
    ton = find(t==5); % Index of time, t=5ms
    tdur = find(t==1);% Number of time points in 1 ms
    % Now select one of the following current inputs (hint, ctrl-r will comment
    % an entire line, ctrl-t will uncomment
    switch currType
    %%+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    % (1) Constant current input @ t=0:
        case 1
        I = Imag.*ones(1,length(t));
    %%+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    % (2) Constant current input @ t=5ms:
        case 2
            I = [zeros(1,ton) Imag.*ones(1,length(t)-ton)];
    %%+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    % (3) Transient step input @ t=5m for duration tdur:
        case 3
            I = [zeros(1,ton) Imag.*ones(1,tdur) zeros(1,length(t)-ton-tdur)];
    %%+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    % (4) Hyperpolarizing current from t=0:ton:
        case 4
            I = [-Imag.*ones(1,ton) zeros(1,length(t)-ton)];
    %%+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    % (5) Hyperpolarizing current followed by depolarizing current:
        case 5
            I = [-Imag.*ones(1,ton) Imag.*ones(1,length(t)-ton)];
    %%+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    % (6) "Noisy" input current mean=Imag, stdev=Imag/3;
        case 6
            I = Imag + (5*Imag).*randn(1,length(t));
    end
    %%=========================================================================
    % Main loop to numerically solve HH Equations:
    y0 = [V;n;m;h]; % set up array with initial values
    % Initialize output variables:
    OD = []; ODn = []; ODm = []; ODh = []; timeVect = [];
    % Main Loop:
    for ts = 2:length(t)
        if ts==2
            y = y0;       % Initially use first values computed above
        else
            y = V(end,:); % start next run with last values of Vm,n,m,h
        end
        Iin = I(ts);
        % Eval HH with matlab's ode45 function:
        % [time,V] = ode45(@HH,[t(ts-1) t(ts)],y);
        [time,V] = ode45(@(t,y) HH(t, y, Cm, Iin, ENa, EK, El, gbarNa, gbarK, gbarl), [t(ts-1) t(ts)], y);
    
        OD = [OD; V(:,1)];
        ODn = [ODn; V(:,2)];
        ODm = [ODm; V(:,3)];
        ODh = [ODh; V(:,4)];
        timeVect = [timeVect; time];
    end

    % Put all the necessary variables for plotting into a struct.
    result = struct('timeVect', timeVect, ...
                    't', t, ...
                    'currType', currType, ...
                    'OD', OD, ...
                    'ODn', ODn, ...
                    'ODm', ODm, ...
                    'ODh', ODh, ...
                    'I', I, ...
                    'ENa', ENa, ...
                    'EK', EK, ...
                    'El', El, ...
                    'Imag', Imag);

    %% Plot results
    if params.plot
        % Plot input current
        subplot(231);cla
        plot(t,I,'k');
        xlabel('Time (ms)');
        ylabel('Current (\muA)')
        title('Input Current');
        axis tight
        if mean(I)~=0
            set(gca,'ylim',[min(I)-Imag max(I)+Imag])
        end
        
        % Plot membrane potential
        subplot(232);cla
        plot(timeVect,OD,'k','linewidth',2);
        hold on
        plot([t(1) t(end)],[ENa ENa],'b--');
        plot([t(1) t(end)],[EK EK],'r--');
        plot([t(1) t(end)],[El El],'k--')
        xlabel('Time (ms)')
        ylabel('Voltage (mV)')
        title('Membrane Voltage: HH Model');
        axis tight
        set(gca,'ylim',[EK-5 ENa+5])
        
        % Model params
        subplot(233);cla
        text(0,1,['Current type: ',num2str(currType)]);
        text(0.7,1,['I_{mag} = ',num2str(Imag),' \muA'])
        text(0,0.8,['C_m = ',num2str(Cm),' \muF/{cm}^2']);
        text(0,0.6,'$\bar{g}_{Na} = $','interpreter','latex','fontsize',12);
        text(0.3,0.6,[num2str(gbarNa),' mS/{cm}^2'])
        text(0,0.4,'$\bar{g}_{K} = $','interpreter','latex','fontsize',12);
        text(0.3,0.4,[num2str(gbarK),' mS/{cm}^2'])
        text(0,0.2,'$\bar{g}_{L} = $','interpreter','latex','fontsize',12);
        text(0.3,0.2,[num2str(gbarl),' mS/{cm}^2'])
        axis off
        
        % Plot gating variables
        subplot(234);cla
        plot(timeVect,ODn,'r','linewidth',2);
        ylabel('Probability')
        xlabel('Time (ms)')
        title('Gating Variable n')
        axis tight
        set(gca,'ylim',[0 1])
        
        subplot(235);cla
        plot(timeVect,ODm,'b','linewidth',2)
        % ylabel('Probability')
        xlabel('Time (ms)')
        title('Gating Variable m')
        axis tight
        set(gca,'ylim',[0 1])
        
        subplot(236);cla
        plot(timeVect,ODh,'g','linewidth',2)
        % ylabel('Probability')
        xlabel('Time (ms)')
        title('Gating Variable h')
        axis tight
        set(gca,'ylim',[0 1])
    end
end