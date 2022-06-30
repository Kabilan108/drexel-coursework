%%October 23rd
%{
x = 1:4; y = 1:4;
[x,y] = meshgrid(x,y);
I = ((x.^2) + y) == (3*x);
combs = [x(I),y(I)]
%% B
x = 5; y=7;
if x<10
	if y>10; y=40;
	elseif true; x=20; end
elseif x==5
	y=5;end
disp( sum([x y]) )
...


function out = scratch( a, b, c, varargin )
out = c + nargin + numel(varargin) + varargin{2};
%}
function [ varargout ] = scratch()
   varargout{1} = 'anna';
	 varargout{2} = 'betty';
	 varargout
end