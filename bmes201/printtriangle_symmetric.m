function printtriangle_symmetric(R)
   
   for i = 1:R
		 for j = 1:R-i
			 fprintf(' ');
		 end
		 for k = 1:(2*i-1)
			 fprintf('*');
		 end
		 fprintf('\n');
	 end

end