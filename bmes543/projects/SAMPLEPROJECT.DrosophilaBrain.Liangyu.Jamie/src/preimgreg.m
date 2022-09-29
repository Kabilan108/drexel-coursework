function [handles] = preimgreg(handles)
[currI1,currI2,~,vertices,~] = applyRegOpts(handles);

axes(handles.fig1axes);
if isfield(handles,'I1')
    imshow(currI1);
end
handles.fig1axes.Visible='On';hold on
plot([vertices(:,1); vertices(1,1)],[vertices(:,2); vertices(1,2)],'r','Linewidth',2);
hold off

axes(handles.fig2axes);
if isfield(handles,'I1')
    imshow(currI2);
end
handles.fig2axes.Visible='On';hold on
plot([vertices(:,1); vertices(1,1)],[vertices(:,2); vertices(1,2)],'r','Linewidth',2);
hold off

end