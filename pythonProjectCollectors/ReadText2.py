F = open("Data.txt", "r")
data = F.read()
count=0
for ch in data:
    if ch == " ":
        count += 1
print("words:",count+1)

