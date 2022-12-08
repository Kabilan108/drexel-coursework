# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 20:16:53 2022

@author: CocosW
"""

import math
import sys

def risk_calc(sex, race, age, BP_treat, BP, TOT_C, HDL_C, smoker, diabetes):
    
    if smoker == "Yes": 
        smoker_num = 1;
    else:
        smoker_num = 0;
    
    if diabetes == "Yes": 
        diabetes_num = 1;
    else:
        diabetes_num = 0;
        
    age = float(age);
    BP = float(BP);
    TOT_C = float(TOT_C);
    HDL_C = float(HDL_C);
    
    if sex == "Female":
        if race == "White":
            if BP_treat == "Yes":
                Ind_Sum = -29.799*math.log(age) + 4.884*(math.log(age)**2) + 13.540*math.log(TOT_C) - 3.114*(math.log(age)*math.log(TOT_C)) - 13.578*math.log(HDL_C) + 3.149*math.log(age)*math.log(HDL_C) + 2.019*math.log(BP) + 7.574*smoker_num - 1.665*math.log(age)*smoker_num + 0.661*diabetes_num;
            else: 
                Ind_Sum = -29.799*math.log(age) + 4.884*(math.log(age)**2) + 13.540*math.log(TOT_C) - 3.114*(math.log(age)*math.log(TOT_C)) - 13.578*math.log(HDL_C) + 3.149*math.log(age)*math.log(HDL_C) + 1.957*math.log(BP) + 7.574*smoker_num - 1.665*math.log(age)*smoker_num + 0.661*diabetes_num;
            Baseline_surv = 0.9665;
            Mean_coef_xval = -29.18;
        else: 
            if BP_treat == "Yes":
                Ind_Sum = 17.114*math.log(age) + 0.940*math.log(TOT_C) - 18.920*math.log(HDL_C) + 4.475*math.log(age)*math.log(HDL_C) + 29.291*math.log(BP) - 6.432*math.log(age)*math.log(BP) + 0.691*smoker_num + 0.874*diabetes_num;
            else: 
                Ind_Sum = 17.114*math.log(age) + 0.940*math.log(TOT_C) - 18.920*math.log(HDL_C) + 4.475*math.log(age)*math.log(HDL_C) + 27.820*math.log(BP) - 6.087*math.log(age)*math.log(BP) + 0.691*smoker_num + 0.874*diabetes_num;
            Baseline_surv = 0.9533;
            Mean_coef_xval = 86.61;
    else:
        if race == "White":
            if BP_treat == "Yes":
                Ind_Sum = 12.344*math.log(age) + 11.853*math.log(TOT_C) - 2.664*(math.log(age)*math.log(TOT_C)) - 7.990*math.log(HDL_C) + 1.769*math.log(age)*math.log(HDL_C) + 1.797*math.log(BP) + 7.837*smoker_num - 1.795*math.log(age)*smoker_num + 0.658*diabetes_num;
            else: 
                Ind_Sum = 12.344*math.log(age) + 11.853*math.log(TOT_C) - 2.664*(math.log(age)*math.log(TOT_C)) - 7.990*math.log(HDL_C) + 1.769*math.log(age)*math.log(HDL_C) + 1.764*math.log(BP) + 7.837*smoker_num - 1.795*math.log(age)*smoker_num + 0.658*diabetes_num;
            Baseline_surv = 0.9144;
            Mean_coef_xval = 61.18;
        else: 
            if BP_treat == "Yes":
                Ind_Sum = 2.469*math.log(age) + 0.302*math.log(TOT_C) - 0.307*math.log(HDL_C) + 1.916*math.log(BP) + 0.549*smoker_num + 0.645*diabetes_num;
            else: 
                Ind_Sum = 2.469*math.log(age) + 0.302*math.log(TOT_C) - 0.307*math.log(HDL_C) + 1.809*math.log(BP) + 0.549*smoker_num + 0.645*diabetes_num;
            Baseline_surv = 0.8954;
            Mean_coef_xval = 19.54;
    
    risk = (1 - Baseline_surv)*math.exp(Ind_Sum - Mean_coef_xval);
    risk_percent = round(risk*100,2);
    
    #print(Baseline_surv)
    #print(Mean_coef_xval)
    #print(Ind_Sum)
    
    return(risk_percent) 

if __name__ == "__main__":
    sex = sys.argv[1]
    race = sys.argv[2]
    age = sys.argv[3]
    BP_treat = sys.argv[4]
    BP = sys.argv[5]
    TOT_C = sys.argv[6]
    HDL_C = sys.argv[7]
    smoker = sys.argv[8]
    diabetes = sys.argv[9]
    risk_calc(sex, race, age, BP_treat, BP, TOT_C, HDL_C, smoker, diabetes)