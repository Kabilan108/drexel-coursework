function printrectangle(R,C)
   % Prints a rectangle with R rows anc C columns
	 % By Tony Kabilan Okeke - 20191112
	 for r = 1:R
		 for c = 1:C
			 fprintf('*');
		 end
		 fprintf('\n')
	 end
end