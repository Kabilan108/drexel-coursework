function v = debug_question2( v )
% A function designed to test for debugging skills.
% Input v is a numeric vector.
% The intended purpose of this function is to remove any prime numbers from
% v. The code has some error(s) that you are expected to identify and
% resolve.
%by AhmetSacan

n = numel( v ); %number of elements in v.

for i=1:n %foreach element in v.
	x = v( i ); %extract the ith number of v and store in x.
	
	if isprime(  x )
		v( i ) = []; %if x is a prime number, remove this ith number from v.
	end
	
end

% at this point, any prime elements of v should have been removed. v should
% now contain the remaining elements and is returned from this function.
