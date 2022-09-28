function avg = avgPain(file)
   [~,~,raw] = xlsread(file);
	 fields = raw(1,:);
	 data = raw(2:end,:);
	 genCol = strcmpi(fields,'gender');
	 painCol = strcmpi(fields,'pain');
	 avg = mean([data{ ([ data{:,genCol} ] == 'F'), painCol }]);
end