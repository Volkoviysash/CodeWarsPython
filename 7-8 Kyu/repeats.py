def main():
    text = input("Input text: ")
    print(f"Number of repeating letters = {repeats(text)}")

def repeats(string):
    string = string.lower()
    outp = ""
    for c in string:
        if string.count(c) > 1 and (not c in outp):
            outp += c     
    return len(outp)

if __name__ == "__main__":
    main()
