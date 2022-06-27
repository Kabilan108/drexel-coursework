function numerrors = trainandtest(Xtrain, Ttrain, Xtest, Ttest)
    %helper function, used in cross validation function
    %goal is to provide a loss (numerrors) for a given dataset and labels
    model = fitcsvm(Xtrain, Ttrain,'KernelFunction',...
        'rbf', 'Standardize', true);
    preds = predict(model, Xtest);
    numerrors = sum(preds ~= Ttest); %how many labels misclassified
end


