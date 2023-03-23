from sys import argv

# "import" is what we use to add features (modules) to the python script
# "argv" is an argument variable that holds the arguments you pass 
    # to your python script when you run it via terminal

# This is an "import" that adds functions to python
# The functions constitute a "module" of code
# (These modules can be called libraries)
# "argv" is the "argument variable" for short 
# that holds the variables that you send in (or "pass") to python

script, first, second, third = argv
# This line "unpacks" argv into four variables from left to right

print("This script is called:", script)
print("Your first variable is:", first)
print("You sceond variable is:", second)
print("Your third variable is:", third)




## In your TERMINAL:

# You use your terminal/window powershell/bash/mingw to run this 
# cd yourself into the directory with the pythong script then you can run it
# command can be: python "File name.py" testing bacon egg
# testing is first variable, bacon is second variable, egg is third variable

# [Input] Sample terminal cmd
# python "Exercise 13 - Parameters, Unpacking, Variables.py" This was hard

# [Output]
# This script is called Exercise 13 - Parameters, Unpacking, Variables.py
# Your first variable is: This
# Your second variable is: is
# Your third variable is: hard

# What this is doing is, you are running python via your terminal
# and selecting the file/script called "Exercise 13 - Parameters, Unpacking, Variables".
# You are then passing in the four variables you have prompted in the script.
    # If you give less than four arguments and you are trying to unpack three, it will output a ValueError saying it expected 4 but got 3.

# The script or "Exercise 13 - Parameters, Unpacking, Variables" unpacks the variables
# through line 8