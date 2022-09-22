def main():
    word = input("Input: ")
    print(encoder(word))
    
    
def encoder(word):
    outp = ""
    for c in word:
        if word.count(c.lower()) > 1:
            outp += ')'
        else:
            outp += '('
    return outp


if __name__ == "__main__":
    main()
