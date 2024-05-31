function xoverKids = rnafoldga_crossover(parents, options, nvars, FitnessFcn,unused,thisPopulation)
% by AhmetSacan

xoverKids = zeros(numel(parents)/2,nvars);

for pi=1:2:numel(parents)
	p1=parents(pi);
	p2=parents(pi+1);
	v1 = thisPopulation(p1,:);
	v2 = thisPopulation(p2,:);
	%perform a single-point cross-over at a coordinate boundary (ie., don't
	%split <x,y,z> coordinates of a nucleotide.
	at = randi(numel(v1)/3-1)*3;
	c1 = [v1(1:at) v2(at+1:end)];
	c2 = [v2(1:at) v1(at+1:end)];
	if FitnessFcn(c1) < FitnessFcn(c2); c=c1;
	else c=c2; end
	xoverKids(ceil(pi/2),:)=c;
end

