
f1 = open("data.txt", "r")
f2 = open("data2.txt", "w")
newdata=""
data = f1.read()
for ch in data:
    if ch=="a":
        newdata+="*"
    else:
        newdata+=ch
f2.write(data)
