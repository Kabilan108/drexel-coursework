// Author: Tony Okeke (Modified from code by Ahmet Sacan)
// Definition and methods for mymatrix class

// Handle warnings
#define _CRT_SECURE_NO_WARNINGS

// Inlcude the mymatrix header
#include "mymatrix.hh"

// Initialize the mymatrix object
mymatrix::mymatrix(int R, int C, std::vector<double> values) {
    // Create empty arma matrix
    this -> m = arma::mat(R, C);
    int idx = 0;

    // Populate the matrix
    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++, idx++) {
            this -> m(i,j) = values[idx];
        }
    }
};

// Define the invert method
mymatrix mymatrix::invert() {
    // Use arma to invert the matrix and modify the `m` attribute
    this -> m = arma::inv(this -> m);

    // Return the modified object
    return *this;
};

// Define the << operator between cout and person
ostream& operator << (ostream& cout, const mymatrix mat) {
    cout << mat.m.n_rows << " x " << mat.m.n_cols << " matrix" << endl
         << "Values: " << endl
         << mat.m << endl;
    return cout;
};

