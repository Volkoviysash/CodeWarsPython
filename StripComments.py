strng = "apples, pears #and bananas \ngrapes\nbananas"
markers = ['#', '!']

#making list of lines
def strip_comments():
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

if __name__ == "__main__":
    strip_comments()
