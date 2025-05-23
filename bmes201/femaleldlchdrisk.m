function [ risk ] = femaleldlchdrisk(data)
   % Takes data input as a struct array nd returns the risk points
	 % By Tony Kabilan Okeke - 20191130
   [ risk ] = zeros(1,numel( [ data.age ] ));
   
   % Loop based on the number of entries in each struct field
	 for i = 1:numel([ data.age ])
		 ldlPts = 0;
		 % Assigning Age points
		 if data(i).age < 35
			 ldlPts = ldlPts + -9;
		 elseif data(i).age < 39
			 ldlPts = ldlPts + -4;
		 elseif data(i).age < 45
			 ldlPts = ldlPts + 0;
		 elseif data(i).age < 50
			 ldlPts = ldlPts + 3;
		 elseif data(i).age < 55
			 ldlPts = ldlPts + 6;
		 elseif data(i).age < 60
			 ldlPts = ldlPts + 7;
		 else
			 ldlPts = ldlPts + 8;
		 end
		 
		 % Assigning ldl points
		 if data(i).ldl < 100
			 ldlPts = ldlPts + -2;
		 elseif data(i).ldl < 160
			 ldlPts = ldlPts + 0;
		 else
			 ldlPts = ldlPts + 2;
		 end
		 
		 % Assigning hdl points
		 if data(i).hdl < 35
			 ldlPts = ldlPts + 5;
		 elseif data(i).hdl < 45
			 ldlPts = ldlPts + 2;
		 elseif data(i).hdl < 50
			 ldlPts = ldlPts + 1;
		 elseif data(i).hdl < 60
			 ldlPts = ldlPts + 0;
		 else
			 ldlPts = ldlPts + -2;
		 end
		 
		 % Assigning blood pressure points
		 if data(i).diastolic < 80
			 if data(i).systolic < 120
				 ldlPts = ldlPts + -3;
			 elseif data(i).systolic < 140
				 ldlPts = ldlPts + 0;
			 elseif data(i).systolic < 160
				 ldlPts = ldlPts + 2;
			 else
				 ldlPts = ldlPts + 3;
			 end
		 elseif data(i).diastolic < 85
			 if data(i).systolic < 140
				 ldlPts = ldlPts + 0;
			 elseif data(i).systolic < 160
				 ldlPts = ldlPts + 2;
			 else
				 ldlPts = ldlPts + 3;
			 end
		 elseif data(i).diastolic < 90
			 if data(i).systolic < 140
				 ldlPts = ldlPts + 0;
			 elseif data(i).systolic < 160
				 ldlPts = ldlPts + 2;
			 else
				 ldlPts = ldlPts + 3;
			 end
		 elseif data(i).diastolic < 100
			 if data(i).systolic < 160
				 ldlPts = ldlPts + 2;
			 else
				 ldlPts = ldlPts + 3;
			 end
		 else
			 ldlPts = ldlPts + 3;
		 end
		 
		 % Assigning Diabetes points
		 if data(i).hasdiabetes
			 ldlPts = ldlPts + 4;
		 else
			 ldlPts = ldlPts + 0;
		 end
		 
		 % Assigning smoking points
		 if data(i).issmoker
			 ldlPts = ldlPts + 2;
		 else
			 ldlPts = ldlPts + 0;
		 end
		 
		 % Assigning CHD risk based on points
		 if ldlPts < -1
			 risk(i) = 1;
		 elseif ldlPts < 2
			 risk(i) = 2;
		 elseif ldlPts < 10 && ldlPts ~= 2
			 risk(i) = ldlPts;
		 elseif ldlPts > 16
			 risk(i) = 32;
		 else
			 switch ldlPts
				 case 2; risk(i) = 3;
				 case 10; risk(i) = 11;
				 case 11; risk(i) = 13;
				 case 12; risk(i) = 15;
				 case 13; risk(i) = 17;
				 case 14; risk(i) = 20;
				 case 15; risk(i) = 24;
				 case 16; risk(i) = 27;
			 end
		 end
	 end
end