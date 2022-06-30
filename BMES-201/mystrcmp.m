function logicOut = mystrcmp(arg1,arg2)
   % Performs the same function as the strcmp function
	 % By Tony Kabilan Okeke - 20191120
	 [r,c] = size(arg1);
	 logicOut = zeros(r,c);
	 for i = 1:numel(arg1)
		 if arg1{i} == arg2
			 logicOut(i) = 1; 
			 break; 
		 else
			 logicOut(i) = 0;
		 end
	 end
	 logicOut = logical( logicOut );
end