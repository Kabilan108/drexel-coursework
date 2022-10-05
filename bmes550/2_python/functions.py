
import os


def getprostaterisk(
    history: bool, 
    euro_ances: float, 
    repeat: int, 
    haplotype: str
) -> float:
    """
    Compute the risk of prostate cancer using factors identified in "Decision 
    Tree-Based Modeling of Androgen Pathway Genes and Prostate Cancer Risk", 
    Cancer Epidemiol Biomarkers Prev. 2011 Jun; 20(6): 1146–1155

    Parameters
    ----------
    history : bool
        Does the patient have family history of prostate cancer
    euro_ances : float
        The patient's European ancestry as a percentage (0.5 = 50%)  
    repeat : int
        The number of AR GGC repeat polymorphisms in the patient's genome
    haplotype : str
        The patient's CYP3A4/CYP3A5 haplotype, one of "AA", "AG", "GG", "GG"

    Returns
    -------
    risk : float
        The patient's risk of prostate cancer relative to the 
    """

    assert isinstance(history, bool), "history must either be True or False"
    assert 0 <= euro_ances <= 1, "euro_ances must be between 0 and 1"
    assert isinstance(repeat, int), "repeat must be an integer"
    assert isinstance(haplotype, str), \
        "haplotype must be one of 'AA', 'AG', 'GG', or 'GG'"
    haplotype = haplotype.upper()

    # Compute risk
    if history:
        if euro_ances >= 0.204:
            if haplotype in ['GA', 'AG', 'GG']:
                risk = 6.24
                denom = 7 + 14
            else:
                risk = 0.94
                denom = 10 + 3
        else:
            if repeat < 16:
                risk = 5.46
                denom = 4 + 7
            else:
                risk = 1.56
                denom = 38 + 19
    else:
        risk = 1.00
        denom = 343 + 110

    # return #prostate / (#numprostate + #control)
    return risk


def knearestneighbors(v: list, x: float, k: int=3) -> list:
    """
    Find the k nearest neighbors of x in the list x

    Parameters
    ----------
    v : list
        List of numbers to search
    x : float
        The number to find the k nearest neighbors of
    k : int
        The number of nearest neighbors to return

    Returns
    -------
    neighbors : list
        The k nearest neighbors of x in the list x
    """

    assert isinstance(v, list), "x must be a list"
    assert k > 0, "k must be greater than 0"

    # Find the k nearest neighbors
    neighbors = sorted(v, key=lambda y: abs(y - x))[:k] 

    return neighbors


def filterpatients(patients: list) -> list:
    """
    Filter out female patients between 30 and 40 (inclusive) from a list of 
    patients.

    Parameters
    ----------
    patients : list
        A list of dictionaries which define the patient's name, gender and age

    Returns
    -------
    patients : list
        List of patient names
    """

    assert isinstance(patients, list), "patients must be a list"

    return [p['name'] for p in patients if 30 <= p['age'] <= 40 and p['gender'] == 'f']


def searchinfile(filename: str, keyword: str) -> list:
    """
    Search a file for the given keyword and return a list of the lines where 
    the keyword was found.

    Parameters
    ----------
    filename : str
        The name of the file to search
    keyword : str
        The keyword to search for

    Returns
    -------
    lines : list
        The lines where the keyword was found
    """

    assert os.path.exists(filename), "file does not exist"
    assert isinstance(keyword, str), "keyword must be a string"

    # Read the file
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Search for the keyword
    return [i for i, line in enumerate(lines) if keyword in line]
    



if __name__ == '__main__':
    # Test the functions

    # Test getprostaterisk
    try: 
        assert getprostaterisk(True, 0.5, 16, 'GA') == 6.24
        assert getprostaterisk(True, 0.1, 16, 'AA') == 1.56
        assert getprostaterisk(False, 0.8, 12, 'GG') == 1.00
        print("getprostaterisk passed")
    except AssertionError as e:
        print("getprostaterisk failed")
        print(e)
    except Exception as e:
        print("Unexpected error")
        print(e)

    # Test knearestneighbors
    try:
        assert knearestneighbors([73,90,99,77,59], 70, 2 ) == [73, 77]
        assert knearestneighbors([73,90,99,77,59], 90, 2 ) == [90, 99]
        assert knearestneighbors([73,90,99,77,59,90], 90, 2 ) == [90, 90]
        assert knearestneighbors([91,58,85,74,59,25,67,9,63,67], 57 ) == [58, 59, 63]
        print("knearsestneighbors passed")
    except AssertionError as e:
        print("knearestneighbors failed")
        print(e)
    except Exception as e:
        print("Unexpected error")
        print(e)

    # Test filterpatients
    try:
        patients1 = [ 
            {'name':'mary','gender':'f','age':25},
            {'name':'john','gender':'m','age':35},
            {'name':'anna','gender':'f','age':30},
            {'name':'paul','gender':'m','age':22},
            {'name':'elaina','gender':'f','age':38} 
        ]
        patients2 = [
            {'name':'mary','gender':'f','age':37},
            {'name':'john','gender':'m','age':35}
        ]

        assert filterpatients(patients1) == ['anna', 'elaina']
        assert filterpatients(patients2) == ['mary']
        print("filterpatients passed")
    except AssertionError as e:
        print("knearestneighbors failed")
        print(e)
    except Exception as e:
        print("Unexpected error")
        print(e)