function [avg] = avgpositive7multiples_for(vec)
   % Takes a vector as input and returns the average of the positive
   % multiples of 7 in the vector
	 % By Tony Kabilan Okeke - 20191112
	 
	 % initialize the average and count at zero
	 avg = 0;
	 count = 0;
	 for i = 1:numel(vec)
		 if (vec(i) > 0) && (mod(vec(i),7) == 0)
			 avg = avg + vec(i);
			 count = count + 1;
		 end
	 end
	 % calculate the average
	 avg = avg / count;
end