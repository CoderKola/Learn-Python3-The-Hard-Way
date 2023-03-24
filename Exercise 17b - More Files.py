# this lets you create a file via script 

# from the os, we are importing system
    # OR you could also use: from os import system
import os

# system let us use this function which mimics internal/external command
    # echo [<any text message to print on the screen>]
os.system("echo 'This is a file created from sys import' > ex17c_sample.txt")
os.system("more ex17c_sample.txt")
