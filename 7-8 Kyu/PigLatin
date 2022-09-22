#Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.
text = "O Pig latin, is cool !"

def main():
    print(pig_it(text))
        

def pig_it(text):
    outpt = []
    
    for i in text.split():
        if i.isalpha():
            outpt.append(i[1:]+i[0]+'ay')
        else:
            outpt.append(i)
            
    return ' '.join(outpt)

if __name__ == "__main__":
    main()
