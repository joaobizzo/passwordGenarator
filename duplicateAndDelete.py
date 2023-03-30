import os

# Name of the source file to be duplicated
origin_file = "things/passW/passwordLog.txt"

# Name of the destination file to be created
destin_file = "../../../../importante/pssw/psswd.txt"

# read the password from the origin_file and save in a variable
with open(origin_file, 'r') as file:
    newPass = file.read().replace('\n', '')

# Duplicate the file
with open(destin_file, 'a') as f:
    f.write('\n' + newPass + '\n')

# Remove the source file
os.remove(origin_file)

print("File duplicated and source file removed successfully.")

# replace <br> to a actually break line
with open(destin_file, 'r') as f:
    newPass = f.read().replace('<br>', '\n')