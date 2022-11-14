import sys,os; sys.path.append(os.environ['BMESAHMETDIR']); import bmes
bmes.pipinstall('skimage','scikit-image')

from skimage import io

#rather than repeating this block of code many times, let's define a function for it:
def myimgshow(img,title=None,dbg=True):
    from skimage import io
    import matplotlib.pyplot as plt
    if dbg:
        io.imshow(img)
        if title: plt.title(title)
        io.show();


def hwbmeimg_countcells(file=None,dbg=False):
    # by [[Write your fullname(s) here]]
    # takes a microscopy image file and returns the number of cells detected.


    ##	* If file argument is not given or is empty, use: file=bmes.downloadurl('http://sacan.biomed.drexel.edu/lib/exe/fetch.php?media=course:bcomp2:img:samplecells.jpg','samplecells.jpg',true);
    if not file: file=bmes.downloadurl('http://sacan.biomed.drexel.edu/lib/exe/fetch.php?media=course:bcomp2:img:samplecells.jpg','samplecells.jpg');

    ##	* Read the image data from the file. imread()
    #		* if dbg is on, show this image.
    img = io.imread(file);
    myimgshow(img,'original image',dbg);


    ##  * Apply sobel edge detection. edge()
    #		* if dbg is on, show the edges as a binary image.


    ##	* Dilate the edge image. imdilate()
    #		* if dbg is on, show the dilated edge image.



    ##	* Fill interior gaps of the edge image. imfill()
    #		* if dbg is on, show the filled edge image.



    ##	* Smoothen the objects in the edge image. imerode()
    #		* if dbg is on, show the smoothened edge image.



    ##	* If dbg is on, show the edge image overlayed on the original image.



    ##	* Find the connected components in edge image. bwconncomp()


    ##	* Return the number of cells found.

