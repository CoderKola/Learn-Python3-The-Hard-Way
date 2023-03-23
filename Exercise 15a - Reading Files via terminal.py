# From the sys module, we are importing argv 
# argv is holding the two argument variables which are 
    # inputting via. terminal
from sys import argv

# these two argument variables are unpacked via argv from left to right
# in the terminal, we put the script name we are using and the name of the file
# "script" is part of the argv argument which includes the name of the script itself as [0]index
script, filename = argv

# we are passing a function to open that file name using open()
# the file name is passed through "filename.txt" in the terminal
txt = open(filename)

# After we input the two argument variables into Python, 
# python will read line 13 above 'open()' function and then 
# use the following two lines of codes below  
# We are using a format-string method and printing the string along with the filename we have 
    # given in the terminal 
print(f"Here's your file {filename}:")

# We are also using another function called txt.read() which reads
# the txt file we have given. 
print(txt.read()) 



