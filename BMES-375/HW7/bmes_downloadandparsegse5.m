function gsedata=bmes_downloadandparsegse5(gseid)
% * Download e.g.,
% ftp://ftp.ncbi.nih.gov/pub/geo/DATA/SeriesMatrix/GSE5847/GSE5847_series_matrix.txt.gz
% * gunzip()
% * geoseriesread()

%TODO: This function takes time! You should spend some effort to "cache"
%its results.

if ~exist('gseid','var'); gseid='GSE5847'; end




url = sprintf('ftp://ftp.ncbi.nlm.nih.gov/geo/series/GSE5nnn/%s/matrix/%s_series_matrix.txt.gz',gseid,gseid);
gzfile = [tempdir '/' sprintf('%s.txt.gz',gseid)];
fprintf('Downloading %s ...\n',url);
urlwrite(url, gzfile);
files = gunzip( gzfile );
file = files{1};

fprintf('Reading %s ...\n',file);
gsedata = geoseriesread( file );



