"""
Functions for Image Processing

By Tony Kabilan Okeke <mailto:tko35@drexel.edu>
"""

# Import the bmes package
import sys, os
sys.path.append(os.environ['BMESAHMETDIR'])
import bmes

# Import necessary packages
import matplotlib.pyplot as plt
import numpy as np
from skimage import io, color, filters,  morphology, measure
from scipy import ndimage


def myimshow(img: np.ndarray, title: str='', dbg: bool=True) -> None:
    """
    Show an image with a title
    """

    if dbg:
        io.imshow(img)
        if title: plt.title(title)
        io.show();
        

def bmeimg_countcells(file: str='', dbg: bool=True, edge_thr: float=0.1) -> int:
    """
    Count the cells in a microscopy image

    Parameters
    ----------
    file : str
        The file name of the image to be processed
    dbg : bool
        Whether to show the intermediate steps
    edge_thr : float
        The threshold for the edge detection (used to convert the Sobel edge
        image to a binary image)
    """

    # If no file is specified, use the default file
    if not file:
        URL = ('http://sacan.biomed.drexel.edu/lib/exe/fetch.php'
               '?media=course:bcomp2:img:samplecells.jpg')
        file = bmes.downloadurl(URL, './samplecells.jpg');

    # Read the image
    I = io.imread(file)

    # Convert to grayscale for processing
    G = color.rgb2gray(I)

    # Edge detection (Sobel)
    E = filters.sobel(G, mode='constant')
    # Convert to a binary image
    E = np.where(E > edge_thr, 1, 0).astype(np.float64)

    # Image dilation
    D = morphology.dilation(E, morphology.diamond(5))

    # Gap filling
    seed = D.copy()
    seed[1:-1, 1:-1] = D.max()
    F = morphology.reconstruction(seed, D, method='erosion')

    # Smoothening (erosion)
    S = morphology.erosion(F, morphology.square(2)).astype(np.float64)

    # Count the number of objects
    L, _ = ndimage.label(S)  # type: ignore

    # Remove small objects
    blobs = measure.regionprops(L)
    blobs = [b for b in blobs if b.area > 200]
    n = len(blobs)

    # Construct a labeled image
    L = np.zeros(L.shape)
    for i, b in enumerate(blobs, 1):
        L[b.coords[:,0], b.coords[:,1]] = i
    L = L.astype(np.int32)

    # Overlay the labeled image on the original image
    O = color.label2rgb(L, I, bg_label=0)

    # Display the results
    if dbg:
        fig, axes = plt.subplots(2, 3, figsize=(12, 8))
        axes = axes.flatten()  # type: ignore
        titles = ['Original Image', 'Edge Detection (Sobel)', 'Dilated Image', 
                'Filled Edge Image', 'Smoothened Image', 'Overlay']
        for ax, img, title in zip(axes, [I, E, D, F, S, O], titles):
            ax.imshow(img, cmap='gray' if img.ndim == 2 else None)
            ax.set_title(title)
        plt.tight_layout()

    return n
