"""
Author: Tony Kabilan Okeke <tko35@drexel.edu>
template by: AhmetSacan.
"""

# Imports
import os


def loadcatsite() -> tuple:
    """
    Function to load catsite data into a numerical matrix, `X`. Each row of `X`
    should represent a sample. Each column of `X` should represent an attribute.
    Each row of `T` should represent the target value of a sample. The names output
    variable should contain the list of names of the attributes in `X`.

    Returns
    -------
    X : numpy.ndarray
        A 2D numpy array containing the numerical data of the catsite dataset.
    T : numpy.ndarray
        A 1D numpy array containing the target values of the catsite dataset.
    names : list
        A list containing the names of the attributes in the catsite dataset.
    """

    # Lad the NataliaPetrova.catsite.arff file into variable catsite
    # Read in the NataliaPetrova.catsite.arff file using the provided bmes.arffload() function
    # (which was slightly modified from "dataformat project":
    # https://ml01.zrz.tu-berlin.de/trac/dataformat/browser/trunk/matlab/arffload.m )
    file=bmes.downloadurl('http://sacan.biomed.drexel.edu/lib/exe/fetch.php?rev=&media=course:ml:nn:hwnn.catsite:NataliaPetrova.catsite.arff');
    catsite=bmes.arffload(file);


    # Convert the AAName1LetterCode feature to numeric data.
    # Each amino acid should be represented by 20 binary numbers. You must use
    # the conventional ordering of the amino acids. See int2aa() for the
    # conventional aminoacid <-> integer conversion.
    # Use "one-hot" encoding: https://en.wikipedia.org/wiki/One-hot
    # where each amino acid is represented by 20 binary numbers. e.g, the amino
    # acid N, which has a conventional integer value of 3 (see aa2int('N')) needs
    # to be encoded as: 0010000000000000000.
    # Assume that only standard amino acids (one of: 'ARNDCQEGHILKMFPSTWYV')
    # will appear in the dataset. With this assumption, non-standard amino
    # acids, if any, would end up being represented with all-zeros in your
    # one-hot encoding.  


    # Remove data with missing values.
    # Remove all data rows where a numeric value is NaN (not a number), which
    # are indicated by '?' in the arff file. See matlab function ``isnan()''.


    # Convert the class labels to numeric +1/-1.
    # Store the class labels into a numerical vector T. Remove that column from X.


    # Convert the data into a numeric matrix X, if you haven't already.
    # X: one row per data sample, and one column for each feature.

