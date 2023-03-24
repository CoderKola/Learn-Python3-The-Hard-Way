# We can create a sample file via. the terminal:
    # echo "String of what you want to input into the file" > preferredfilename.txt
    # cat preferredfilename.txt
    # output will be the string that you just used and it will also create a sample file
# To learn more about cat, type in ther terminal:
    # 'man cat'

# The first modulo 'sys' is to allow the use of terminal input for argv
# The second modulo 'os.path' is to allow for 'exists' to be usable
    # https://docs.python.org/3/library/os.path.html ; more on os.path usage
from sys import argv
from os.path import exists

# Through the terminal, we will pass these three argument variables
script, from_file, to_file = argv

# We are letting the user know that one file
# is being copied to another
print(f"Copying from {from_file} to {to_file}")

# We could do these two on one line, how?

in_file = open(from_file)
indata = in_file.read()

# Will tell you how many bytes the file is.
print(f"The input file is {len(indata)} bytes long.")

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hi RETURN to continue, CTRL-C to abort.")
input()

# Once the user hits return....
# We will open the to_file or 'going to' file 
# in the mode of 'w' for write
out_file = open(to_file, 'w')
out_file.write(indata)  # This is used to overwrite the out_file with the content of indata file (from_file) 

# Just letting you know the process is done
print("Allright, all done.")

# Making sure to close both files
# The reason you close your files are limited managed 
    # by the os system 
out_file.close()
in_file.close()