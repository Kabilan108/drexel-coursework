function stopCapture(~,~)
%% DESCRIPTION
%    This function serves as the callback for the 'Stop Capture' Button in
%    the liveFeed Figure
%    This function serves as the callback for the 'Stop Capture' button in
%    the liveFeed figure. It changes the value of myHandle.stopCapture to
%    true, to break out of the while loop in startCapture.
%  INPUT: None
%  OUTPUT: None
%  ------------------------------------------------------------------------
%  Authors: Tony Kabilan Okeke
%           Vrigav Narra
%           Ankit Patel
%           Deep Patel
%  Date: 12/01/2020

%% Callback Operations
	 % Retrieve Information Stored In The liveFeed Figure
	 myHandle = guidata( gcbo );
		
	 % Set Boolean Trigger As true
	 myHandle.stopCapture = true;
		
	 % Save Structure In liveFeed Figure
	 guidata( gcbo , myHandle );
end