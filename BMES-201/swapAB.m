function [a,b] = swapAB(a,b)
   a = a+b;
	 b = a-b;
	 a = a-b;
end