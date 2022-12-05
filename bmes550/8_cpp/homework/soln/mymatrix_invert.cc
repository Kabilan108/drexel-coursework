//Author: Ahmet Sacan
//Sourcecode for a command-line executable that takes R, C, and
// matrix values (in row-order), calculates and prints the inverse of that matrix.
#include <stdio.h>
#include <stdlib.h>
#include "mymatrix.hh"
#define PAUSE {cout << "Print any key to continue..." << endl; getchar();}
using namespace std;

int main(int argc, char* argv[]) {
	// declare variables
	int R, C;
	std::vector<double> vec;

	// Check if R,C are provided.
	if (argc < 3) {
		printf("usage: %s numRows numCols value1 value2 value 3 ... (matrix values must be listed in row-order)\n", argv[0]);
		return 1;
	}

	// Convert R,C command line string's to double's.
	R = atoi(argv[1]);
	C = atoi(argv[2]);

	// Check if R,C are positive integers.
	if (R <= 0 || C <= 0) { //conveniently, atoi returns 0 on error.
		printf("---ERROR: numRows and numCols must be positive integers.\n");
		return 1;
	}

	// Check if there are enough additional command line values for
	//  the values of the RxC matrix.
	if (argc < 3 + R*C) {
		printf("---ERROR: Expecting %d matrix values, but you only provided %d.\n", R*C, argc-3);
		return 1;
	}

	// Convert Command-line matrix values to double's and push them into the vector.
	for (int i = 0; i < R * C; i++) {
		vec.push_back(stod(argv[3 + i]));
	}
	
	// Create mymatrix from R,C, and vector of values. Invert & print.
	mymatrix m(R, C, vec);
	// cout << "Input: " << m << endl;
	// m = m.invert();
	// cout << "After inversion: " << m << endl;


	//PAUSE
	return 0;
}
