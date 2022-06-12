text = input("Enter: ")
outp = ""

for c in text:
    if text.count(c) > 1 and not c in outp:
        outp += c
print(len(outp))