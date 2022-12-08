function [handles] = imgselect(handles, iNum)
% prompt the user to select the file
path = bmes.datadir;
filter = ['*.lsm;*.jpeg,*.jpg,*.png,*.bmp'];
[selectedFile, filePath] = uigetfile(fullfile(path , filter));
[~,~,ext] = fileparts(selectedFile);

% if .lsm files, then use use lsmread to read the file
if strcmpi(ext,'.lsm')
    [Iraw] = lsmread([filePath selectedFile]);
    Iraw = squeeze(Iraw(1,:,:,:,:));
    nChannels = size(Iraw,1);
    
    I = cell(nChannels,1);
    for i = 1:nChannels
        I{i} = squeeze(Iraw(i,:,:,:));
        I{i} = mat2gray(squeeze(max(I{i},[],1)));
    end
    if nChannels<3
        I{3} = I{2};
    end
else
    % otherwise, use the inbuilt imread
    I = repmat({imread([filePath selectedFile])},3,1);
end

str = num2str(iNum);
% update handles
handles.(['imgFName' str]).String = selectedFile;
handles.(['imgFPath' str]) = filePath;
handles.(['I' str]) = I;

% get the current channel
Chan = handles.(['img' str 'Channel']).Value;

% plot the image in the corresponding image panel
axes(handles.(['fig' str 'axes']));
imshow(handles.(['I' str]){Chan});

axes(handles.figMergeaxes);
if iNum == 1
    checkField = 'I2';
else
    checkField = 'I1';
end
% check if the other image is uploaded
if isfield(handles,checkField)
    % if so, then plot the overlay on the merged image panel
    ChanMerge = handles.imgMergeChannel.Value;
    imshowpair(handles.I1{ChanMerge}, handles.I2{ChanMerge},'Scaling','joint')
else
    % if not, then only plot the current image on the merged image panel
    imshow(handles.(['I' str]){Chan});
end

end