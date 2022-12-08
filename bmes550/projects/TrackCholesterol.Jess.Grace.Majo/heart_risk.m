%% Jess Baggett calculates risk of heart disease
%formula comes from https://www.mdcalc.com/calc/38/framingham-risk-score-hard-coronary-heart-disease#evidence
function risk=heart_risk(age,sex,smoker,tot_chol,HDL,syst_bp,meds)
%outer loop is for gender as this determines the formula used
if strcmpi(sex,'female')
    %if user is smoker set corresponding value
    if strcmpi(smoker,'yes')
        smoke=1;
    else
        smoke=0;
    end
    %if user is taking medication for BP set correstponding value
    if strcmpi(meds,'yes')
        treated=1;
    else
        treated=0;
    end
    %if user is older than 78 set age to 78 (formula stops at 78)
    if age>78
        age=78;
    end
%formula
L=31.764001*log(age)+22.465206*log(tot_chol)+(-1.187731)*log(HDL)+2.552905*log(syst_bp)+0.420251*treated+13.07543*smoke+(-5.060998)*log(age)*log(tot_chol)+(-2.996954)*log(age)*smoke-146.5933061;
risk=(1-0.98767^(exp(L)))*100;
risk=sprintf('%.2f%%',risk);

    %if user is male
else
%if user is smoker set corresponding value
    if strcmpi(smoker,'yes')
        smoke=1;
    else
        smoke=0;
    end
    %if user is taking medication for BP set correstponding value
    if strcmpi(meds,'yes')
        treated=1;
    else
        treated=0;
    end
    %if user is older than 78 set age to 78 (formula stops at 78)
    if age>70
        age=70;
    end
%formula
L=52.00961*log(age)+20.014077*log(tot_chol)+(-0.905964)*log(HDL)+1.305784*log(syst_bp)+0.241549*treated+12.096316*smoke+(-4.605038)*log(age)*log(tot_chol)+(-2.84367)*log(age)*smoke+(-2.93323)*log(age)*log(age)-172.300168;
risk=(1-0.9402^(exp(L)))*100;
risk=sprintf('%.2f%%',risk);
end