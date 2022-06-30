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

   %--- figure handle
   GUI.fh = figure(1);
	 clf(GUI.fh)
	 GUI.fh.WindowState = 'maximized';
	 GUI.fh.Tag = 'liveFeed';
	 GUI.fh.Name = 'Live Feed';
	 
	 %--- 'start capture' ('begin') button handle
	 GUI.bh = uicontrol('String','Start Capture',... 
											'Units','normalized',...
											'Position',[0.03 0.03 0.1 0.05],...
											'Callback',{@startCapture},...
											'BackgroundColor','#77AC30',...
											'FontSize',14); 
										
   %--- 'stop capture' ('end') button handle
	 GUI.eh = uicontrol('String','Stop Capture',...
											'Units','normalized',...
											'Position',[0.87 0.03 0.1 0.05],...
											'Callback',{@stopCapture},...
											'BackgroundColor','#A2142F',...
											'FontSize',14);
		
   % Save GUI Handles to struct, create boolean trigger for @stopCapture,
   % and save structure in figure
	 myHandle = guihandles( GUI.fh );
	 myHandle.stopCapture = false;
	 guidata( GUI.fh , myHandle );
	 
	 % Display Wait Image
	 waitImg = 'Images/Wait.jpg';
	 if exist(waitImg,'file')
		 imshow(waitImg)
	 end
end