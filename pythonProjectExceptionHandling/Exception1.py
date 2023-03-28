try:
    A = int(input("Please enter any number:"))
    print(A * 2)
    nums = [3, 9]
    print("Hello!")
    file = open("data.txt")
    data = file.read()
    print(data)
    print(nums[0])
    print(nums[1])
except ValueError:
    print("Please enter digits only")
except IndexError:
    print("There is only 2 values in the list")
except FileNotFoundError:
    print("File not found")
except:
    print("Something went wrong")
