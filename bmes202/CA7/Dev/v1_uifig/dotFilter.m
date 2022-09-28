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
					 
	 %% If dot color was not providedPrompt User To Select Dot Color
	 if ~exist('dotColor','var')
		 hFig = uifigure;
		 hFig.Tag = 'Menu';
		 hFig.Position = [500 400 200 300];
		 h = guihandles(hFig);
		 h.dotColor = '';
		 guidata(hFig,h)
		
		 % Create Menu
		 uilabel(hFig,'Text','SELECT DOT COLOR','FontSize',16,...
			 'Position',[16 250 180 40],'FontWeight','bold');
		 
		 uibutton(hFig,'Text','Red','FontSize',20,...
			 'Position',[10 200 180 40],'BackgroundColor','#A2142F',...
			 'ButtonPushedFcn',@(btn,event) btnRed(btn,event));
		 
		 uibutton(hFig,'Text','Green','FontSize',20,...
			 'Position',[10 150 180 40],'BackgroundColor','#77AC30',...
			 'ButtonPushedFcn',@(btn,event) btnGrn(btn,event));
		 
		 uibutton(hFig,'Text','Blue','FontSize',20,...
			 'Position',[10 100 180 40],'BackgroundColor','#0072BD',...
			 'ButtonPushedFcn',@(btn,event) btnBlu(btn,event));
		 
		 uibutton(hFig,'Text','Yellow','FontSize',20,...
			 'Position',[10 50 180 40],'BackgroundColor','#EDB120',...
			 'ButtonPushedFcn',@(btn,event) btnYel(btn,event));
		 
		 % Pause function while waiting for user to select color
		 while true
			 h = guidata(hFig);
			 if ~isempty(h.dotColor)
				 dotColor = h.dotColor;
				 close(findall(0,'type','figure','Tag','Menu'));
				 break;
			 end
			 pause(1)
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
  h = guidata( gcbo);
	h.dotColor = 'red';
	guidata( gcbo , h );
end
function btnGrn(~,~)
  h = guidata( gcbo);
	h.dotColor = 'green';
	guidata( gcbo , h );
end
function btnBlu(~,~)
  h = guidata( gcbo);
	h.dotColor = 'blue';
	guidata( gcbo , h );
end
function btnYel(~,~)
  h = guidata( gcbo);
	h.dotColor = 'yellow';
	guidata( gcbo , h );
end