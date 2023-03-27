f = open("pelican.txt", "r")
data = f.read()
print(f"Data type is {type(data)}")
print(data)

f = open("pelican.txt", "r")
pelican_list = f.readlines()
print(f"There is {len(pelican_list)} elements in the list")
for line in pelican_list:
    print(line.strip())

# Correct way to write this code is
#
# with open("pelican.txt", "r") as f:
#     data = f.read()
# print(f"Data type is {type(data)}")
# print(data)
#
# with open("pelican.txt", "r") as f:
#     pelican_list = f.readlines()
#     print(f"There is {len(pelican_list)} elements in the list")
#     for line in pelican_list:
#         print(line.strip())
