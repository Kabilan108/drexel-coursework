%% ========================================================================
% BMES-477/710: Neural Signals
% Homework 3: Models of action potential generation
% Part 3: Model of Thalamic Relay Neuron: the T-type Calcium 
% current to generate post-inhibitory rebound
% Description: run the initial simulation, the modify the desired values to
% understand how the system works
% Edited by CvR 09/2021
%% ========================================================================
clear,clc
% DEFINING CONSTANTS:
Cm = 10e-9; % specific membrane capacitance, F/mm^2 default: 10e-9
dt = 0.000005;  % time step default: 0.000005
tmax = 2;     % time to run, in s  default: 2
t = 0:dt:tmax;  % time vector

ENa = 0.055;    % Na reversal potential default: 0.055
EK = -0.09;     % K reversal potential default: -0.09
EL = -0.07;     % Leak reversal potential default: -0.07
ECa = 0.120;    % Ca reversal potential default: 0.120

gbarNa = 0.36e-3;  % Specific Na conductance, S/mm^2 default: 0.36e-3
gbarK = 0.16e-3;% Specific K conductance, S/mm^2 default: 0.16e-3
gbarL = 1e-6;   % Specific leak conductance default: 1e-6
gbarCaT = 18e-6;% Specific T-type Ca conductance default: 18e-6

% Defining current inputs:
istart = 0.5;   % Inject current time, s default: 0.5
ilength = 0.5;  % Duration of injected current, s default: 0.5
I0 = 0;      % Initial current, default: 0
Imag = 10e-9;   % magnitude of applied current pulse default: 10e-9
Iend = I0;

% Initialize variables:
V = zeros(size(t));     % voltage vector
IL = zeros(size(t));    % leak current vector
INa = zeros(size(t));   % Na current vector
IK = zeros(size(t));    % K current vector
ICaT = zeros(size(t));  % T-type Ca current vector

V(1) = EL;  % Set initial value of membrane voltage

n = zeros(size(t));     % n: K activation gating variable
n(1) = 0;               % initially @ 0
m = zeros(size(t));     % m: Na activation gating variable
m(1) = 0;               % initially = 0
h = zeros(size(t));     % h: Na inactivation gating variable
h(1) = 0;               % initially = 0;

M = zeros(size(t));     % CaT current activation gating variable
M(1) = 0;               % initially = 0;
H = zeros(size(t));    % CaT current inactivation gating variable
H(1) = 0;              % initially = 0;

% Define input current:
Iin = zeros(size(t));  % applied current.
for i = 1:length(t)
    if t(i)>=istart && t(i)<=istart+ilength
        Iin(i) = Imag;
    elseif t(i)<istart
        Iin(i) = I0;
    else
        Iin(i) = Iend;
    end
end

