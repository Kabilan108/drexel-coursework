function [dt_pos, S_obj] = ca6_fun3(imBW_in)
%% DESCRIPTION (Analyze Objects_
%    This function analzes objects in the BW filtered image and returns the
%    position of the objects and a struture for object analysis.
%  INPUT
%    imBW_in -> [MxNx1] array containig 'final' logical image (size filtered)
%  OUTPUT
%    dt_pos -> [1x2] vector containing x,y position of object
%    S_obj  -> Structure containing results for object analysis
%  ------------------------------------------------------------------------
%  Author: Tony Kabilan Okeke
%          Jessica Baggett
%          Vrigav Narra
%          Jackie Tang
%  Team: B02
%  Date: 11/10/2020

%% Remove White Frame Around Image
   BW_hva = bwareafilt( imBW_in , [200 10000] );

%% Visualize labeled objects
   fig = figure(5);
	 clf(fig)
	 imL = bwlabel(BW_hva);
	 imshow(imL)
	 title('Labeled Objects')
	
%% Determine Centroid Position
   S_obj = regionprops(imL);
	 dt_pos = S_obj.Centroid;

%% Provide Formatted Output
   fprintf('<strong>Centroid Position: </strong>')
	 fprintf('( %.2f \t %.2f )\n',dt_pos)
end