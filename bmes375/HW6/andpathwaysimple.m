function dy = andpathwaysimple(t, y, kf, Vmax)
% the species in y:
% S1, R1, R1S1, S2, R2, R2S2, TF, TFP, TFPP




%arbitrary constants. The magitudes are not important.
if ~exist('kf', 'var'); kf = 8; end
if ~exist('Vmax', 'var'); Vmax = 2; end
kr = 4;
km = 2;

re1 = kf*y(1)*y(2) - kr*y(3);
re2 = kf*y(4)*y(5) - kr*y(6);
re3 = Vmax*y(7)*y(3)/(km + y(7)) ;
re4 = Vmax*y(8)*y(6)/(km + y(8)) ;

dy = zeros(9,1);
dy(2) = -re1;
dy(3) = +re1;
dy(5) = -re2;
dy(6) = +re2;
dy(7) = -re3;
dy(8) = +re3-re4;
dy(9) = +re4;
