function dy = andpathway(t, y, varargin)

o=bmes_mergeoptions(struct( ...
	'kf',8 ... %Reaction constants in arbitrary units.
	,'kr',4 ...
	,'vmax',2 ...
	,'km',2 ...
	), varargin{:});

[s1,r1,s1r1,s2,r2,s2r2,tf,tfp,tfpp]=bmes_dealvector(y);

%% Reactions
re1 = o.kf*s1*r1 - o.kr*s1r1;
re2 = o.kf*s2*r2 - o.kr*s2r2;
re3 = o.vmax*s1r1*tf  / (o.km + tf);
re4 = o.vmax*s2r2*tfp / (o.km + tfp);

%% Amount of change in species
ds1 = 0; %s1,s2 stay constant.
dr1 = -re1;
ds1r1 = +re1;

ds2 = 0;
dr2 = -re2;
ds2r2 = +re2;

dtf = -re3;
dtfp = +re3 - re4;
dtfpp = +re4;

dy = [ds1 dr1 ds1r1 ds2 dr2 ds2r2 dtf dtfp dtfpp]';

