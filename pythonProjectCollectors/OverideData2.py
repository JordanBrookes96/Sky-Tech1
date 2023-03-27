
f1 = open("data.txt", "r")
f2 = open("data2.txt", "w")

data = f1.read()
f2.write(data)
