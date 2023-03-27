def addition(*data):
    if len(data) == 0:
        print("Nothing Too ADD")
    else:
        total = 0
        for d in data:
            total += d
        print("The Sum Of All Numbers Is:", total)


addition(2, 3)
addition(1, 2, 3, 4, 5, 6, 7, 8, 9, 5, 4, 56, 23, 547, 5258)
addition()
