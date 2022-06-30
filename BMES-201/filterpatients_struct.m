function out = filterpatients_struct(data)
   % Takes patient data (in form of a structure) as input and returns the
   % names of feamle patients whose ages fall in the closed interval
   % [30,40]
	 % By Tony Kabilan Okeke - 20191120
	 I1 = ([data.gender] == 'f'); % Identify the female entries
	 I2 = ( [data.age] >=30  ) & ( [data.age] <=40 ); % Identify patients between 30 and 40 years old
	 out = { data(I1 & I2).name }; % Get the names of patients that fit the criteria
end