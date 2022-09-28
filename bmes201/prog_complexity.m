function ret=prog_complexity( file, dbg )
% This function strips all comments and reduces variable names to a single
% character and reports the code complexity.
% Provide the file name for your matlab code. e.g.,:
% >> prog_complexity( 'femalechdrisk.m' )
% ans =
%   548
% Copyright (C) 2016, 2017 by Ahmet Sacan
if ~exist('dbg','var'); dbg=false; end

ret=0;
s=fileread( file );
if strcmp(file(end-1:end),'.m')
	[commentlocs,stringlocs]=matlab_locatestringsandcomments(s);
	for i=1:size(stringlocs,1); s(stringlocs(i,1):stringlocs(i,2))=' '; ret=ret+stringlocs(i,2)-stringlocs(i,1)+1; end %remove strings (that are not orphan)
	for i=1:size(commentlocs,1); s(commentlocs(i,1):commentlocs(i,2))=' '; end %remove all comments.
	s(s==',')=' ';
	s(s==';')=' ';
	s=strrep(s,'...',' ');
else %we'll assume it's python.
	%locate '__main__' before we strip off strings. TODO: get all such
	%matches and remove any that are within strings.
	[beginmain,endmainline]=regexp(s,'\nif\s+__name__\s*==\s*''__main__''\s*:','start','end','once');
	if ~isempty(beginmain)
		%find the ending of the indentation.
		endmain=regexp(s(endmainline+1:end),'\n[^\s]','start','once');
		if isempty(endmain); endmain=numel(s);
		else endmain=endmainline+endmain; end
		s(beginmain:endmain)=' ';
	end
	[commentlocs,stringlocs,orphanstringlocs]=py_locatestringsandcomments(s);
	for i=1:size(stringlocs,1); s(stringlocs(i,1):stringlocs(i,2))=' '; ret=ret+stringlocs(i,2)-stringlocs(i,1)+1; end %remove strings (that are not orphan)
	for i=1:size(commentlocs,1); s(commentlocs(i,1):commentlocs(i,2))=' '; end %remove all comments.
	for i=1:size(orphanstringlocs,1); s(orphanstringlocs(i,1):orphanstringlocs(i,2))=' '; end %remove orphanstrings (docstrings,etc.)
	s=regexprep(s,'\\\n',' '); %don't penalize line-continuation character.
	s(s==';')=' '; %don't penalize semicolon.
end

if dbg
	fprintf('Strings are counted and removed. Total length of all strings is: %d\n',ret);
	fprintf('Comments are removed. Remaining code is:\n  %s\n',regexprep(regexprep(s,'[ \t]+',' '),'\s*\n\s*','\n  '));
end
%replace all words with a single letter 'X'
s=regexprep(s,'\<([a-zA-Z]\w*)\>','X');
%remove all space characters.
s=regexprep(s,'\s','');
ret=ret+ numel(s);


%func_embed_list: matlab_locatestringsandcomments,py_locatestringsandcomments,eol

%---------------------------------------------------------
%<begin_matlab_locatestringsandcomments>
function [commentlocs,stringlocs]=matlab_locatestringsandcomments(s)
% TODO: now matlab allows double-quoted string objects. Update this to
% allow that.
% Copyright (C) 2016 by Ahmet Sacan
if ~exist('s','var');
	%s=['' eol '=""'];
	%s='d=Dog(''a'');';
	s=fileread('R:\temp.m');
end

commentlocs=[];
stringlocs=[];

