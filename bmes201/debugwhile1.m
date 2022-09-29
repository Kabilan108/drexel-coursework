function n=debugwhile1( n )
% A function designed to test for debugging skills.
% Input n is assumed to be an integer.
%by AhmetSacan
i=0;
while log10(n)*sqrt(n)>10
	n=n/exp(1);
	i=i+1;
end
