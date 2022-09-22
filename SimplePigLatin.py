#Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.
text = "O Pig latin, is cool !"

def main():
    pig_it(text)
        

def pig_it(text):
    textList = list(text.split(" "))
    outp = ""    
    for word in textList:    
        if (not word[len(word)-1].isalpha()) and len(word) == 1:
            outp += word
        elif len(word) == 1:
            outp += word[0] + "ay "
        else:
            ind = 1
            while ind<=len(word)-2:
                outp+=word[ind]
                ind+=1
            if word[len(word)-1].isalpha():
                outp += word[len(word)-1] + word[0] + "ay "
            else:
                outp += word[0] + "ay" + word[len(word)-1] + " "
    return(outp.rstrip())

if __name__ == "__main__":
    main()
