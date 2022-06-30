function stopCapture(~,~)
%% DESCRIPTION
%    This function serves as the callback for the 'Stop Capture' Button in
%    the liveFeed Figure
%  INPUT: None
%  OUTPUT: None
%  ------------------------------------------------------------------------
%  Author: Tony Kabilan Okeke
%  Date: 11/24/2020

%% Callback Operations
	 % Retrieve Information Stored In The liveFeed Figure
	 myHandle = guidata( gcbo );
		
	 % Set Boolean Trigger As true
	 myHandle.stopCapture = true;
		
	 % Save Structure In liveFeed Figure
	 guidata( gcbo , myHandle );
	 
	 fprintf('Button Clicked\n')
		
	 % Turn Off Camera  Connection by deleting the variable containing the
	 % webacm link in the workspace of @liveFeed
	 %evalin('caller','clear cam')
end