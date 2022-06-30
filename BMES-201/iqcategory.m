function [cat] = iqcategory(num)
   % Returns the category in which an IQ score falls
	 % By Tony Kabilan Okeke - 20191023
	 
	 % Check the rab=nge in which the input falls
	 if num >= 130
		 cat = 'Very Superior';
	 elseif num >= 120
		 cat = 'Superior';
	 elseif num >= 109
		 cat = 'High Average';
	 else
		 cat = 'Average';
	 end
end