#!python
#by Ahmet Sacan.
 
def printfile(filename):
	with open(filename) as f: code = f.read()
	print(code)
 
def anotherfunction(a,b):
	return a+b
 
 
 
# This if statement allows running this file from command line
if __name__ == "__main__":
	import sys
	if len(sys.argv) < 2:
		print('--- ERROR: You need to provide the name of the file you want printed.');
		print('usage: python printfile.py filename')
		print('usage: printfile.py filename')
 
		sys.exit(1); #abort
 
	printfile(sys.argv[1])