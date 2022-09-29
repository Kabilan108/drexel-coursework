function [MI] = calcMI(I1, I2)

assert(all(size(I1)==size(I2)),'Images need to be the same size')

% convert to uint8
% (easier to compute and makes sure the problem doesn't blow up)
I1 = im2uint8(I1)+1;
I2 = im2uint8(I2)+1;

% compute the joint probability distributions
jointHist = accumarray([I1(:) I2(:)], 1);
jointProb = jointHist / numel(I1);
% compute joint entropy
jointEntropy = -sum(jointProb(jointProb>0).*log2(jointProb(jointProb>0)));

% compute the marginal probabilities
probI1 = sum(jointProb, 1);
probI2 = sum(jointProb, 2);
% Compute the marginal entropy
entropy1 = -sum(probI1(probI1>0).*log2(probI1(probI1>0)));
entropy2 = -sum(probI2(probI2>0).*log2(probI2(probI2>0)));

% calculate Mutual Information
MI = entropy1 + entropy2 - jointEntropy;

end