function [sum] = addmany(varargin)
   % Takes variable number of inputs and returns their sum
	 % By Tony Kabilan Okeke - 20191120
	 % initialize the sum
	 sum = 0;
	 for i = 1:nargin
		 sum = sum + varargin{i};
	 end
end