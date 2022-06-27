function [bin_labels, remove] = get_binary_labels(labels, class1, class2)
%function useful because we are training multiple classifiers
%input: labels is cell array or table of characters
%        class1 and class2 are strings for the 2 classes
%        
%output: bin_labels: binary vector where class1 -> 0 and class2 -> 1
%        remove:     binary vector of labels not in class1 or 2

remove = ~(strcmp(labels, class1) |... %indices of samples to remove
           strcmp(labels, class2));    %AKA, not in class1 or class2
labels = labels(~remove);

bin_labels = zeros(numel(labels), 1);
bin_labels(strcmp(labels, class2)) = 1;

end

