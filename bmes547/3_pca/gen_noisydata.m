function [X]=gen_noisydata(n,d,noiseratio,scale,meancenter)
% generate linear data with noise
% X is mxn data matrix (m samples, n dimensions)
% Copyright (C) by Ahmet Sacan

if ~exist('noiseratio','var'); noiseratio=0.3; end
if ~exist('scale','var'); scale = 1; end
if ~exist('meancenter','var'); meancenter = true; end
if numel(scale)==1; scale=repmat(scale,1,d); end

X=zeros(n,d);
for i=1:n
  X(i,:) = (rand*ones(1,d)+rand(1,d)*noiseratio).*scale;
end

if meancenter
	X=X-repmat(mean(X,1),n,1);
end

