function x = zerosamesize(m)
   % Create a zero matrix equal in dimension to the input matrix
	 % By Tony Kabilan Okeke - 20191110
	 [rows,cols] = size(m);
	 x = zeros(rows,cols);
end

% Alternatively, m(1:end)=0 , or m(:,:) = 0 , or m(1:end,1:end) = 0, or...
% m(1:R,1:C) = 0