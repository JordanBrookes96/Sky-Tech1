
F = open("Data.txt", "r")
content = F.read()
uniqueWords = []
word = ""
for ch in content:
    if ch == " ":
        if not word in uniqueWords:
            uniqueWords.append(word)
        word = ""
    else:
        word += ch
if not word in uniqueWords:
    uniqueWords.append(word)
print(uniqueWords)
