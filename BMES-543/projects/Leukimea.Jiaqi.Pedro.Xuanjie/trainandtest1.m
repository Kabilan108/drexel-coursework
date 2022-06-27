function numerror1 = trainandtest1(Xtrain1,Ttrain1, Xtest1,Ttest1)

mdl1 = fitcsvm(Xtrain1,Ttrain1,'KernelFunction','rbf');
Ytest1 = mdl1.predict(Xtest1);
numerror1 = sum(~strcmp(Ytest1, Ttest1));