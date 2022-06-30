function data = loadGEO(geoID)
  % This function can be used to download GPL and GSE data from the Gene
  % Expression Omnibus (GEO)
  % INPUT: geoID - a GSM, GSE, or GPL number
  % OUTPUT: a GSM, GSE or GPL struct depending on geoID
  
  % Determine if valid data type is being requested
  if isempty(regexp(geoID, '^(GSM|GSE|GPL)', 'ONCE'))
		error('Invalid geoID. Please provide Valid Accession number.')
	end
	
	% Define temporary file
	file = fullfile(tempdir, [geoID '.txt']);
	
	% Check if file has already been downloaded to tempdir. If not, download
	% the data from geo.
	if isfile( fullfile(tempdir, [geoID '.txt']) )
		fprintf('Loading cached data...\n');
		if ~isempty(regexp(geoID, '^GPL', 'ONCE'))
			data = geosoftread( file );
		elseif ~isempty(regexp(geoID, '^GSE', 'ONCE')) 
			data = geoseriesread( file );
		end
		fprintf('Done!\n');
	else
		% Load data from geo and save to temporary file
		try
			fprintf('Retreiving %s from GEO...\n', geoID);
			data = getgeodata(geoID, 'ToFile', file);
			fprintf('Done!\n');
		catch
			error(['An error occured when retrieving data from GEO.'...
				'Please provide Valid Accession number and try again.']);
		end
	end
end