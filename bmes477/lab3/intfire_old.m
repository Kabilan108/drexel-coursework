% Basic integrate-and-fire neuron 
% R Rao 1999  (adapted for 590rr)
% Updated 01/2018 CvR

clear
% for sinusoidal input current
%f = 0.5; %frequency, in radians/ms

% capacitance and leak resistance
C = 1; % nF
R = 40; % M ohms

% I & F implementation dV/dt = - V/RC + I/C
% Using h = 1 ms step size, Euler method

V = 0;
tstop = 200; %stop time, in ms
abs_ref = 5; % absolute refractory period, ms
ref = 0; % absolute refractory period counter
V_trace = []; % voltage trace for plotting
V_th = 10; % spike threshold

f = 0.01;

% input current
% I=1; %in microAmps
I = sin((1:tstop)*f); 
I(I<0)=0;

for t = 1:tstop
  
   if ~ref
       % V = V - (V/(R*C)) + (I/C);
     V = V - (V/(R*C)) + (I(t)/C);
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

figure
plot(V_trace)
xlabel('Time(ms)')
ylabel('Voltage (mV)')
