function gpldata=bmes_downloadandparsegpl(gplid)
% * Download e.g.,
% http://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?form=text&acc=GPL96&view=full
% * geosoftread()

%TODO: This function takes time! You should spend some effort to "cache"
%its results.

if ~exist('gplid','var'); gplid='GPL96'; end


if any(exist('bmes_downloadandparsegpl_ahmet')==[2 5 6]); gpldata=eval('bmes_downloadandparsegpl_ahmet(gplid)'); return; end

url = sprintf('https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?form=text&acc=%s&view=full',gplid);
file = [tempdir '/' gplid '.txt'];
urlwrite(url, file);
gpldata = geosoftread( file );
