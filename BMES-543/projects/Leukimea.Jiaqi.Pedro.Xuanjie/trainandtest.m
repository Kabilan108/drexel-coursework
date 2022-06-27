function numerror = trainandtest(Xtrain,Ttrain, Xtest,Ttest)


mdl = fitcsvm(Xtrain,Ttrain,'KernelFunction','rbf');
Ytest = mdl.predict(Xtest);
numerror = sum(~strcmp(Ytest, Ttest));