%% Button Triggers
function buttonTriggers
    GUI.fh = figure;
    
    GUI.h1 = uicontrol('style','Edit',...
                   'string','XX',...
                   'Units','normalized',...
                   'Position',[0.1 0.1 0.8 0.2],...
                   'backgroundcolor','c',...
                   'Tag','EditField2',...
                   'Enable','off');
    
    GUI.h2 = uicontrol('Style','PushButton',...
                   'String','Start',...
                   'Units','normalized',...
                   'Position',[0.1 0.4 0.3 0.2],...
                   'callback',{@func_compute},...
                   'Tag','StartButton',...
                   'backgroundcolor',...
                   'g','FontSize',12);
                   
    GUI.h3 = uicontrol('Style','PushButton',...
                   'String','Stop',...
                   'Units','normalized',...
                   'Position',[0.5 0.4 0.3 0.2],...
                   'callback',{@breakOP},...
                   'Tag','StopButton',...
                   'backgroundcolor',...
                   'r','FontSize',12);
    
    myHandle = guihandles(GUI.fh);  % save gui handles to struct
    myHandle.breakOP = false;       % flag for break OP
    guidata(GUI.fh,myHandle);       % save structure
end
function func_compute(~,~)
    
    a = 1;
    while 1
        myHandle = guidata(gcbo);                   % get structure
        myHandle.EditField2.String = num2str(a);    % edit field string
        pause(0.01);
        if myHandle.breakOP                         % check for break OP flag
            break;
        end
        a = a +1;
    end
   
end
function breakOP(~,~)
    myHandle = guidata(gcbo);   % get structure
    myHandle.breakOP = true;    % change break OP flag
    guidata(gcbo,myHandle);     % save structure
end


%% BUTTON TEST
% Clear Workspace  Command Window
clear
clc

% Create Figure
GUI.fh = figure;
GUI.bh = uicontrol('String','Stop Video','Callback',@stopVideo,'Value',true);

% Save gui handles
myHandle = guihandles(GUI.fh);
myHandle.stopVideo = false;
guidata(GUI.fh,myHandle)

% Initialize Web am
cam = webcam;

% Loop

while true
	I = snapshot(cam);
	imshow(I)
	hold on
	plot(mean(xlim),mean(ylim),'ok')
	hold off
	
	myHandle = guidata(GUI.bh);
	if myHandle.stopVideo
		break;
	end
end

clear cam

function stopVideo(~,~)
  myHandle = guidata(gcbo);
	myHandle.stopVideo = true;
	guidata(gcbo,myHandle);
end


%% CAM VIEWER
clear
cam = webcam;
figure;
c = uicontrol;

for i = 1:50
	I = snapshot(cam);
	h = rgb2hsv(I);
	h = h(:,:,3);
	imshow(h)
	colormap copper
	hold on
	plot(mean(xlim),mean(ylim),'ok')
	hold off
end


%% FILT
clc
clear

[imRGB,imHue,imSat,imVal] = imview;

BWh = (imHue > 0.95) | (imHue < 0.05);
BWv = (imVal > 0.50) & (imVal < 1.00);
BWs = (imSat > 0.50) & (imSat < 1.00);
BWhvs = BWh & BWv & BWs;

sthr = round( pi/4 * [10 50].^2 );
BWhvsa = bwareafilt(BWhvs,sthr);


figure(5)
clf

nexttile
imshow(BWh)
title('BWh')

nexttile
imshow(BWv)
title('BWv')

nexttile
imshow(BWs)
title('BWs')

nexttile
imshow(BWhvs)
title('BWhvs')

nexttile
imshow(BWhvsa)
title('BWhvsa')

S = regionprops(BWhvsa);

figure(1)
hold on
x = S.Centroid(1);
y = S.Centroid(2);
plot(x,y,'oy','LineWidth',1.5)