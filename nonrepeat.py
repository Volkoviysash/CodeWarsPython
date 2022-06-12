string = "abcdeaB"
string = string.lower()
outp = ""
for c in string:
    if string.count(c) > 1 and (not c in outp):
        outp += c        
print(len(outp))