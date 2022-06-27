function [] = channelselect(handles,type)

% if the channel is 1 or 2
if strcmpi(class(type),'double')
    str = num2str(type);
    axes(handles.(['fig' str 'axes']));
    currChannel = handles.(['img' str 'Channel']).Value;
    %axes(handles.fig2axes);
    %currChannel = handles.img2Channel.Value;
    if isfield(handles,['I' str])
        imshow(handles.(['I' str]){currChannel});
    end
    handles.(['fig' str 'axes']).Visible='On';
elseif ischar(type)
    % otherwise, it's the merged channel
    axes(handles.figMergeaxes);
    currChannel = handles.imgMergeChannel.Value;
    if isfield(handles,'I1') && isfield(handles,'I2')
        imshowpair(handles.I1{currChannel}, handles.I2{currChannel},'Scaling','joint')
    elseif isfield(handles,'I1')
        imshow(handles.I1{currChannel});
    else
        imshow(handles.I2{currChannel});
    end
end

end