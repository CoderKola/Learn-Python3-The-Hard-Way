# There are other functions that you must remember:
    # close() which closes the file
    # read() reads the contents of the file. you can assign the result to a variable
    # readline() reads just one line of a text file
    # write('stuff') writes "stuff" to the file
    # seek(0) moves the read/write location to the beginning of the file 
    # truncate() empties the file. Watch out if you care about the file


# we are passing two argumetn variables through 'argv' from the system
from sys import argv

# these two argument variables passed via terminal is stored in 'script' and 'filename' 
script, filename = argv

# Now we are giving the statement that the file is going to be erased 
print(f"We're going to erase {filename}.")

# We are giving you the option to abort that. If you use CTRL-C (^C) in the terminal when
# the script is running, it will abort the process. 
print("if you don't want that, hit CTRL-C (^C).")

# At the same time, we are also giving you the option to continue the process of deleting whatever
# was in the .txt file
print("If you do want that, hit RETURN.")

# This prompt allows the user to interact with the process. Here you are able 
# to choose whether to continue the process by pressing enter or abort by using
# CTRL-C (^C)
input("?")

# If you selected abort, the terminal will output 'KeyboardInterrupt'
# If you choose to press enter, it will .open() the file 
print("Opening the file...")
target = open(filename, 'w')

# It will then truncate or empty the file
print("Truncating the file. Goodbye!")
target.truncate()

# Now that the file is emptied, we will enter some new lines.
print("Now I'm going to ask you for three lines.")

# We will ask the user three times to add information
line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")

# After asking for three items, we are telling the user that we are 
# going to add that to the file
print("I'm going to write these to the file.")

# we are using list_name.write() to add to the .txt file
# 
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close()

# Note:
# In line 35, 'target = open(filename, 'w')'
# the 'w' is needed to edit the file. 
# What this is doing is, we are opening the file in the mode of 'open for writing'
# These are called modes:
#
# CHARACTER                     |                   Meaning
# 'r'                                               open for reading (default)
# 'w'                                               open for writing, truncating the file first
# 'x'                                               open for exclusive creation, failing if the file already exist; will create a file if it doesn't exist
# 'a'                                               open for writing, appending to the end of file if it exists
# 'b'                                               binary mode
# 't'                                               text mode (default)
# '+'                                               open for updating (reading and writing)