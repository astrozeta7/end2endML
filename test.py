a = [1,1,2,2,3]

c = 0
opdict = {} 
for i in a:
    if i in opdict.keys():
        opdict[i] +=1
    else:
        opdict[i] =1

opdict2 = {}   
for k, v in opdict.items():
    if v != 1:
        opdict2[k] = v

print(opdict2)