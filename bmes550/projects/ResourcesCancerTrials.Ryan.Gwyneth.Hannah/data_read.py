#https://acfdata.coworks.be/cancerdrugsdb.txt
#https://acfdata.coworks.be/ReDO_Trials_DB.txt

import requests

info = requests.get('https://acfdata.coworks.be/cancerdrugsdb.txt')
splitting_val = str(info.text).split("/20")
THE_LIST_OF_MEDICINES = []

for i in range(1,len(splitting_val)-1):
    voidL = []
    
    inner_split = splitting_val[i].split("	")
    #print(inner_split[1],inner_split[2] ,inner_split[-2])
    voidL.append(inner_split[1].replace("\r\n",""))
    voidL.append(inner_split[2])
    voidL.append(inner_split[-2])
    THE_LIST_OF_MEDICINES.append(voidL)

#print(THE_LIST_OF_MEDICINES)
#print(len(THE_LIST_OF_MEDICINES))


info = requests.get('https://acfdata.coworks.be/ReDO_Trials_DB.txt')
splitting_val = str(info.text).split("	")

input_coef = 39
input_self_ = 895

# required 0,9,10,31,33
THE_LIST_OF_CANCERS = []
for input_self in range(2,input_self_):
    voidL = []
    for i in range(input_coef*input_self,input_coef*(input_self+1)):
        if i==input_coef*input_self:
            voidL.append((splitting_val[i])[3:])
        elif i==input_coef*input_self+8:
            voidL.append((splitting_val[i]))
        elif i==input_coef*input_self+9:
            voidL.append((splitting_val[i]))
        elif i==input_coef*input_self+32:
            voidL.append((splitting_val[i]))
        elif i==input_coef*input_self+34:
            voidL.append((splitting_val[i]))
        

    THE_LIST_OF_CANCERS.append(voidL)
    
    
#print(THE_LIST_OF_CANCERS)