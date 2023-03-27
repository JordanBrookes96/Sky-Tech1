
ones=["","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
ty=["","","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninty"]

number = int(input("Enter Any Number:"))

answer = ""

if number >= 1000:
    answer += ones[int(number/1000)] +" Thousand "
    number = number % 1000

if number >= 100:
    answer += ones[int(number/100)] +" Hundred "
    number = number % 100

if number >= 20:
    if len(answer) == 0:
        answer += ty[int(number/10)] + " "
    else:
        answer += "and " + ty[int(number / 10)] + " "
    number = number % 10

if number >= 1:
    answer += ones[number]

print(answer)
