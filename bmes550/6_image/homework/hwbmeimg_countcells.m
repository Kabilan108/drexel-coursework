function count=hwbmeimg_countcells(file,dbg)
% by [[Write your fullname(s) here]]

%%	* If file argument is not given or is empty, use: file=bmes.downloadurl('http://sacan.biomed.drexel.edu/lib/exe/fetch.php?media=course:bcomp2:img:samplecells.jpg','samplecells.jpg',true);
if ~exist('file','var'); file=bmes.downloadurl('http://sacan.biomed.drexel.edu/lib/exe/fetch.php?media=course:bcomp2:img:samplecells.jpg','samplecells.jpg'); end

%%	* If dbg argument is not given, use dbg=true;
if ~exist('dbg','var'); dbg=true; end

%%	* Read the image data from the file. imread()
%		* if dbg is on, show this image.
img = imread(file);
if dbg; figure(); imshow(img); title('original image'); end


%%  * Apply sobel edge detection. edge()
%		* if dbg is on, show the edges as a binary image.


%%	* Dilate the edge image. imdilate()
%		* if dbg is on, show the dilated edge image.



%%	* Fill interior gaps of the edge image. imfill()
%		* if dbg is on, show the filled edge image.



%%	* Smoothen the objects in the edge image. imerode()
%		* if dbg is on, show the smoothened edge image.



%%	* If dbg is on, show the edge image overlayed on the original image.



%%	* Find the connected components in edge image. bwconncomp()


%%	* Return the number of cells found.

