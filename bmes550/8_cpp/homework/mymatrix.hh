// Author: Tony Okeke (Modified from code by Ahmet Sacan)
// Header file for the mymatrix class.

// Handle warnings
#define _CRT_SECURE_NO_WARNINGS
#define ARMA_DONT_PRINT_CX11_WARNING

// Headers
#include <armadillo>
#include <ctime>
#include <iostream>
#include <stdio.h>
#include <string>

// Namespaces
using namespace arma;
using namespace std;

// mymatrix class
class mymatrix {
    public:
        arma::mat m;

        // Constructor - take nrows, ncols, and a std::vector<double> of values
        mymatrix(int R, int C, std::vector<double> vec);

        // invert() method
        mymatrix invert();
};

// Overload << operator
ostream& operator<<(ostream& cout, const mymatrix m);

