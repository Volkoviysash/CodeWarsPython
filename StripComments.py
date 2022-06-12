strng = "apples, pears \ngrapes\nbananas"
markers = ['#', '!']

#making list of lines
strngList = list(strng.split("\n"))
strngoutput = ""
strngarray = []

for line in strngList:
    strngoutput = ""
    for c in line:
        if c in markers:
            break
        else:
            strngoutput += c
    strngarray.append(strngoutput.rstrip())

print('\n'.join(strngarray))