function [currI1,currI2,thresh,vertices,mask] = applyRegOpts(handles)

thresh = max(1,str2double(handles.regThresh.String))./100;

currChannel = handles.img1Channel.Value;
currI1 = handles.I1{currChannel};
currI1(currI1<thresh) = 0;

currChannel = handles.img2Channel.Value;
currI2 = handles.I2{currChannel};
currI2(currI2<thresh) = 0;

if all(isfield(handles,{'TLCorner','TRCorner','BLCorner','BRCorner'}))
    try
        tmp(1,:) = regexp(handles.TLCorner.String,'\d*','Match');
    catch
        tmp(1,:) = {'1',num2str(size(currI1,2))};
    end
    try
        tmp(2,:) = regexp(handles.TRCorner.String,'\d*','Match');
    catch
        tmp(2,:) = {num2str(size(currI1,1)),num2str(size(currI1,2))};
    end
    try
        tmp(3,:) = regexp(handles.BLCorner.String,'\d*','Match');
    catch
        tmp(3,:) = {num2str(size(currI1,1)),'1'};
    end
    try
        tmp(4,:) = regexp(handles.BRCorner.String,'\d*','Match');
    catch
        tmp(4,:) = {'1','1'};
    end
    vertices = cell2mat(cellfun(@str2num,tmp,'un',0));
else
    vertices = [1,size(currI1,1);
        size(currI1,1),size(currI1,1);
        size(currI1,1),1;
        1,1];
end

mask = poly2mask(vertices(:,1),vertices(:,2),size(currI1,1),size(currI1,2));

end