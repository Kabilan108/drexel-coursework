# BrainCellRegistration
BrainCellRegistration is a MATLAB GUI used for registration of tissue samples and cell detection


## Installation
1. Install [SQLite](https://sqlitestudio.pl/index.rvt?act=download)
2. Install [7zip](https://www.7-zip.org/download.html)
3. Install [MATLAB](https://www.mathworks.com/)
   * Required toolboxes: [Image Processing](https://www.mathworks.com/help/images/index.html?s_tid=CRUX_lftnav), [Database Processing](https://www.mathworks.com/products/database.html)

## Usage

```matlab
>>BrainCellRegistration

% to unzip files
[status,result] = system(['"pathto\7z.exe" -y x ' '"' ... [bmes.tempdir '\filename.lsm.bz2'] '"' ' -o' '"' ...
bmes.datadir '"']);

```

## Functions


* **imgselect.m**: User selects images, performs maximum projection, and plots the images in GUI image handles
* **channelselect.m**: Updates images in image handles based on the currently selected color channels
* **preprocess.m**: Preregister image by performing rotation
* **applyRegOpts.m**: Thresholding for registration, obtains corners for ROI and creates mask
* **preimgreg.m**: View the ROI and the result of thresholding
* **runimgreg.m**: Run either image registration
* **celldetect.m**: Perform cell detection
* **savedatabase.m**: Save relevant information to database. If no database exists, then initialize the database

