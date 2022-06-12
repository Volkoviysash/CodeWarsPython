n = 907
nstr = str(n)
arrayofnumbs = []
out = ""
ind = len(nstr) - 1
while ind >= 0:
    if int(nstr[ind]) < int(nstr[ind])


for i in range(len(nstr)-1):
    if nstr[len(nstr)-1-i] > nstr[len(nstr)-1-i-1]:
        out+=nstr[:len(nstr)-i-1]
        for c in nstr[len(nstr)-i-1:]:
            arrayofnumbs.append(int(c))
        out += ''.join(str(x) for x in sorted(arrayofnumbs))
print(out)