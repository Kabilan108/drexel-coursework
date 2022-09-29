function [handles, num1, num2,nOverlap] = celldetect(handles, int_thres, min_size)

%--------------------------------------------------------------------------
% use handles.imgMergeChannel.Value if you want to use the current channel
% shown in the merge image 
% OR use handles.img1Channel.Value/handles.img2Channel.Value for the
% currently shown channel in image 1 or 2
% handles.I1 and handles.I2 have the images already loaded as matrices.
% These are 1xn cell arrays where each cell is a 2048x2048 image. For
% instance, handles.I1{1} will contain the image for the first channel for
% image 1
%--------------------------------------------------------------------------
img1 = handles.I1{handles.imgMergeChannel.Value};
img2 = handles.I2{handles.imgMergeChannel.Value};
%--------------------------------------------------------------------------
% there's no reason to do the merge. The merge image is just overlaying the
% second image over the first.
% Just: 1. generate a binary mask of cells for image 1 -> count number of
% cells
%       2. generate a binary mask of cells for image 2 -> count number of
% cells
%       3. Look to see how many of the cells have overlap between image 1
%       and 2
%--------------------------------------------------------------------------
%merge = handles.I1{handles.imgMergeChannel.Value};



[rows1, columns1, numberOfColorBands1] = size(img1);
[rows2, columns2, numberOfColorBands2] = size(img2);
%[rows3, columns3, numberOfColorBands3] = size(merge);

if numberOfColorBands1 > 1
    img1 = rgb2gray(img1);
elseif numberOfColorBands2 > 1
    img2 = rgb2gray(img2);
% elseif numberOfColorBands3 > 1
%     merge = rgb2gray(merge);
end   

%% int_thres  take the given intensity threshold, im2bw converts image to
%%binary image consisting of 1s and 0s based on a threshold value

result1 = im2bw(img1, int_thres);
result2 = im2bw(img2, int_thres);
%result3 = im2bw(merge, int_thres);

%% 
%tilde switches the intensities where cells have intensity of 1 and background has intensity of 0
result1=~result1;
result2=~result2;
%result3=~result3;

%% get rid of cells on the border, not sure if this is necessary
result1 = imclearborder(result1);
result2 = imclearborder(result2);
%result3 = imclearborder(result3);
%% bwmorph applies morphological effects, currently it is set to erode 3 times
result1 = bwmorph(result1, 'erode', 1);
result2 = bwmorph(result2, 'erode', 1);
%result3 = bwmorph(result3, 'erode', 1);
%% bwlabel labels connected components in 2-D binary images
[L1,num1] = bwlabel(result1);
[L2,num2] = bwlabel(result2);
%[L3,num3] = bwlabel(result3);
%% 

for i=1:num1
 area = length(find(L1==i));  %% area = length of each cell detected
 if area<min_size  %%if my area is less then the min_size given, then get rid of it by making it part of the background
     L1(L1==i) = 0; num1=num1-1;
 end
end

[L1, num1] = bwlabel(result1);


for i=1:num2
 area = length(find(L2==i));  %% area = length of each cell detected
 if area<min_size  %%if my area is less then the min_size given, then get rid of it by making it part of the background
     L2(L2==i) = 0; num2=num2-1;
 end
end

[L2, num2] = bwlabel(result2);

numAll = [num1 num2];
LAll = {L1, L2};
for imgN = 1:2
    stats = regionprops('table',LAll{imgN},'Centroid',...
            'MajorAxisLength','MinorAxisLength','ConvexHull');
    axes(handles.(['fig' num2str(imgN) 'axes']));hold on;
    for i = 1:numAll(imgN)
        plot(stats.ConvexHull{i}(:,1),stats.ConvexHull{i}(:,2),'Linewidth',2.5)
    end
    minLim = floor(min(cell2mat(stats.ConvexHull)));
    maxLim = ceil(max(cell2mat(stats.ConvexHull)));
    if all((maxLim - minLim) <300)
        centLim = (minLim+minLim)./2;
        xlim([centLim(1)-150 centLim(1)+150]);
        ylim([centLim(2)-150 centLim(2)+150]);
    else
        xlim([minLim(1)-25 maxLim(1)+25]);
        ylim([minLim(2)-25 maxLim(2)+25]);
    end
    hold off

end

percOverlap = zeros(num1,1);
for i = 1:num1
    currI = L1==i;
    percOverlap(i) = sum(sum(currI.*(L2>0)))./sum(currI(:));
end
nOverlap = sum(percOverlap>0.3);
