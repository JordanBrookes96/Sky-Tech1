def findWords(msg, findW):
    word = ""
    count = 0
    for ch in msg:
        if ch == " ":
            if word == findW:
                count += 1
            word = ""
        else:
            word += ch

    if word == findW:
        count += 1
    print("There are", count, findW, "in the message")


findWords("Where is bob in london bob in back bob avc bob", "bob")
