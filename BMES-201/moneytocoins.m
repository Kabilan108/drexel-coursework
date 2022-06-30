function [dollars,quarters,dimes,nickels,pennies] = moneytocoins(input)
   % Returns the number of different coin types in a certain amount
	 % By Tony Kabilan Okeke - 20190410
	 
	 % Convet the user input to cents
	   cents = round(input * 100);
	 % Obtain Number of dollars by dividing by 100
	     dollars = fix(cents/100);
	 % centsRem is the number of cents remaining after the number of dollars
	 % has  been removed
		 centsRem = mod(cents,100);
	 % Obtain the number of quarters by dividing by 25, and the cents
	 % remaining
	     quarters = fix(centsRem/25);
	   centsRem = mod(centsRem,25);
	 % Obtain the number of dimes by dividing by 10, and the cents remaining
	     dimes = fix(centsRem/10);
     centsRem = mod(centsRem,10);
	 % Obtain the number of nickels by dividing by 5, the remainder is the
	 % number of pennies
	     nickels = fix(centsRem/5);
       pennies = mod(centsRem,5);
end