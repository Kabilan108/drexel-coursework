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
	 cam = webcam;
	 
	 fprintf('Start\n')
	 
%% Display Live Image Feed
   while true
		 %% Retreive Snapshot (frame) & visualize it
		 I = snapshot(cam);
		 imshow(I);
		 
		 %% Filter Image To Locate Centroid of Red Dot
		 [x,y] = dotFilter(I,'red');
		 
		 %% Overlay Centroid onto Live Feed
		 if ~isnan(x)
			 hold on
			 plot(x,y,'oy','LineWidth',1.5)
			 hold off
		 end
		 
		 %% Loop Exit Conditions
		 % Extract data stored in liveFeed figure
		 myHandle = guidata( gcbo );
		 
		 if myHandle.stopCapture
			 % Reset myHandle.stopCapture value so buttons still work
			 myHandle.stopCapture = false;
			 guidata( gcbo , myHandle );
			 
			 % Display Wait Image
			 waitImg = 'Images/Wait.jpg';
			 if exist(waitImg,'file')
				 imshow(waitImg)
			 end
			 
			 fprintf('Stop\n')
			 
			 clear cam
			 
			 % Exit Loop
			 break;
		 end
	 end
end