function dt_out = ca6_fun4
%% DESCRIPTION
%    This function plots the position of green objects against tje position
%    of red objects across all images (frames) in the directory.
%  INPUT
%    None
%  OUTPUT
%    dt_out -> [Mx6] matrix containing position data
%     (:,1) -> Frame Number
%     (:,2) -> Green-to-Red distance
%     (:,3) -> X-Position [Green]
%     (:,4) -> Y-Position [Green]
%     (:,5) -> X-Position [Red]
%     (:,6) -> Y-Position [Red]
%  ------------------------------------------------------------------------
%  Author: Tony Kabilan Okeke
%          Jessica Baggett
%          Vrigav Narra
%          Jackie Tang
%  Team: B02
%  Date: 11/10/2020

%% Get Image File Name, use previously selected file name as default
   % Assuming the previously selected file name is stored in 
	 % the 'FileName' handle of the figure tagged 'Original Object'
	 defname = get( findobj('Tag','Original Image'), 'FileName' );
	 if ~isempty(defname)
		 [~,fnm,ext] = fileparts(defname);
		 defname = [fnm ext];
	 end
	 % Prompt User to Select Image File, file name from fig 1 handle is 
	 % default input.
	 [~, pth] = uigetfile('*.jpg','Please Select Image File',defname);
	 
%% Get all Images in Directory
   % Find all  inmages in the user-selected path
   S_dir = dir(pth);
	 
	 % Remove Directory Listings from S_dir
	 dirs = ([S_dir.isdir] == 1 );
	 S_dir( dirs ) = [];
	 
%% Loop Through All Images in Directory
   % Preallocate loop number (Frame #)
	 n_loop = zeros(1, length( S_dir ) );
	 
	 % Preallocate Position Vectors, p_grn & p_red
	 % -> [Nx2] matrices containing centroid positions of green & red objects 
	 % -> Col 1 = x pos; Col 2 = y pos 
	 p_grn = zeros(length( S_dir ),2);
	 p_red = zeros(length( S_dir ),2);
	 
   for i = 1:length( S_dir )
		 % Get Name of Current File
		 img_file = [pth S_dir(i).name];
		 
		 % Read File & Convert Image
		 [imHSV, ~, ~] = ca6_fun1(img_file);
		 
		 % Filter Green Objects From Converted Image
		 grn_filter = [0.25,0.42;0.5,1;10,1000];
		 [BW_hva, ~] = ca6_fun2(imHSV,grn_filter);
		 
		 % Get Positions for green objects
		 [p_grn(i,[1 2]), ~] = ca6_fun3(BW_hva);
		 
		 % Filter Red Objects From COnverted Image
		 red_filter = [0.95,0.05;0.5,1.1;20,1000];
		 [BW_hva, ~] = ca6_fun2(imHSV,red_filter);
		 
		 % Get Positions for red objects
		 [p_red(i,[1 2]), ~] = ca6_fun3(BW_hva);
		 
		 % Store Loop Number (Frame #)
		 n_loop(i) = i;
	 end
	 
%% Plot Positions of Green & Red Objects
   fig = figure(6);
	 clf(fig)
	 hold on
	 %Plot Settings
	 ax = gca;
	 ax.XGrid = 'on';
	 ax.YGrid = 'on';
	 ax.XMinorGrid = 'on';
	 ax.YMinorGrid = 'on';
	 xlabel('X-Position (px)')
	 ylabel('Y-Position (px)')
	 title('Positions of Immuno Cells & Cancer Cells')
	 subtitle('(Green & Red Objects, Respectively)')
	 %Plot Positions of Green Objects (Immuno Cells)
	 plot(p_grn(:,1),p_grn(:,2),'o','Color','#77AC30','MarkerFaceColor','#77AC30')
	 %Plot Red Positions
	 plot(p_red(:,1),p_red(:,2),'o','Color','#A2142F','MarkerFaceColor','#A2142F')
	 %Make Axes equal
	 axis equal
	 %Add legend
	 legend('Immuno Cell','Cancer Cell','Location','southeast')
	 hold off
	 
%% Plot Green-to-Red (gtr) distance
   % Calculate Distance between green and red objects (applying the formula
   % for distance between 2 points to matrices)
	 % AB = sqrt( (Xb-Xa)^2 + (Yb-Ya)^2 )
	 gtr = sqrt( sum( (p_grn - p_red).^2 , 2 ) );
	 %---- find square of difference b/w corresponding x&y coords, sum
	 %---- them along dimension 2 (i.e. add columns), and take square root
	 
	 %% Plot green-to-red distance against frames(measure of time)
	 fig = figure(7);
	 clf(fig)
	 hold on
	 %Plot Settings
	 ax = gca;
	 ax.XGrid = 'on';
	 ax.YGrid = 'on';
	 ax.XMinorGrid = 'on';
	 ax.YMinorGrid = 'on';
	 xlabel('Frame')
	 ylabel('Separation (px)')
	 title('Distance between Immuno & Cancer Cells')
	 subtitle('(Green-to-Red Distance)')
	 xticks( 1:numel(n_loop) )
	 %Plot Data
	 plot(n_loop,gtr,'-o','Color','#7E2F8E','LineWidth',2)
	 hold off
	 
%% Create Output Matrix
   dt_out = [n_loop' gtr p_grn p_red];
	 
end