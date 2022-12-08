function [handles] = runimgreg(handles)

[fixedRg,movingRg,thresh,vertices,mask] = applyRegOpts(handles);
fixedRg(~mask) = 0;movingRg(~mask) = 0;
%fixedRg = handles.I1{handles.img1Channel.Value};
%movingRg = handles.I2{handles.img2Channel.Value};

[optimizer, metric] = imregconfig('multimodal');
optimizer.MaximumIterations = 300;
optimizer.InitialRadius = optimizer.InitialRadius/3.5;

typeStr = handles.RegType.String{handles.RegType.Value};
if strcmpi(typeStr,'Rigid')
    type = 'rigid';
else
    type = 'affine';
end
handles.regStatus.String = ['Getting ' type ' Transformation'];pause(0.1)
tform = imregtform(movingRg,fixedRg,type,optimizer,metric);
handles.regStatus.String = ['Applying ' type ' Transformation'];pause(0.1)
for i = 1:numel(handles.I2)
    handles.I2{i} = imwarp(handles.I2{i},tform,'OutputView',imref2d(size(fixedRg)));
end

handles.regStatus.String = 'Done with Registration';pause(0.1)

end