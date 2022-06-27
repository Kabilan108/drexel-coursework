function [handles] = savedatabase(handles)
dbfile = fullfile(bmes.datadir, 'BrainCellResults.db');

if ~exist([bmes.datadir '/BrainCellResults.db'],'file') %if database doesn't exist, create new database
    conn = sqlite(dbfile, 'create');
    createTable = ['CREATE table Imageinfo' ...
        '(id INTEGER, date DATE, img1_data VARCHAR, img2_data VARCHAR, filename_img1 VARCHAR,'...
        'filename_img2 VARCHAR, cellnum_img1 INTEGER, cellnum_img2 INTEGER, cellnum_merge INTEGER)'];
    exec(conn, createTable)
else
    conn =  sqlite(dbfile, 'connect');
end

% if the folder to save the processed mat file does not exist, create it
matFolder = [bmes.datadir '/RegisteredMatFiles'];
if ~exist(matFolder, 'dir')
    mkdir(matFolder)
end
% save th emat files
matFile1 = [matFolder '/' handles.imgFName1.String(1:end-4) '.mat'];
matFile2 = [matFolder '/' handles.imgFName2.String(1:end-4) '.mat'];
I = handles.I1;save(matFile1,'I')
I = handles.I2;save(matFile2,'I')

% if cell detection was not done, then use nans for number of cells/overlap
if ~isfield(handles,'cells')
    handles.cells.i1 = nan;
    handles.cells.i2 = nan;
    handles.cells.iOverlap = nan;
end

% fetch and increment the id
currIds = fetch(conn,'SELECT id FROM Imageinfo');
newId = max([cell2mat(currIds); 0])+1;

% insert the current to the database
colnames = {'id','date', 'img1_data' , 'img2_data',...
    'filename_img1' , 'filename_img2','cellnum_img1' , 'cellnum_img2', 'cellnum_merge'};
insert(conn, 'Imageinfo', colnames, ...
    {newId,handles.editdate.String,matFile1, matFile2, handles.imgFName1.String, handles.imgFName2.String,...
    handles.cells.i1, handles.cells.i2, handles.cells.iOverlap});

%close the connection
close(conn)
handles.dbStatus.String = ['Database Updated; newest id = ' num2str(newId)];

end
