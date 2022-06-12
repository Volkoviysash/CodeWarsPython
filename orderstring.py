from curses.ascii import isdigit


sentence = "is2 Thi1s T4est 3a"
wordsarr = sentence.split(" ")
output = ""

dict = {}
for word in wordsarr:
    for c in word:
        if c.isdigit():
            dict[word] = int(c)

for word in sorted(dict.items(), key=lambda x: x[1]):
    output += word[0] + ' '

print(output.rstrip())