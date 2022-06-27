function [out]=Rexe(varargin)
% return location of R executable.
% search for common installation locations.
%
% Adapted from Ahmet Sacan's "bmes.pyexe"

persistent ret;
if ~isempty(ret)&&isempty(varargin); out=ret; return; end


if isempty(ret)&&ispc
	tryfile=['C:/"Program Files"/R/R-4.2.0/bin/Rscript.exe'];

    %quirky, but isfile doesnt recognize quotes needed by powershell...
	if bmes.isfile('C:/Program Files/R/R-4.2.0/bin/Rscript.exe')
        ret=tryfile;
    end
	
end


if isempty(ret); ret='/Library/Frameworks/R.framework/Resources/Rscript'; end %this is our fallback command if we don't find a specific location.

out=ret;
end
