function [x,y] = dotFilter(imRGB,dotColor)
%% DESCRIPTION
%    This function uses HVA filtering to detect the dot in the image
%    provided. It returns the centroid position of the dot.
%  INPUT
%    imRGB -> [MxNx3] array containing image RGB data
%    dotColor -> [1xN] string containing color to search for
%  OUTPUT
%    x -> x-position of dot centroid
%    y -> x-position of dot centroid
%  ------------------------------------------------------------------------
%  Author: Tony Kabilan Okeke
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
		 
		 % Create Menu
		 hTtl = uicontrol('Style','text','String','SELECT DOT COLOR',...
                      'Units','normalized','Position',[.1 .78 .8 .2],...
											'FontSize',14,'FontWeight','bold');
		 hRed = uicontrol('Style','pushbutton','String','Red',...
											'Units','normalized','Position',[.1 0.67 .8 .18],...
											'BackgroundColor','#A2142F','Callback',@btnRed,...
											'FontSize',25);
		 hGrn = uicontrol('Style','pushbutton','String','Green',...
											'Units','normalized','Position',[.1 .45 .8 .18],...
											'BackgroundColor','#77AC30','Callback',@btnGrn,...
											'FontSize',25);
		 hBlu = uicontrol('Style','pushbutton','String','Blue',...
											'Units','normalized','Position',[.1 .23 .8 .18],...
											'BackgroundColor','#0072BD','Callback',@btnBlu,...
											'FontSize',25);
		 hYel = uicontrol('Style','pushbutton','String','Yellow',...
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
	 BWv = ( imHSV(:,:,3) > 0.50 ) & ( imHSV(:,:,3) < 1.00 );
	 
	 % Combine HSV filters
	 BW = BWh & BWs & BWv;
	 
	 % Size Filter
	 sthr = round( pi/4 * [10 50].^2 );
	 BW = bwareafilt(BW,sthr);
	 
%% Determine Centroid of Object
   S = regionprops( BW );
	 
	 if ~isempty(S)
		 for i = 1:length(S)
			 x(i) = S(i).Centroid(1);
			 y(i) = S(i).Centroid(2);
		 end
	 else
		 x = NaN; y = NaN;
	 end
end

%% Define Callback Functions
function btnRed(~,~)
  assignin('caller','dotColor','red');
	close( findobj('Tag','Menu') );
end
function btnGrn(~,~)
  assignin('caller','dotColor','green');
	close( findobj('Tag','Menu') );
end
function btnBlu(~,~)
  assignin('caller','dotColor','blue');
	close( findobj('Tag','Menu') );
end
function btnYel(~,~)
  assignin('caller','dotColor','yellow');
	close( findobj('Tag','Menu') );
end