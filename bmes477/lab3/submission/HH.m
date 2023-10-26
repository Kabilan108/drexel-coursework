%% ========================================================================
% FUNCTION - HH
%%=========================================================================
function dydt = HH(t, y, Cm, I, ENa, EK, El, gbarNa, gbarK, gbarl)

% Values are set to equal the input values
V = y(1);
n = y(2);
m = y(3);
h = y(4);

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

%%
gNa = gbarNa*m^3*h; % transient Na conductance
gK = gbarK*n^4;     % persistent K conductance
gl = gbarl;         % leak conductance

INa = gNa*(V - ENa);% Na current
IK = gK*(V - EK);   % K current
Il = gl*(V - El);   % Leakage current

% Hodgkin-Huxley model equation
dydt = [((1/Cm)*(I-(INa+IK+Il))); an(V)*(1-n)-bn(V)*n;...
    am(V)*(1-m)-bm(V)*m; ah(V)*(1-h)-bh(V)*h];
end