def main():
    text = input("Input text: ")
    print(f"Quantity of unique elements ={unique(text)}")


def unique(string):
    string = string.lower()
    outp = 0
    for c in string:
        if string.count(c) > 1 and (not c in outp):
            outp += 1      
    return outpt
