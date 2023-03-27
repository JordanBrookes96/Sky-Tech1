UpperAlpha = [0] * 26
LowerAlpha = [0] * 26
msg = input("Please Enter Any Message")

for ch in msg:
    if ord(ch) >= 65 and ord(ch) <= 90:
        UpperAlpha[ord(ch) - 65] += 1
    if ord(ch) >= 97 and ord(ch) <= 122:
        LowerAlpha[ord(ch) - 97] += 1

i = 0
while i < len(UpperAlpha):
    if UpperAlpha[i] > 0:
        print(chr(i + 65), UpperAlpha[i])
    i += 1

i = 0
while i < len(LowerAlpha):
    if LowerAlpha[i] > 0:
        print(chr(i + 97), LowerAlpha[i])
    i += 1
