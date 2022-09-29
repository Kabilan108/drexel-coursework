function startCapture(~,~)
%% DESCRIPTION
%    This function serves as the callback for the 'Start Capture' button in
%    the liveFeed figure.
%    It creates displays a live feed from the camera, uses H-V-A filtering
%    to locate the centroid of the 'marker' object, which - by default - is
%    a red dot (done by @dotFilter function).
%    The determined centroid is then overlayed onto the live feed.
%  INPUT: None
%  OUTPUT: OUTPUT
%  ------------------------------------------------------------------------
%  Author: Tony Kabilan Okeke
%  Date: 11/24/2020

%% Initialize Webcam Connection
   %---> this section needs work
	 cm = struct('Interpreter','tex','WindowStyle','modal');
	 uiwait( msgbox('\fontsize{13}Please Select a Webcam.','icon','warn',cm) )
	 if length(webcamlist) > 1
		 list = webcamlist;
		 prmt = {'Choose a Webcam.','Only One Webcam can be Chosen at a Time.',''};
		 [indx,tf] = listdlg('PromptString',prmt,'ListString',list,...
			           'SelectionMode','single','OKString','Start Capture',...
								 'ListSize',[200 100]);
		 if tf
			 cam = webcam( list{indx} );
		 else
			 myHandle = guidata( gcbo );
			 myHandle.stopCapture = true;
			 guidata( gcbo , myHandle );
			 cam = webcam;
		 end
	 else
		 cam = webcam;
	 end
	 
%% Display Live Image Feed
   while true
		 %% Retreive Snapshot (frame) & visualize it
		 I = snapshot(cam);
		 GUI.fh = gcbo;
		 imshow(I,'Parent',GUI.fh.Parent.CurrentAxes)
		 
		 %% Filter image to locate centroid of red dot
		 [x,y] = dotFilter(I,'red');
		 
		 %% Overlay Centroid onto Live Feed
		 if ~isnan(x)
			 hold(GUI.fh.Parent.CurrentAxes,'on')
			 plot(GUI.fh.Parent.CurrentAxes,x,y,'ro','LineWidth',1.5)
			 hold(GUI.fh.Parent.CurrentAxes,'off')
		 end
		 
		 %% Loop Exit Conditions
		 % Extract data stored in liveFeed uifigure
		 myHandle = guidata( gcbo );
		 
		 if myHandle.stopCapture
			 % Reset myHandle.stopCapture value so buttons still work
			 myHandle.stopCapture = false;
			 guidata( gcbo , myHandle );
			 
			 % Display Wait Image
			 waitImg = 'Images/Wait.jpg';
			 if exist(waitImg,'file')
				 imshow(waitImg,'Parent',GUI.fh.Parent.CurrentAxes)
			 end
			 
			 % Stop Capture
			 clear cam
			 
			 % Exit loop
			 break;
			 
		 end
	 end
end