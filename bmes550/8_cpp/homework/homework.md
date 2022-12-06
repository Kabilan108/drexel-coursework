# Assignment: OOP in C++

- In this assignment, you are going to create a command-line executable
  `mymatrix_invert.exe` that calculates and prints the inverse of a given matrix.
  - The executable should take in as command-line arguments the number of rows and the
    number of columns of a matrix; followed by the values of the matrix in row-order.
- Create a mymatrix class (`mymatrix.hh` and `mymatrix.cc`) that has an armadillo
  matrix attribute. 
  - The constructor of mymatrix should accept as input: the number of rows and the
    number of columns of the matrix, and std::vector<double> of the matrix values.
  - The constructor should initialize the matrix attribute and store the given vector
    of values in that armadillo matrix.
  - mymatrix class should have an `invert()` method that inverts the armadillo matrix
    and also returns the modified mymatrix object (i.e., returns `*this`).
- Write a main program file `mymatrix_invert.cc` that takes in command-line arguments
  and creates a mymatrix object from the given R,C, and matrix values; and calls
  mymatrix's `invert()` to invert it. 
- Print the mymatrix before and after inversion. The main program should also perform
  error-checking to ensure there are enough command-line arguments and prints an error
  message when the command-line arguments are missing or invalid.
- Compile the cc files to create the executable `mymatrix_invert.exe` in the same folder.
- Run the execuatable manually, using example 2×2 matrices (in Cygwin/VisualStudio/Terminal).
- Download [`mymatrix_invert_test.mlx`](https://sacan.biomed.drexel.edu/lib/exe/fetch.php?rev=&media=course:bcomp2:cc.dll:hwarmacompileandrunonly:mymatrix_invert_test.mlx) in to your homework folder containing all your
  C++ files and the executable. Run the code `mymatrix_invert_test.mlx` to regenerate
  the output. 
  - Save that notebook as pdf and upload the pdf on Blackboard.
- Solutions to the C++ program described above are available here: [mymatrix.hh](https://sacan.biomed.drexel.edu/lib/exe/fetch.php?rev=&media=course:bcomp2:cc.dll:hwarmacompileandrunonly:mymatrix.hh), [mymatrix.cc](https://sacan.biomed.drexel.edu/lib/exe/fetch.php?rev=&media=course:bcomp2:cc.dll:hwarmacompileandrunonly:mymatrix.cc), [mymatrix_invert.cc](https://sacan.biomed.drexel.edu/lib/exe/fetch.php?rev=&media=course:bcomp2:cc.dll:hwarmacompileandrunonly:mymatrix_invert.cc).
  - You may download and use these files (with no grade penalty), or create your own
    solutions.

## Windows -- Armadillo Visual Studio Instructions

- Install Visual Studio for C + + development, if you haven't already.
- Download Armadillo
- Create a new Visual Studio “Empty Project”.
- Add a new `example_armadillo.cc` file. (Create or add a different file name if you
  are working on a different program).
- Copy and paste armadillo's example program. Try compiling now and again after each
  of the following steps.
- Add armadillo's include directory to your project's Additional Include Directories.
- Add armadillo's examples\lib_win64 folder (which contains precompiled BLAS and
  LAPACK lib files) to your projects Additional Library Directories. Add the *.lib
  files within armadillo's examples/lib_win64 folder as Additional Dependencies.
- Add armadillo's examples\lib_win64 folder (which contains dll files) to Debugging
  Environment PATH (by setting e.g.: PATH=D:\myarma\examples\lib_win64 )
- To see which command lines are being executed to compile your code, change
  C/C++:General:SuppressStartupBanner = No. Repeat for Linker.

## Windows -- Armadillo Cygwin Instructions

- Install Cygwin packages gcc-g + +, make, cmake; if you haven't already.
- Download Armadillo

``` bash
cd Armadillo
```

- Run “the usual” ./configure, make, make install commands. If you get a cmake error
  that it cannot find CMAKE_ROOT, you may need to run the following workaround before
  configuring: `export PATH=”/usr/bin/:$PATH”`
- cd back into your homework directory.
- Use g++ to compile your own cc file(s), link with armadillo.

## MacOS -- Armadillo Homebrew Instructions

- Install Xcode and homebrew if you haven't already.
- Install armadillo using homebrew
- Use g++ to compile your own cc file(s), link with armadillo.

