uniqueWords = []
msg = input("Enter Any Message:")
word = ""
for ch in msg:
    if ch == " ":
        if not word in uniqueWords:
            uniqueWords.append(word)
        word = ""
    else:
        word += ch
if not word in uniqueWords:
    uniqueWords.append(word)
print(uniqueWords)
