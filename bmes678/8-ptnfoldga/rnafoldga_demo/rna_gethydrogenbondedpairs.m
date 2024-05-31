function pairs=rna_gethydrogenbondedpairs(seq,locs,dist)
% Takes a distance matrix (inter-nucleotide distances) and identifies pairs
% of nucleotides that are hydrogen-bonded.
% Assumptions/Requirements:  (Some of these assumptions may not be
% physically/chemically correct).
% * Hydrogen bonds are only between A-U, A-T, and G-C pairs.
% * Nucleotides that are between 5-25 Angstroms are considered
% hydrogen-bonded.
% * There needs to be at least 4 residues between hydrogen-bonding
% partners; e.g,. 1st nucleotide cannot form H-bond with nucleotides 2-5, but can
% form H-bond with nucleotide 6+.
% * A nucleotide can form H-bond with at most one other nucleotide.
% (monogamy). If multiple partners satisfy the distance requirements, use
% the one with the smallest distance as H-bonding partner.
% * We follow a greedy matching strategy to pair up the closest eligible
% partners at each step.
% by Ahmet.

MINSEQDIST = 4; % need to be at least this far apart on the sequence.
MINDIST = 5;    % need to be at least this far apart in distance.
MAXDIST = 25;   % need to be at most this far apart in distance.

if ~exist('dist','var')
	if size(locs,1)==1;	locs = reshape(locs,3,[])'; end
	dist=squareform(pdist(locs));
end

% we mark ineligible ones by setting their distance to infinite.
dist(tril(true(size(dist)))) = inf; % we only use the Upper Triangle of this matrix.
dist(dist<MINDIST) = inf;
dist(dist>MAXDIST) = inf;

seq=upper(seq);
for i=1:numel(seq)
	for j=i+1:numel(seq)
		if ~isinf(dist(i,j)) && ~any(strcmp({'AU','UA','AT','TA','CG','GC'}, seq([i j]))); dist(i,j)=inf; end
	end
end

%mark nucleotides that are less than MINSEQDIST-apart as ineligible.
for i=1:size(dist,1)
	dist(i, i:min(i+MINSEQDIST,end)) = inf;
	 % no need to turn off i-MINSEQDIST:i or do this symmetrically, because the eligibles is set up as an upper-triangle-only matrix.
end

pairs = zeros(0,2);
while ~all(isinf(dist),'all')
	% [~,ind]=min(dist,[],'all');
	% [r,c]=ind2sub(size(dist),ind);

    mindist=min(dist,[],'all');
    [r,c]=find(dist==mindist);
    rc=sortrows([r,c]);
    r=rc(1,1); c=rc(1,2);

    if size(rc, 1) > 1
        fprintf('multiple values\n')
        break
    end
    if size(rc, 2) ~= 2
        fprintf('idk\n')
        break
    end

	pairs(end+1,:)=[r,c];
	dist(r,:)=inf;
	dist(c,:)=inf;
	dist(:,r)=inf;
	dist(:,c)=inf;
end
pairs=sortrows(pairs);

	