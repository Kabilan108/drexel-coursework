%% Majo Garcia
% Function identifies whether LDL, HDL and Total Cholesterol are high,
% borderline high or normal.

% Cut off levels have been determined from Cleveland Clinic
% (https://my.clevelandclinic.org/health/articles/11920-cholesterol-numbers-what-do-they-mean)

% Based on the previous output, recommendations will be made to improve or
% maintain current cholesterol levels. 

%% Function
function [tot_chol_lvl, ldl_lvl, hdl_lvl, recom1, recom2, recom3]=recommendations(age, sex, tot_chol, ldl, hdl, diabetes)
%% Total Cholestrol 
% Determine if total cholesterol is high, borderline high or normal
% depending on age

 if age <= 19
	 if tot_chol >= 200
		 tot_chol_lvl = 'high';
	 elseif tot_chol <= 199 && tot_chol >= 170
		 tot_chol_lvl = 'borderline high';
	 else
		tot_chol_lvl = 'normal';
	 end
 else
	 if tot_chol >= 240
		 tot_chol_lvl = 'high';
	 elseif tot_chol <= 239 && tot_chol >= 200
		 tot_chol_lvl = 'borderline high';
	 else
		tot_chol_lvl = 'normal';
	 end
 end

%% LDL
% Determine if LDL cholesterol is high, borderline high or normal
% depending on age

if age <= 19
	 if ldl >= 130
		 ldl_lvl = 'high';
	 elseif ldl <= 129 && ldl >= 110
		 ldl_lvl = 'borderline high';
	 else
		ldl_lvl = 'normal';
	 end
 else
	 if ldl >= 160
		 ldl_lvl = 'high';
	 elseif ldl <= 159 && ldl >= 100
		 ldl_lvl = 'borderline high';
	 else
		ldl_lvl = 'normal';
	 end
end
 
%% HDL
% Determine if HDL cholesterol is high, borderline high or normal
% depending on age

if age <= 19
	 if hdl >= 45
		 hdl_lvl = 'normal';
	 else
		hdl_lvl = 'high';
	 end
else
	 if hdl >= 60
			 hdl_lvl = 'normal';
	 elseif strcmpi(sex,'female')
		 if hdl <= 59 && hdl >= 50
			 hdl_lvl = 'borderline high';
		 else
			 hdl_lvl = 'high';
		 end
	 else
		 if hdl <= 59 && hdl >= 40
			 hdl_lvl = 'borderline high';
		 else
			 hdl_lvl = 'high';
		 end
	 end
end
 
%% Recommendations
% Determine recommendations based on ldl, hdl and total cholesterol.
if strcmpi (tot_chol_lvl, 'normal') && strcmpi (ldl_lvl, 'normal') && strcmpi (hdl_lvl, 'normal')
	recom1 =('https://www.cdc.gov/cholesterol/prevention.htm');
	recom2 = ('https://www.hopkinsmedicine.org/health/conditions-and-diseases/high-cholesterol/high-cholesterol-prevention-treatment-and-research');
	recom3 = ('https://www.heartandstroke.ca/healthy-living/healthy-eating/healthy-eating-basics');
else
	if strcmpi(diabetes,'yes')
		recom1 = ('https://www.eatingwell.com/article/7964765/diabetes-friendly-meal-plan-for-high-cholesterol/#:~:text=Diabetes%2DFriendly%20Foods%20to%20Focus%20on%20for%20High%20Cholesterol&text=Beans%20and%20lentils,broccoli%2C%20cauliflower%20and%20Brussels%20sprouts');
		recom2 = ('https://www.healthline.com/nutrition/blood-sugar-and-cholesterol-friendly-foods">Recommendation 2</a>');
		recom3 = ('https://www.lencolab.com/publications/2021/6/how-to-lower-sugar-cholesterol-tips.html');
	else
		recom1 = ('https://www.mayoclinic.org/diseases-conditions/high-blood-cholesterol/in-depth/reduce-cholesterol/art-20045935');
		recom2 = ('https://www.mayoclinic.org/diseases-conditions/high-blood-cholesterol/in-depth/cholesterol/art-20045192');
		recom3 = ('https://www.health.harvard.edu/heart-health/11-foods-that-lower-cholesterol');
	end
end

