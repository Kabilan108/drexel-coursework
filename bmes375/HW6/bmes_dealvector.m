function varargout=bmes_dealvector(v)
% e.g.,
% v=[1 2 3]
% [a,b,c] = bmes_dealvector(v)


varargout=cell(1,numel(v));
for i=1:numel(v)
	varargout{i} = v(i);
end
