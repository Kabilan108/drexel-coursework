function opts = mergeoptions(opts, varargin)
  % This function converts any options from varargin into the options
  % structure object.
	i = 0; % Loop counter
	while i < numel(varargin)
		i = i+1; % increment counter
		next = varargin{i}; % next argument
		% Read name, value pairs
		if ischar(next)
			name = varargin{i};
			value = varargin{i+1};
			i = i+1;
			opts.(name) = value; % add pair to opts
		elseif isstruct(next)
			% If a structure of options is recieved
			fields = fieldnames(next);
			for fi = 1:numel(fields)
				name = fields{fi};
				opts.(name) = next.(name);
			end
		else
			error('Unsopported argument type. Expecting Name, Value pair or struct');
		end
	end
end