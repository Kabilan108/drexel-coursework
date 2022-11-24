//Author: Ahmet Sacan
#define _CRT_SECURE_NO_WARNINGS
#define ARMA_DONT_PRINT_CXX11_WARNING

#include <string>
#include <iostream>
#include <ctime>
#include <stdio.h>
#include <armadillo>

using namespace std;
using namespace arma;


class mymatrix {
public:
	arma::mat m;

	//constructor
	mymatrix(int R, int C, std::vector<double> vec);

	mymatrix invert();
};

//define << operator between cout and person
ostream& operator<<(ostream& cout, const mymatrix m);

