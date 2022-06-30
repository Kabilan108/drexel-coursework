function [out] = myisletter(l)
  %{
	Returns true if the input is a letter. If the input is any character
	other than a letter, or is not a character at all, it returns NaN without
	using the isletter function.
	
	By Tony Kabilan Okeke - 20191025
	%}
%{
	if ischar(l) 
		 if ( (l >= 'a' && l <= 'z') || (l >= 'A' && l <= 'Z') )
			 out = true;
		 else
			 out = nan;
		 end
	else 
		 out = nan;
	end
%}
out = zeros(1,numel(l));
%{
for i = 1:numel(l)
	out(i) = l(i) >= 'a' && l(i) <= 'z' || l(i) >= 'A' && l(i) <= 'Z';
end
%}
out = (l >= 'a' & l <= 'z' ) | ( l >= 'A' & l <= 'Z' ) ;
    
end