function bacteriaKilled = killbacteria_1d_noedgecase(V,i)
   % Returns the number of bacteria killed, assuming the antibiotic is
   % never placed on an edge dish
	 % By Tony Kabilan Okeke - 20191110
	 
	 % Bacteria in the i'th block are all dead
	 allDead = V(i);
	 
	 % Calculate the number of bacteria killed in the left and right petri
	 % dishes
	 halfDeadLeft = (V(i-1)/2);
	 halfDeadRight = (V(i+1)/2);
	 
	 bacteriaKilled = allDead + halfDeadLeft +halfDeadRight;
end