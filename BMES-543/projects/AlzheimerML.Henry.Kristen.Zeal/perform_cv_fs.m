function [error, selected, model] = perform_cv_fs(data, bin_labels, cv, selected)
%function for feature selection, cross validation.
%input:  cv is crossvalidation object
%        data is a matrix of doubles size (numSubjects, numGenes)
%        selected is a vector of column numbers
%        if selected not provided, feature selection is performed
%        bin_labels is binary vector from get_binary_labels.m

%%
%perform fs if not already done
if ~exist('selected', 'var')
     selected =sequentialfs(@trainandtest, data,...     
     bin_labels,'cv',cv,'options',...
     statset('display','iter'),'direction','forward');
end

%train model on selected features
model = fitcsvm(data(:, selected),bin_labels, 'kernelFunction','rbf'); %return model

%perform validation on trained model
error = crossval(@trainandtest, data(:, selected),... % cross val error
    bin_labels, 'partition',cv);

