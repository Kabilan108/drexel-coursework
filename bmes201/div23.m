function div23(input)
  % Returns whether input is divisible by 2
	% T.K.O - 20191023

	% Is input divisible by 2?
	if mod(input,2)==0
		% Yes
		fprintf('divisible by 2: yes\n')
	else
		% No
		fprintf('divisible by 2: no\n')
	end
	
	% Is input divisible by 3?
	if mod(input,3)==0
		% Yes
		fprintf('divisible by 3: yes\n')
	else
		% No 
		fprintf('divisible by 3: no\n')
	end
end