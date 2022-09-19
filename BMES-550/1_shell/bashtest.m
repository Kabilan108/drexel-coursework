%% set up location of BASH
BASH ='bash';
if ispc
	if exist('C:/cygwin/bin/bash.exe','file')
		BASH ='C:/cygwin/bin/bash.exe';
	elseif exist('C:/cygwin64/bin/bash.exe','file')
		BASH ='C:/cygwin64/bin/bash.exe';
	end
	setenv('PATH', [ fileparts(BASH) ';' getenv('PATH')  ] )
end

%% helloworld.sh
system([ BASH ' helloworld.sh 2>&1']);


%% wctop10lines.sh
system([ BASH ' wctop10lines.sh 2>&1']);


%% listmyhome.sh
system([ BASH ' listmyhome.sh 2>&1']);


%% backupself.sh
delete backupself.sh.bak
system([ BASH ' backupself.sh 2>&1']);
info=dir('backupself.sh.bak')


%% findrecentdocx.sh
% Write your own test case here. As argument, use a folder that does contain
% some recently modified docx files. Create new docx files in that folder
% if you do not have any docx files.


%% compareab.sh
% Write your own test case here.