markerlist={};
markerlocs=[];
locs=find(s==''''); %we'll decide which of these are transpose operator later.
markerlist=[markerlist repmat({''''},1,numel(locs))]; markerlocs=[markerlocs locs];


if exist('string','class') %double-quotes became available after R2017a
	locs=find(s=='"');
	markerlist=[markerlist repmat({'"'},1,numel(locs))]; markerlocs=[markerlocs locs];
end

locs=regexp(s,'(^|\n)\s*%{\s*\n');
locs=locs+1; locs(locs==2)=1; %don't include the newline as part of the start.
markerlist=[markerlist repmat({'%{'},1,numel(locs))]; markerlocs=[markerlocs locs];
locs=regexp(s,'\n\s*%}\s*(\n|$)','end');
markerlist=[markerlist repmat({'%}'},1,numel(locs))]; markerlocs=[markerlocs locs];

locs=find(s=='%');
markerlist=[markerlist repmat({'%'},1,numel(locs))]; markerlocs=[markerlocs locs];

locs=find(s==eol);
markerlist=[markerlist repmat({eol},1,numel(locs))]; markerlocs=[markerlocs locs];


[markerlocs,I]=sort(markerlocs);
markerlist=markerlist(I);

mi=0;
while mi<numel(markerlocs)
	
	% get the next marker
	mi=mi+1; marker=markerlist{mi};
	if strcmp(marker,eol)||strcmp(marker,'%}'); continue; end

	% make sure this is a not a transpose operator.
%{
https://www.mathworks.com/matlabcentral/newsreader/view_thread/25108
	 A single quotation character is a tranpose operator if it
   follows a right bracket ("]"), right parenthesis (")"),
   right brace ("}"), letter, digit, underline ("_"),
   punctuation mark ("."), or another single quote character
   ("'").
%}
	if strcmp(marker,'''')&&markerlocs(mi)>1&& ~isempty(regexp(s(markerlocs(mi)-1),'[\]\)\}a-zA-Z0-9_\.]','once')); continue; end
	
	
	markerloc=markerlocs(mi);
	if strcmp(marker,'%'); nextmarker=eol;
	elseif strcmp(marker,'%{'); nextmarker='%}';
	else nextmarker=marker; end %only remaining option here is single quote 
	
	%find the matching nextmarker
	foundnextmarker=false;
	while mi<numel(markerlocs)
		mi=mi+1;
		if strcmp(markerlist{mi},nextmarker);
			%make sure this is not first of a double-single-quote (which needs to be ignored).
			if strcmp(nextmarker,'''')&&numel(s)>=markerlocs(mi)&&numel(s)>markerlocs(mi)&&s(markerlocs(mi)+1)==''''; continue; end
			foundnextmarker=true; break;
		end
	end
	if strcmp(marker,'%')||strcmp(marker,'%{')
		if foundnextmarker; commentlocs=[commentlocs; markerloc markerlocs(mi)-1];
		else commentlocs=[commentlocs; markerloc numel(s)]; end
	else
		if foundnextmarker; stringlocs=[stringlocs; markerloc markerlocs(mi)+numel(nextmarker)-1];
		else stringlocs=[stringlocs; markerloc numel(s)]; end %an unclosed string is an error. but we'll ignore that. just use to the end of string.
	end	
end

%condense consequtive comments
for i=size(commentlocs,1)-1:-1:1
	if commentlocs(i,2)+2==commentlocs(i+1,1) && s(commentlocs(i,2)+1)==eol
		commentlocs(i,2)=commentlocs(i+1,2);
		commentlocs(i+1,:)=[];
	end
end

if ~nargout 	%meant for debugging purposes:
	commentlocs,stringlocs
	fprintf('Marking comments with %% and strings with # gives the following:\n');
	for i=1:size(commentlocs,1); s(commentlocs(i,1):commentlocs(i,2))='%'; end
	for i=1:size(stringlocs,1); s(stringlocs(i,1):stringlocs(i,2))='#'; end	
	fprintf('%s',str_eol(s));
	clear commentlocs;
end
%<end_matlab_locatestringsandcomments>

%---------------------------------------------------------
%<begin_py_locatestringsandcomments>
function [commentlocs,stringlocs,orphanstringlocs]=py_locatestringsandcomments(s)
% orphanstrings are the strings that are not being used. (e.g., docstrings)
% if orphanstrings is requested, we remove them from stringlocs.
% Copyright (C) 2016 by Ahmet Sacan
if ~exist('s','var');
	s=fileread('r:/temp.py');
	%s=['' eol '=""'];
	%s='d=Dog(''a'');';
end

commentlocs=[];
stringlocs=[];
orphanstringlocs=[];

markerlist={};
markerlocs=[];
for q='"'''
	tripleq=[q q q];
	blocklocs=strfind(s,tripleq);
	markerlist=[markerlist repmat({tripleq},1,numel(blocklocs))]; markerlocs=[markerlocs blocklocs];
	locs=s==q;
	locs([blocklocs blocklocs+1 blocklocs+2])=false; %only keep quotes that are not part of triple-quotes.
	locs=find(locs);
	markerlist=[markerlist repmat({q},1,numel(locs))]; markerlocs=[markerlocs locs];
end

%remove any quote that follow an odd number of backslashes.
for i=numel(markerlocs):-1:1
	loc=markerlocs(i)-1;
	numbackslashes=0;
	while loc && s(loc)=='\'; numbackslashes=numbackslashes+1; loc=loc-1; end
	if mod(numbackslashes,2); markerlocs(i)=[]; markerlist(i)=[]; end
end


locs=find(s=='#');
markerlist=[markerlist repmat({'#'},1,numel(locs))]; markerlocs=[markerlocs locs];

locs=find(s==eol);
markerlist=[markerlist repmat({eol},1,numel(locs))]; markerlocs=[markerlocs locs];

[markerlocs,I]=sort(markerlocs);
markerlist=markerlist(I);

mi=0;
while mi<numel(markerlocs)
	% get the next marker
	mi=mi+1; marker=markerlist{mi};
	if strcmp(marker,eol); continue; end
	markerloc=markerlocs(mi);
	if strcmp(marker,'#'); nextmarker=eol;
	else nextmarker=marker; end
	
	%find the matching nextmarker
	foundnextmarker=false;
	while mi<numel(markerlocs)
		mi=mi+1;
		if strcmp(markerlist{mi},nextmarker); foundnextmarker=true; break; end
	end
	if strcmp(marker,'#')
		if foundnextmarker; commentlocs=[commentlocs; markerloc markerlocs(mi)-1];
		else commentlocs=[commentlocs; markerloc numel(s)]; end
	else
		if foundnextmarker; stringlocs=[stringlocs; markerloc markerlocs(mi)+numel(nextmarker)-1];
		else stringlocs=[stringlocs; markerloc numel(s)]; end %an unclosed string is an error. but we'll ignore that. just use to the end of string.
	end	
end

%condense consequtive comments
for i=size(commentlocs,1)-1:-1:1
	if commentlocs(i,2)+2==commentlocs(i+1,1) && s(commentlocs(i,2)+1)==eol
		commentlocs(i,2)=commentlocs(i+1,2);
		commentlocs(i+1,:)=[];
	end
end

if ~nargout||nargout>2
	for i=size(stringlocs,1):-1:1
		if i==1; sbefore=s(1:stringlocs(i,1)-1);
		else sbefore=s(stringlocs(i-1,2)+1:stringlocs(i,1)-1); end
		if ~isempty(regexp(sbefore,'(^|\n)\s*$','once')) && isempty(regexp(sbefore, '\\\n\s*$','once'))
			orphanstringlocs=[orphanstringlocs; stringlocs(i,:)];
			stringlocs(i,:)=[];
		end
	end
end

if ~nargout
	commentlocs,stringlocs,orphanstringlocs
	clear commentlocs;
end
%<end_py_locatestringsandcomments>

%---------------------------------------------------------
%<begin_eol>
function s=eol()
%return a new line character.
% Copyright (C) 2006 by Ahmet Sacan
%s=sprintf('\n');
s=char(10);
%<end_eol>