function m=debug_question1(n)
% A function designed to test for debugging skills. Input n is assumed to
% be an integer.
%by AhmetSacan

m = magic(n);
for i=1:numel(m)
	switch mod(m(i),4)
		case 0
			m(i)=log(m(i));
		case 1
			m(i)=sqrt(m(i));
		case 2
			m(i)=sin(m(i));
		case 3
			m(i)=cos(m(i));
	end
end
