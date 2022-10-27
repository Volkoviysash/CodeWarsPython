inpt = "AABCCCCD"
outp = []
ind = 0

while ind < len(inpt):
    if ind == 0:
        outp += inpt[ind]
        ind += 1
    elif inpt[ind-1] == inpt[ind]:
        ind += 1
    else:
        outp+=inpt[ind]
        ind += 1
print(outp)
