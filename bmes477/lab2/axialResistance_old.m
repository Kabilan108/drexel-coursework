
%% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Neural Signals BMES-477/710
% Lab 2: Passive membrane properties
% Section 2: Axial Resistance
% Updated: C.von Reyn,PhD 01/2018
% Instructions: Modify parameter values as indicated in the lab handout,
% and answer questions accordingly!
%% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

clear 

% x_init = 0; % Initial distance
rho = 10;   % resistivity in ohm-mm
a = 1;      % radius of the neural process (in mm)
area = pi*(a)^2;    % Cross-sectional area of process (mm^2)
ra = rho/area;      % axial resistance ohms/mm

Rm=10; %membrane resistance (ohms)
R_M = (4*pi*a^2)*Rm;  % specific membrane resistance (ohms mm^2)
rm = R_M/(2*pi*a); % resistance of a unit lenght of membrane (ohms mm)


lambda = sqrt(rm/ra);


% Define the stimulus
Imag = 1;  %current injected in Amps
C = 1;    % membrane capacitance in Farads
 
% Time of simulation
tstart = 0;
tstop = 100;
dt = 0.1;
time = tstart:dt:tstop;
% Length vector
% NOTE, when modifying X, always include x = 0 as the calculation
% below at different distances is based on the voltage at x = 0!
x = [0 2:2:10];  % default is to record every 2 mm for 10mm 


% Initialize voltage
V = zeros(length(x),1);

inc=1;
for i = 2:length(time)
    if time(i)<10
        I = 0;
    else
        I = Imag; inc = inc+1;
    end
    V(1,i) = Rm*(1 - exp(-time(inc)/(Rm*C)))*I;
    for j = 1:length(x)
        V(j,i) = V(1,i)*exp(-x(j)/lambda);
    end
end
% %  
figure(46)
for j = 1:length(x)
    plot(time,V(j,:))
    hold on
end
axis tight
legend(string(x'))
ylabel('Membrane Voltage (V)');
xlabel('Time (s)')


