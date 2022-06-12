from ast import arg


args = [-3,-2,-1,2,10,15,16,18,19,20]

temp = []
outp = []

indx = 0


temp.append(args[indx])
indx+=1
while temp[0] + 1 == args[indx+1]:
    temp.append(args[indx+1])    