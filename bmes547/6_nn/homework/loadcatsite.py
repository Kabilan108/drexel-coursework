"""
Author: Tony Kabilan Okeke <tko35@drexel.edu>
template by: AhmetSacan.
"""

# Imports for data loading and manipulation
from sklearn.preprocessing import StandardScaler
import scipy.io as sio
import pandas as pd
import numpy as np

# Import the bmes module
import sys, os; sys.path.append(os.environ['BMESAHMETDIR'])
import bmes


# Amino acid conventional ordering
aminos = 'ARNDCQEGHILKMFPSTWYV'


def OneHotEncoder(aaseq):
    """
    Function to convert a single amino acid into a one-hot encoding.
    """

    # Initialize a 20-element vector of zeros.
    onehot = np.zeros((len(aaseq), 20))

    # Set the appropriate elements to 1
    for i in range(len(aaseq)):
        if aaseq[i] in aminos:
            onehot[i, aminos.index(aaseq[i])] = 1
        else:
            onehot[i, :] = 0

    return onehot


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

    # Load the NataliaPetrova.catsite.arff file into variable catsite
    URL = ('http://sacan.biomed.drexel.edu/lib/exe/fetch.php?rev=&media=course:'
           'ml:nn:hwnn.catsite:NataliaPetrova.catsite.arff')
    file = bmes.downloadurl(URL, 'catsite.arff');
    data, _ = sio.arff.loadarff(file)
    df = pd.DataFrame(data)

    # Decode any bytes to strings
    df = df.applymap(lambda x: x.decode('utf-8') if isinstance(x, bytes) else x)

    # Extract numeric features
    X = df.select_dtypes(include=['float64', 'int64']).values

    # Standardize the numeric features
    X = StandardScaler().fit_transform(X)
    
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
    A = OneHotEncoder(df['AAName1LetterCode'].values)

    # Add the one-hot encoding of the amino acid sequence to the feature matrix X.
    X = np.hstack((A, X))

    # Create names for the features.
    names = ['AminoAcid' + aminos[i] for i in range(20)]
    names.extend(df.select_dtypes(include=['float64', 'int64']).columns.values)

    # Remove data with missing values.
    # Remove all data rows where a numeric value is NaN (not a number), which
    # are indicated by '?' in the arff file. See matlab function ``isnan()''.
    nanIdx = np.isnan(X).any(axis=1)
    X = X[~nanIdx, :]

    # Convert the class labels to numeric +1/-1.
    # Store the class labels into a numerical vector T. Remove that column from X.
    T = df['class'].apply(eval).values
    T = T[~nanIdx]  # Remove the rows with missing values

    # Convert the data into a numeric matrix X, if you haven't already.
    # X: one row per data sample, and one column for each feature.

    return X, T, names
