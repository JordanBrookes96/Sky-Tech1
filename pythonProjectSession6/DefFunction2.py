def ones(number):
    result = ""
    if number == 1:
        result = "One"
    elif number == 2:
        result = "Two"
    elif number == 3:
        result = "Three"
    elif number == 4:
        result = "Four"
    elif number == 5:
        result = "Five"
    elif number == 6:
        result = "Six"
    elif number == 7:
        result = "Seven"
    elif number == 8:
        result = "Eight"
    elif number == 9:
        result = "Nine"
    elif number == 10:
        result = "Ten"
    elif number == 11:
        result = "Eleven"
    elif number == 12:
        result = "Twelve"
    elif number == 13:
        result = "Thirteen"
    elif number == 14:
        result = "Fourteen"
    elif number == 15:
        result = "Fifteen"
    elif number == 16:
        result = "Sixteen"
    elif number == 17:
        result = "Seventeen"
    elif number == 18:
        result = "Eighteen"
    elif number == 19:
        result = "Nineteen"


def ty(number):
    result = ""
    if number == 20:
        result = "Twenty"
    elif number == 30:
        result = "Thirty"
    elif number == 40:
        result = "Forty"
    elif number == 50:
        result = "Fifty"
    elif number == 60:
        result = "Sixty"
    elif number == 70:
        result = "Seventy"
    elif number == 80:
        result = "Eighty"
    elif number == 90:
        result = "Ninty"
    return result


answer = ""
num = int(input("Enter Any Number"))
if num >= 1000:
    answer = ones(int(num / 1000)) + " Thousand"
    num = num % 1000
if num >= 100:
    answer += ones(int(num/100)) + " Hundred"
    num = num % 100
if num >= 20:
    answer += ty(int(num/10) * 10)
    num = num % 10
if num >= 1:
    answer += ones(num)

print(answer)
