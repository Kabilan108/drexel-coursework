import sys

def aplusb(a,b):
	return a+b;

print('Outside the __name__==main check...');

#if I am running this mypython.py file directly in a terminal or in a system command.
if __name__=="__main__":
	print('First argument is: '+sys.argv[1]);
	print('Second argument is: '+sys.argv[2]);

	print('Summation: '+str(float(sys.argv[1]) + float(sys.argv[2])));

