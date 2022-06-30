function [risk] = cardiodiseaserisk( cholesterol , systolic )
   % Takes the patient's bood cholesterol level and systolic blood
   % pressure, and returns the percent risk of cardiovascular disease.
	 % By Tony Kabilan Okeke (tko35) - 20191101
	 
	 % If the cholesterol is between 150 and 200
	 if (cholesterol >= 150) && (cholesterol < 200)
		 if (systolic >= 80) && (systolic < 120)
			 % if the systolic b.p. is between 80 and 120
			 risk = 2;
		 elseif systolic <= 140
			 % if the systolic b.p isn't between 80 and 120, but is less than or
			 % equal to 140
			 risk = 3;
		 else
			 % if the systolic b.p is outside the range
			 risk = nan;
		 end
	 elseif ((cholesterol >= 200) && (cholesterol <= 250)) && ((systolic>=80) && (systolic <=140))
		 % if the cholesterol isn't between 150 and 200, but is less than or
		 % equal to 250, and the systolic b.p is between 80 and 140 then the 
		 % risk is 5%
		 risk = 5;
	 else
		 % if the cholesterol doesn't fit in the range, then return NaN 
		 risk = nan;
	 end
end