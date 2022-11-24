//Author: Ahmet Sacan
#define _CRT_SECURE_NO_WARNINGS
#include "mymatrix.hh"

//create a mymatrix object from RxC dimensions and the matrix values given in a vector (using row-order)
mymatrix::mymatrix(int R, int C, std::vector<double> vec){
	this->m = arma::mat(R, C);
	int vi = 0;
	for (int i = 0; i < R; i++) {
		for (int j = 0; j < C; j++, vi++) {
			this->m(i,j) = vec[vi];
		}
	}
}

mymatrix mymatrix::invert() {
	this->m = arma::inv(this->m);
	return *this;
}

//define << operator between cout and person
ostream& operator<<(ostream& cout, const mymatrix m) {
	cout << "Matrix numRows: " << m.m.n_rows << ", numCols: " << m.m.n_cols << ", Values: " << endl
		<< m.m << endl;
	return cout;
}

