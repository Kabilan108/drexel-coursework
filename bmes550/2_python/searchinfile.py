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

import os


def searchinfile(filename: str, keyword: str) -> list:
    assert os.path.exists(filename), "file does not exist"
    assert isinstance(keyword, str), "keyword must be a string"
    keyword = keyword.lower()

    # Read the file
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Search for the keyword
    return [i for i, line in enumerate(lines, start=1) if keyword in line]
