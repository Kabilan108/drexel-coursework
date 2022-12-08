function  [results,hyp] = REMsleepanalysis(txtfile)
%Input of EEG signal text file
% Creates 'score' matrix determining sleep stage for every 30 seconds
% % 0 = wake
% % 1 = Sleep stage 1
% % 2 = Sleep stage 2
% % 3 = Sleep stage 3
% % 4 = Sleep stage 4
% % 5 = REM sleep 
% Analyzes score results to determine if REM occured in first 30 mins
% % Narcolepsy is present if REM sleep occurs within 30 minutes for two
% or more naps


if nargin == 0
    txtfile = 'narco1.txt';
end


% Analysis first file input
start=0;
hyp= []; %hypnogram
h=[];    %hours
m=[];    %minutes
s=[];    %seconds
[file, path]=uigetfile(txtfile,'Select report with annotations');
path(end)=[];
cd (path)
ptr = fopen(file,'r'); %opens the .txt files and returns the id

while 1
    tline = fgetl(ptr); 
   
    if ~ischar(tline),
        break,
    end
    if numel(tline)>10
    if tline(1:11)=='Sleep Stage'
       start=1;
       k=0; %hyp counter
       j=0; %CAP counter
    end
    if start==1

            p=strfind(tline,':');
            if numel(p)==0
                p=strfind(tline,'.');
            end
            if tline(p(2)+4:p(2)+5)=='SL'      %sleep stage: write on hyp
                k=k+1;
                if tline(p(2)+11)=='E'  %REM
                    hyp(k,1)=5;
                elseif tline(p(2)+11)=='T'  %MT
                    hyp(k,1)=7;
                    
                else
                    hyp(k,1)=str2num(tline(p(2)+11)); %sleep stage 0 1 2 3 4
                end

                h(k)=str2num(tline(p(1)-2:p(1)-1));
                m(k)=str2num(tline(p(1)+1:p(1)+2));
                s(k)=str2num(tline(p(2)+1:p(2)+2));
                if h(k)<10
                    hyp(k,2)=(h(k)+24)*3600+m(k)*60+s(k);
                else
                    hyp(k,2)=h(k)*3600+m(k)*60+s(k);
                end
            elseif (tline(p(2)+4:p(2)+5)=='MC') %CAP A phase: write on time_tot, duration, type
                j=j+1;
                t=strfind(tline,'-');
                type_ar(j)=str2num(tline(t(1)+2));
                duration(j,1)=str2num(tline(t(1)+4:t(1)+5));

                hCAP(j)=str2num(tline(p(1)-2:p(1)-1));
                mCAP(j)=str2num(tline(p(1)+1:p(1)+2));
                sCAP(j)=str2num(tline(p(2)+1:p(2)+2));
                if hCAP(j)<10
                    timevector(j,1)=(hCAP(j)+24)*3600+mCAP(j)*60+sCAP(j);
                else
                    timevector(j,1)=hCAP(j)*3600+mCAP(j)*60+sCAP(j);
                end
            end
    end
    end
end
hyp(:,2)=hyp(:,2)-hyp(1,2);
score = hyp; % 1095x2 double with sleep score in first column and seconds in second column
% Create matrix nap with only sleep scores for first thirty minutes

nap = score(1:60, :);

if ismember(5, nap) == 1
    results=1
    %fprintf('REM detected');
else
    results=0
    %fprintf('REM not detected');
end



end

