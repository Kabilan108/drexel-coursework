function startCapture(~,~)
%% DESCRIPTION
%    This function serves as the callback for the 'Start Capture' button in
%    the liveFeed figure.
%    It displays a live feed from the user's chosen camera, and uses
%    H-V-S-A (Hue, Value, Saturation & Area) filtering to locate the
%    centroid of the 'marker' object, which -by default- is a red dot (done
%    by @dotFilter function).
%    The centroid is overlayed onto the live feed.
%  INPUT: None
%  OUTPUT: None
%  ------------------------------------------------------------------------
%  Authors: Tony Kabilan Okeke
%           Vrigav Narra
%           Ankit Patel
%           Deep Patel
%  Date: 12/01/2020

%% Initialize Webcam Connection
   % Create message box to prompt user
	 cm = struct('Interpreter','tex','WindowStyle','modal'); %--- createMode
	 uiwait(msgbox('\fontsize{13}Please Select a Webcam.','icon','help',cm));
	 
	 % If there are multiple webcams, prompt the user to select one
	 if length( webcamlist ) > 1
		 list = webcamlist;
		 prmt = {'Choose a Webcam.','Only One Can Be Chosen At A Time.',''};
		 [indx,tf] = listdlg('PromptString',prmt,'ListString',list,...
			           'SelectionMode','single','OKString','Start Capture',...
								 'ListSize',[200 100]);
			
			% If the user made a selection, activate the camera				 
			if tf
				cam = webcam( list{indx} );
			else
				% If no selection was made, reset .stopCapture trigger, so the
				% program doesn't start without a selection
				%        gcbo -> retrieves handle of object whose callback is being
				%                exectued
				myHandle = guidata( gcbo );
				myHandle.stopCapture = true;
				guidata( gcbo , myHandle );
			end
	 else
		 % If only one webcam exists, turn it on
		 cam = webcam;
	 end
	 
%% Display Live Image Feed
   while true
		 %% Loop Exit Conditions
		 % Extract data stored in liveFeed figure
		 myHandle = guidata( gcbo );
		 
		 if myHandle.stopCapture
			 % Reset myHandle.stopCapture values so buttons still work
			 myHandle.stopCapture = false;
			 guidata( gcbo , myHandle );
			 
			 % Display Wait Image
			 waitImg = 'Images/Wait.jpg';
			 if exist(waitImg,'file')
				 imshow(waitImg)
			 end
			 
			 % Turn off Webcam if it exists
			 if exist('cam','var')
				 clear cam;
			 end
			 
			 % Exit Loop
			 break;
			 
		 else %--- If exit conditions not met, generate live feed
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
		 end %--- end of 'if' at line 55
	 end %--- end of 'while' at line 50
end %--- end of function