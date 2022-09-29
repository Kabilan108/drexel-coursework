function [x,y] = dotFilter(imRGB,dotColor)
%% DESCRIPTION
%    This function uses H-V-S-A (Hue,Value,Saturation & Area) filtering to 
%    detect the dot in the image provided. It returns the centroid position
%    of the dot.
%    NOTE:
%      During our testing, we found that H-V-A filtering was not sufficient
%      to filter our image reliably. As such, we expanded out filter to
%      include 'Saturation' which makes it easier to locate the desired
%      'marker' object.
%  INPUT
%    imRGB -> [MxNx3] array containing image RGB data
%    dotColor -> [1xN] string containing color to search for
%  OUTPUT
%    x -> x-position of dot centroid
%    y -> x-position of dot centroid
%  ------------------------------------------------------------------------
%  Authors: Tony Kabilan Okeke
%           Vrigav Narra
%           Ankit Patel
%           Deep Patel
%  Date: 11/24/2020

%% Input Checking
   % If image RGB data was not provided
	 if ~exist('imRGB','var')
		 [fnm,pth] = uigetfile('*.jpg','Please Choose Image File');
		 img = fullfile(pth,fnm);
		 imRGB = imread(img);
	 end
	 
	 % If dot color was not providedPrompt User To Select Dot Color
	 if ~exist('dotColor','var')
		 hFig = figure;
		 clf(hFig)
		 hFig.Tag = 'Menu';
		 hFig.Position = [500 500 200 400];
		 
		 % Create Menu buttons
		 uicontrol('Style','text','String','SELECT DOT COLOR',...
               'Units','normalized','Position',[.1 .78 .8 .2],...
			  			 'FontSize',14,'FontWeight','bold');
		 uicontrol('Style','pushbutton','String','Red',...
							 'Units','normalized','Position',[.1 0.67 .8 .18],...
							 'BackgroundColor','#A2142F','Callback',@btnRed,...
							 'FontSize',25);
		 uicontrol('Style','pushbutton','String','Green',...
							 'Units','normalized','Position',[.1 .45 .8 .18],...
							 'BackgroundColor','#77AC30','Callback',@btnGrn,...
							 'FontSize',25);
		 uicontrol('Style','pushbutton','String','Blue',...
							 'Units','normalized','Position',[.1 .23 .8 .18],...
							 'BackgroundColor','#0072BD','Callback',@btnBlu,...
							 'FontSize',25);
		 uicontrol('Style','pushbutton','String','Yellow',...
							 'Units','normalized','Position',[.1 .01 .8 .18],...
							 'BackgroundColor','#EDB120','Callback',@btnYel,...
							 'FontSize',25);
		 
		 % Pause function while waiting for user to select color
		 while ~exist('dotColor','var')
			 pause(1);
		 end
	 end
	 
%% Filter Image
   % Extract hue, saturation and value data
	 imHSV = rgb2hsv(imRGB);
   
   % Hue Filter
   switch dotColor
		 case 'red'
			 BWh = ( imHSV(:,:,1) > 0.95 ) | ( imHSV(:,:,1) < 0.05 );
		 case 'green'
			 BWh = ( imHSV(:,:,1) > 0.25 ) & ( imHSV(:,:,1) < 0.40 );
		 case 'blue'
			 BWh = ( imHSV(:,:,1) > 0.60 ) & ( imHSV(:,:,1) < 0.70 );
		 case 'yellow'
			 BWh = ( imHSV(:,:,1) > 0.15 ) & ( imHSV(:,:,1) < 0.19 );
	 end
	 
	 % Saturation Filter
	 BWs = ( imHSV(:,:,2) > 0.50 ) & ( imHSV(:,:,2) < 1.00 );
	 
	 % Value Filter
	 BWv = ( imHSV(:,:,3) > 0.50 ) & ( imHSV(:,:,3) < 1.10 );
	 
	 % Combine HVS filters
	 BW = BWh & BWv & BWs;
	 
	 % HSVA (Size) Filter
	 sthr = round( pi/4 * [10 50].^2 );
	 BW = bwareafilt(BW,sthr);
	 
%% Determine Centroid of Object
   S = regionprops( BW ); %--- logical image used instead of labeled image 
	                        %--- to improve speed
	 % Preallocate x & y for speed
	 x = zeros( length(S) , 1 );
	 y = zeros( length(S) , 1 );
	 
	 if ~isempty(S)
		 % if objects were found, extract values into x & y
		 for i = 1:length(S)
			 x(i) = S(i).Centroid(1);
			 y(i) = S(i).Centroid(2);
		 end
	 else
		 % if no objects were found, set x & y to NaN
		 x = NaN; y = NaN;
	 end
end

%% Define Button Callback Functions
function btnRed(~,~)
  % create dotColor variable in the workspace of the 'caller' function
  assignin('caller','dotColor','red');
	% close menu
	close( findobj('Tag','Menu') );
end
function btnGrn(~,~)
  % create dotColor variable in the workspace of the 'caller' function
  assignin('caller','dotColor','green');
	% close menu
	close( findobj('Tag','Menu') );
end
function btnBlu(~,~)
  % create dotColor variable in the workspace of the 'caller' function
  assignin('caller','dotColor','blue');
	% close menu
	close( findobj('Tag','Menu') );
end
function btnYel(~,~)
  % create dotColor variable in the workspace of the 'caller' function
  assignin('caller','dotColor','yellow');
	% close menu
	close( findobj('Tag','Menu') );
end