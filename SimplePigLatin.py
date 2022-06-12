text = "O Pig latin, is cool !"

textList = list(text.split(" "))
outp = ""

# [Pig] [latin,] [is] [cool]"
for word in textList:    
    if (not word[len(word)-1].isalpha()) and len(word) == 1:
        outp += word
    elif len(word) == 1:
        outp += word[0] + "ay"
    else:
        
        while ind<=len(word)-2:
            outp+=word[ind]
            ind+=1
        if word[len(word)-1].isalpha():
            outp += word[len(word)-1] + word[0] + "ay "
        else:
            outp += word[0] + "ay" + word[len(word)-1] + " "

print(outp.rstrip())