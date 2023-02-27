import sys
import glob
import os


if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']

# Construct a portable wildcard pattern
pattern = os.path.join(hdir, '*')


file_list = glob.glob(pattern)
for file_name in file_list:
    print(file_name)

print("-------------------------------------------------------")

# # TODO: use os.path.getsize to find each file's size
file_list = glob.glob(pattern)
for file_name in file_list:
    file_size = os.path.getsize(file_name)
    print("The file", file_name, "has a size of", file_size, "bytes")

print("-------------------------------------------------------")

# # TODO: Add a test to only display files that do not have a size of zero

file_list = glob.glob(pattern)
for file_name in file_list:
    file_size = os.path.getsize(file_name)
    if file_size > 0:
        print("The file", file_name, "has a size of", file_size, "bytes")

print("-------------------------------------------------------")

# # TODO: Remove the leading directory name(s) from each filename before you print it -
# # using os.path.basename()

file_list = glob.glob(pattern)
for file_name in file_list:
    file_size = os.path.getsize(file_name)
    if file_size > 0:
        print("The file", os.path.basename(file_name), "has a size of", file_size, "bytes")

print("-------------------------------------------------------")