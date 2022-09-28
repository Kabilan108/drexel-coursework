function [points] = valueMapping(values,ranges,pointAssignments)
   % Takes a value, range, and points as input and retuns the points
   % allocated to the value based on where it falls in the range
	 % By Tony Kabilan Okeke - 20191206
	 points( values < ranges(1) ) = pointAssignments(1);
	 points( values > ranges(end) ) = pointAssignments(end);
	 for i = 1:(numel(ranges) - 1)
		 points( values >= ranges(i) & values < ranges(i+1) ) = pointAssignments(i);
	 end
end