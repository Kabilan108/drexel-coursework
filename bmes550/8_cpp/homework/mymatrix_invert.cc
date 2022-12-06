// Author: Tony Okeke (Modified from code by Ahmet Sacan)
// A command line executable that takes R, C and matrix vaues (in row-order),
// calculates and prints the inverse of the matrix.

// Headers
#include <stdio.h>
#include <stdlib.h>
#include "mymatrix.hh"

// Pause function
#define PAUSE {cout << "Print any key to continue..." << endl; getchar();}

// Namespaces
using namespace std;


int main(int argc, char* argv[]) {
    // argc (argument count) and argv (argumen vector) are used to accept command line
    // arguments for main().

    // Declare variables
    int R, C;
    std::vector<double> values;

    // Check if R and C were provided
    if (argc < 3) {
        cout << "Usage: " << argv[0] << " nrows ncols val1 val2 val3 ...  "
             << "(values must be listed in row-order)." << endl;
        return 1;
    }

    // Convert R, C from string to double (atoi returns 0 on error)
    R = atoi(argv[1]);
    C = atoi(argv[2]);

    // Check that R, C are positive integers
    if (R <= 0 || C <= 0) {
        cout << "ERROR: nrows and ncols must be positive integers." << endl;
        return 1;
    }

    // Check if there are enough values provided for an R x C matrix
    if (argc < 3 + R*C) {
        cout << "ERROR: Expecting " << R*C << " matrix values, but you only provided "
             << argc-3 << "." << endl;
        return 1;
    }

    // Convert command line matrix values to doubles and store them in a vector
    for (int i = 0; i < R * C; i++) {
        values.push_back(stod(argv[3 + i]));
    }

    // Create a mymatrix object
    mymatrix A(R, C, values);

    // Invert the matrix and print the results
    cout << "Input: " << A << endl;
    A = A.invert();
    cout << "After inversion: " << A << endl;

    // Pause
    return 0;
}

