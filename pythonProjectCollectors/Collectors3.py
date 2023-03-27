
alpha = [0]*26
msg = input("Please Enter Any Message")

for ch in msg:
    if ord(ch) >= 65 and ord(ch) <= 90:
        alpha[ord(ch) - 65] += 1
    if ord(ch) >= 97 and ord(ch) <= 122:
        alpha[ord(ch) - 97] += 1

i = 0
while i < len(alpha):
    if alpha[i] > 0:
        print(chr(i+65), alpha[i])
    i += 1