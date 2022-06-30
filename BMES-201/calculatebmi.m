function [bmi] = calculatebmi(h,w)
    % Takes two inputs, h (height), and w (weight) and returns the bmi
		% by Tony Kabilan Okeke - 20190927
    bmi = (w*4.88)/(h^2);
end