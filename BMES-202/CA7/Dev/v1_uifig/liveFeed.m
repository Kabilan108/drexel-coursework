function liveFeed
%% DESCRIPTION
%    This function initializes MATLAB's connection to thhe system's camera,
%    and provides the user with a toggle-able live video feed. The function
%    then locates the red dot (laser point) (@filter) in the video feed, 
%    and overlays the position of its centroid onto the live feed.
%  INPUT
%    None.
%  OUTPUT
%    None.
%    Saves Video File
%  ------------------------------------------------------------------------
%  Author: Tony Kabilan Okeke
%  Date: 11/24/2020
 
%% Create Window For Live Feed
   % This window will contain the live image feed from the camera. It will
   % provide the user with two buttons to start and stop capturing video.
	 % When Video Capture is started the @startCapture callback function is
	 % triggered.
	 % When Video Capture is stopped the @stopCapture callback function is
	 % triggered.
	 
	 %--- close previous iterations
	 close(findall(0,'type','figure','Name','Live Feed'))

   %--- figure handle
	 GUI.fh = uifigure;
	 GUI.fh.WindowState = 'maximized';
	 GUI.fh.Tag = 'liveFeed';
	 GUI.fh.Name = 'Live Feed';
	 
	 %--- axis handle
	 GUI.ax = uiaxes(GUI.fh,'Position',[330 200 1280 720],'Visible','off');
	 
 	 %--- 'start capture' ('begin') button handle
	 GUI.bh = uibutton(GUI.fh,'Text','Start Capture','FontSize',20,...
		                 'Position',[50 50 200 40],'BackgroundColor','#77AC30',...
										 'ButtonPushedFcn',@(btn,event) startCapture(btn,event));
   GUI.bh = uibutton(GUI.fh,'Text','Stop Capture','FontSize',20,...
		                 'Position',[1650 50 200 40],'BackgroundColor','#A2142F',...
										 'ButtonPushedFcn',@(btn,event) stopCapture(btn,event));
									 
	 % Display Wait Image
 	 waitImg = 'Images/Wait.jpg';
 	 if exist(waitImg,'file')
		 imshow(waitImg,'Parent',GUI.ax)
 	 end
									 
   % Save GUI Handles to struct, create boolean trigger for @stopCapture,
   % and save structure in figure
	 myHandle = guihandles( GUI.fh );
	 myHandle.stopCapture = false;
	 guidata( GUI.fh , myHandle );
end