function [avgodds,avgevens] = averageoddsandevens(data)
   % Returns the average of odd numbers and even numbers respectively
	 % By Tony Kabilan Okeke - 20191016
	 
	 % Obtain the even entries i.e. the entries which when divided by 2 will
	 % have no remainder. Then obtain the average
	 evens = data(mod(data,2) == 0);
	 avgevens = mean(evens);
	 
	 % Obtain the odd entries i.e. the entries which when divided by 2 will
	 % have a remainder
	 odds = data(mod(data,2) ~= 0);
	 avgodds = mean(odds);
end