function [bmi] = calculatebmis(heights,weights)
   % Takes two input vectors, heights and weights, and returns a vector
   % containing the calculated BMIs
	 % By Tony Kabilan Okeke - 20191016
	 
	 bmi = (weights .* 4.88) ./ (heights .^ 2);
end