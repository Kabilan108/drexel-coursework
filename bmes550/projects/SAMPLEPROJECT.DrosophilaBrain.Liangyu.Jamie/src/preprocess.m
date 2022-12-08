function [handles] = preprocess(handles)
Chan1 = handles.img1Channel.Value;
Chan2 = handles.img2Channel.Value;
fixed = handles.I1{Chan1};
moving = handles.I2{Chan2};

handles.regStatus.String = 'Performing Rotation';pause(0.1)
MI = zeros(180,1);
for i = 1:2:180
    J = imrotate(moving,i,'nearest','crop');
    [MI(i)] = calcMI(fixed, J);
end
rotAng = find(MI == max(MI));
handles.regStatus.String = 'Ready for Registration';

for i = 1:numel(handles.I2)
    handles.I2{i} = imrotate(handles.I2{i},rotAng,'nearest','crop');
end

handles.rotateAmount.String = [num2str(rotAng) ' deg Rotation'];

end