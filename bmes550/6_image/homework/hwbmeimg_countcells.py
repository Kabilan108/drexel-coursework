"""
Functions for Image Processing

By Tony Kabilan Okeke <mailto:tko35@drexel.edu>
"""

# Import the required libraries
import matplotlib.pyplot as plt
import skimage.io as io
import numpy as np

# Import the bmes module
import sys, os
sys.path.append(os.environ['BMESAHMETDIR'])
import bmes


def myimshow(img: np.ndarray, title: str='', dbg: bool=True) -> None:
    """
    Show an image with a title
    """

    if dbg:
        io.imshow(img)
        if title: plt.title(title)
        io.show();


def hwbmeimg_countcells(file: str='', dbg: bool=False) -> int:
    """
    Count the cells in a microscopy image
    """

    # If no file is given, download the sample image
    if not file:
        URL = ('http://sacan.biomed.drexel.edu/lib/exe/fetch.php'
               '?media=course:bcomp2:img:samplecells.jpg')
        file = bmes.downloadurl(URL, './samplecells.jpg')
    
    # Read the image data from the file
    img = io.imread(file)
    myimshow(img, 'Original Image', dbg);

    # Apply sobel edge detection

    # Dilate the edge image

    # Fill the interior gaps of the edge image

    # Smoothen the objects in the edge image

    # Show the edge image overlayed on the original image
    if dbg:
        pass

    # Find the connected components in the edge image

    # Count the number of cells in the image

    return 0
