strng = "foobar99"
outp = ""
indx = 0

while indx < len(strng):
    if strng[indx:].isdigit():
        outp += strng[:indx]
        newnumber = str(int(strng[indx:])+1)
        zeroes = len(strng) - len(outp) - len(newnumber)
        for _ in range(zeroes):
            outp+="0"
        outp += newnumber
        break
    else: 
        indx+=1
if indx >= len(strng):
    outp += strng + "1"

print(outp)
