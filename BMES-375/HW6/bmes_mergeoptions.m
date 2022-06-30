function opt=bmes_mergeoptions(opt, varargin)


%% convert any options from varargin into the opt structure.
i = 0;
while i<numel(varargin)
	i=i+1;
	next = varargin{i};
	if ischar(next)		
		name=varargin{i};
		value=varargin{i+1};
		i=i+1;
		opt.(name)=value;
	elseif isstruct(next)
		fields = fieldnames(next);
		for fi = 1:numel(fields)
			name = fields{fi};
			opt.(name) = next.(name);
		end
	else
		error('Unsupported argument type. Expecting field name or struct');
	end
end
