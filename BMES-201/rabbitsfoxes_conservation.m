function out = rabbitsfoxes_conservation(R,F, kr,krf,kfr,kf, T)
%% Create the output Matrix
   % Simulates the population of rabbits and foxes based on specified
   % conditions
	 % By Tony Kabilan Okeke - 20191120
	 out = zeros(T,2); % Preallocate the answer
	 out(1,[1 2]) = [R F];  % Set the first entries to be the initial populations
	 for Y = 2:T % loop frim 2 to T for Years, Y
		 % Calculate the changes
		 dR = round(kr*R-krf*R*F);
		 dF = round(-kf*F+kfr*R*F);
		 
		 % evaluate the new population
		 R = R + dR;
		 F = F + dF;
		 
		 % If either of the populations are less than 2, then set them equal to
		 % 2
		 if R < 2
			 R = 2;
		 end
		 if F < 2
			 F = 2;
		 end
		 
		 % Replace the elements in the output matrix with the current
		 % population
		 out( Y , [1 2] ) = [R F];
	 end
	 
%% Plot the Graph
	 plot( [1:T] , out(:,1), 'r-o')
	 hold on
	 plot( [1:T] , out(:,2), 'b-o' )
	 xlabel('Time (Years)')
	 ylabel('Population Size')
	 legend('Rabbits','Foxes')
	 title( sprintf( 'Simulation of Rabbit and Fox Populations Over %d Years' , T ) ) 
end