Itot = zeros(size(t));  % total current vector
caCond = [];
%% Main Loop: Calculate Vm and gating variables using forward-Euler method
for i = 2:length(t)
    IL(i-1) = gbarL*(EL-V(i-1));   % Leak current
    Vm = V(i-1)*1000;   % Convert V to mV
    
    % Calculating transition rates for Na and K conductances
    if (Vm == -35)
        alpha_m = 1;
    else
        alpha_m = 0.1*(Vm+35)/(1-exp(-0.1*(Vm+35)));
    end
    beta_m = 4*exp(-(Vm+60)/18);
    
    if (Vm == -34)
        alpha_n = 0.05/0.1;
    else
        alpha_n = 0.05*(Vm+34)/(1-exp(-0.1*(Vm+34)));
    end
    beta_n = 0.625*exp(-0.0125*(Vm+44));
    
    alpha_h = 0.35*exp(-0.05*(Vm+58));
    beta_h = 5/(1+exp(-0.1*(Vm+28)));
    
    % Finding steady state values and time constants for m,n,h
    m_inf = alpha_m/(alpha_m+beta_m);
    tau_m = 1e-3/(alpha_m+beta_m);
    
    n_inf = alpha_n/(alpha_n+beta_n);
    tau_n = 1e-3/(alpha_n+beta_n);
    
    h_inf = alpha_h/(alpha_h+beta_h);
    tau_h = 1e-3/(alpha_h+beta_h);
    
    % Update m,n,h
    m(i) = m_inf;
    h(i) = h_inf - (h_inf-h(i-1))*exp(-dt/tau_h);
    n(i) = n_inf - (n_inf-n(i-1))*exp(-dt/tau_n);
    
    % The CaT current gating variables s and hs, are expressed in terms of
    % steady state values and time constants:
    M_inf = 1/(1+exp(-(Vm+52)/7.4));
    H_inf = 1/(1+exp((Vm+76)/2));
    if (Vm<-80)
        tau_H = 1e-3*exp((Vm+467)/66.6);
    else
        tau_H = 24e-3+1e-3*119/(1+exp((Vm+70)/3));
    end
    
    % Update s, hs
    M(i) = M_inf;
    H(i) = H_inf - (H_inf-H(i-1))*exp(-dt/tau_H);
    
    % Calculate conductances for Na, K, L, Ca:
    gNaCur = gbarNa*(m(i)^3)*h(i);
    INa(i-1) = gNaCur*(ENa - V(i-1)); % Total Na current
    
    gKCur = gbarK*(n(i))^4;
    IK(i-1) = gKCur*(EK - V(i-1));    % Total K current
    
    gCaTCur = gbarCaT*(M(i)^2)*H(i);
    ICaT(i-1) = gCaTCur*(ECa - V(i-1));% Total T-type Ca current
    caCond(i) = gCaTCur;
    % Total current
    Itot(i-1) = IL(i-1)+INa(i-1)+IK(i-1)+ICaT(i-1)+Iin(i-1);
    
    gTot = gbarL+gNaCur+gKCur+gCaTCur;
    V_inf = (gbarL*EL + gNaCur*ENa + gKCur*EK + gCaTCur*ECa + ...
        Iin(i-1))/gTot;
    
    % Update the membrane potential:
    V(i) = V_inf - (V_inf-V(i-1))*exp(-dt*gTot/Cm);
    
end

%% ============= PLOTTING =================================================
figure('position',[100 100 1200 800]);
subplot(2,4,1);
plot(t,Iin);
xlabel('Time (s)')
ylabel('Input Current (A)')
title('Input Current')
axis tight
% set(gca,'ylim',[I0-I0/4 Imag+Imag/4]);

subplot(2,4,2);
plot(t,V);
xlabel('Time (s)')
ylabel('V_m (V)');
title('Membrane potential')
hold on;
plot([0 tmax],[ENa ENa],'k--');
plot([0 tmax],[EK EK],'g--');
axis tight
% set(gca,'ylim',[EK+EK/4 ENa+ENa/4]);

subplot(2,4,3);
plot(t,n);
xlabel('Time (s)')
ylabel('Probability');
title('Gating Variable n')
axis tight
set(gca,'ylim',[0 1])

% subplot(2,4,4);
% plot(t,n);
% xlabel('Time (s)')
% ylabel('Probability');
% title('Gating Variable n')
% axis tight
% set(gca,'ylim',[0 1])

subplot(2,4,5);
plot(t,m);
xlabel('Time (s)')
ylabel('Probability');
title('Gating Variable m')
axis tight
set(gca,'ylim',[0 1])

subplot(2,4,6);
plot(t,h);
xlabel('Time (s)')
ylabel('Probability');
title('Gating Variable h')
axis tight
set(gca,'ylim',[0 1])

subplot(2,4,7);
plot(t,M);
xlabel('Time (s)')
ylabel('Probability');
title('Gating Variable M')
axis tight
set(gca,'ylim',[0 1])

subplot(2,4,8);
plot(t,H);
xlabel('Time (s)')
ylabel('Probability');
title('Gating Variable H')
axis tight
% set(gca,'ylim',[0 1])
    










