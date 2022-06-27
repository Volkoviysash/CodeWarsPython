world = input("Input: ")
outp = ""
for c in word:
    if word.count(c.lower()) > 1:
        outp += ')'
    else:
        outp += '('
print(outp)

#((()(((((((((()((((())((((((((()((
#((()(((((((((()((((())((((((((()((
#))()))))()())))))()())(()()))())))
