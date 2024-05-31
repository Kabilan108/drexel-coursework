function [fitness,info]=rna_fitness(seq, locs)
% Given an RNA sequence (composed of ACGU characters) and locations of
% these nucleotides, return a fitness score.
% locations can be given as a 3-column matrix of <x,y,z> coordinates or a
% row-vector of all these <x,y,z> coordinates.
% by AhmetSacan.

% if a row-vector is given, convert to a 3-column format.
if size(locs,1)==1;	locs=reshape(locs,3,[])'; end

N=numel(seq);
distmat=squareform(pdist(locs));

% Calculate total hydrogen bonds
seq=upper(seq);
pairs = rna_gethydrogenbondedpairs( seq, [], distmat );
totalhbonds=0;
for i=1:size(pairs,1)
	%A-U and A-T form 2-hydrogen bonds; G-C form 3-hydrogen bonds.
	if ismember(seq(pairs(i,:)),{'AU','UA','AT','TA'}); totalhbonds=totalhbonds+2;
	elseif ismember(seq(pairs(i,:)),{'GC','CG'}); totalhbonds=totalhbonds+3; end
end

% Consecutive residues should be between 4-10 Angstroms
MINSEQDIST = 4;
MAXSEQDIST = 10;

seqdist = distmat(N+1:N+1:end); %distances between consecutive residues.
%We could just count the number of violations:
%seqviolations = nnz( seqdist<MINSEQDIST | seqdist>MAXSEQDIST );
%Or, to obtain a more continuous fitness value, incorporate the distance
%into the fitness calculation.
seqviolations = 0;
Iminviol= seqdist<MINSEQDIST;
seqviolations = seqviolations + sum(MINSEQDIST-seqdist(Iminviol));
Imaxviol= seqdist>MAXSEQDIST;
seqviolations = seqviolations + sum(seqdist(Imaxviol)-MAXSEQDIST);

% Non-consecutive residues should be farther than 4 Angstroms
MINNONSEQDIST = 4;
Inonseq = triu(true(size(distmat))); Inonseq(1:N+1:end)=false; Inonseq(N+1:N+1:end)=false;
nonseqdists = distmat(Inonseq);
%We could just count the number of violations:
%nonseqviolations = nnz(nonseqdists<MINNONSEQDIST);
%Or better, incorporate the distance into the fitness value.
Inonseqviol=nonseqdists<MINNONSEQDIST;
nonseqviolations = sum(MINNONSEQDIST-nonseqdists(Inonseqviol));


%{
% If we use discrete count of violations, we can also ensure that fitness
remains positive.
% There can be no more than (N/2) pairs --> no more than (N/2)*3 hydrogen
% bonds.
fitness = totalhbonds - (seqviolations+nonseqviolations) * (N/2)*3;
%}
%We could define weights for different types of fitness components if their
%energy contributions were known. Here, we'll use a simple/unweighted sum.
fitness = totalhbonds - (seqviolations+nonseqviolations);


if nargout>1
	info.seqviolations = seqviolations;
	info.nonseqviolations = nonseqviolations;
	info.totalhbonds = totalhbonds;
end

