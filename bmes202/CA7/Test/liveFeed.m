function liveFeed
%% DESCRIPTION ('Master' Function)
%    This function creates the GUI environmet for the program to run in. It
%    provides buttons for the user to interact with the program.
%    The 'Start Capture' button triggers the @startCapture button when
%    clicked.
%    The 'Stop Capture' button triggers the @stopCapture button when
%    clicked.
%  INPUT: None
%  OUTPUT: None
%  ------------------------------------------------------------------------
%  Authors: Tony Kabilan Okeke
%           Vrigav Narra
%           Ankit Patel
%           Deep Patel
%  Date: 12/01/2020
 
%% Create Window For Live Feed
   % This window will contain the live image feed from the camera. It will
   % provide the user with two buttons to start and stop capturing video.
	 % When Video Capture is started the @startCapture callback function is
	 % triggered.
	 % When Video Capture is stopped the @stopCapture callback function is
	 % triggered.

   %--- create figure handle
   GUI.fh = figure(1);
	 clf(GUI.fh)
	 GUI.fh.WindowState = 'maximized';
	 GUI.fh.Tag = 'liveFeed';
	 GUI.fh.Name = 'Live Feed';
	 
	 %--- create 'start capture' ('begin') button handle
	 GUI.bh = uicontrol('String','Start Capture',... 
											'Units','normalized',...
											'Position',[0.03 0.03 0.1 0.05],...
											'Callback',{@startCapture},...
											'BackgroundColor','#77AC30',...
											'FontSize',14); 
										
   %--- create 'stop capture' ('end') button handle
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