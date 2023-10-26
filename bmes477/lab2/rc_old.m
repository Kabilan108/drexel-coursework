%% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Neural Signals BMES-477/710
% Lab 2: Passive membrane properties
% Section 1: Parallel RC Circuit
% Author: E.Knudsen,PhD
% Updated: C.von Reyn,PhD 09/2021
% Instructions: Modify parameter values as indicated in the lab handout,
% and answer questions accoringly!
%% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% time of simulation
tstart = 0;
tstop = 1000;
dt = 0.01;
time = tstart:dt:tstop; %in seconds
% Define the stimulus:
Imag = 1E-9; % stimulus amplitude in A
Istep = [zeros(1,find(time==10)) Imag.*ones(1,length(time)-find(time==10))];

% Define R and C
R = 10E6;      % in Ohms
C = 1E-6;      % in Farads

% Initialize voltage
V_init = 0;
V = [V_init zeros(1,length(time)-1)];
%% 
inc=1;
for i = 2:length(time)
    if time(i)<10
        I = 0;
    else
        I = Imag;inc=inc+1;
    end
    V(i) = R*(1 - exp(-time(inc)/(R*C)))*I;
%     V2(i) = V(i)/2;
%     V3(i) = V(i)/5;
end

%convert from A to nA
Istep=Istep./1E-9;

figure('position',[200 100 600 600]);
ax1=subplot(211);plot(time,Istep);
ylabel('Input Current (nA)')

%convert from V to mV
V=V.*1000;

ax2=subplot(212);
plot(time,V,'r')
% hold on
% plot(time,V2,'g')
% plot(time,V3,'b')
ylabel('Voltage (mV)')
xlabel('Time (sec)')
title(['Steady state voltage = ',num2str(V(end)),'mV'])
%text(60,9,['Steady state voltage = ',num2str(V(end)),'V'])
%disp(['Steady state voltage = ',num2str(V(end)),'V'])
linkaxes([ax1,ax2],'x')
xlim ([0 100])

%%
%Estimate the time to reach steady state here

%%
% Estimate the time constant here
