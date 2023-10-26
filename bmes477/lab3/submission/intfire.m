function [V_trace] = intfire(varargin)
    %% Input parsing
    % -- I: Current (µA)
    % -- R: Resistance (MΩ)
    % -- C: Capacitance (nF)
    
    % Defaults
    params = struct('I', 1, ...
                    'R', 40, ...
                    'C', 1, ...
                    'f', 0.01, ...
                    'usesine', false);

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
    I = params.I;
    R = params.R;
    C = params.C;
    if params.usesine
        f = params.f;
    end

    %% Run simulation
    V = 0;
    tstop = 200; %stop time, in ms
    abs_ref = 5; % absolute refractory period, ms
    ref = 0; % absolute refractory period counter
    V_trace = []; % voltage trace for plotting
    V_th = 10; % spike threshold

    % for sinusoidal inputs
    if params.usesine
        I = sin((1:tstop)*f); 
        I(I<0) = 0;
    end

    for t = 1:tstop
       if ~ref
           if params.usesine
               V = V - (V/(R*C)) + (I(t)/C);
           else
               V = V - (V/(R*C)) + (I/C);
           end
       else
         ref = ref - 1;
         V = 0.2*V_th; % reset voltage
       end
       
       if (V > V_th)
         V = 50;  % emit spike
         ref = abs_ref; % set refractory counter
       end
    
       V_trace = [V_trace V];    
    end
end
