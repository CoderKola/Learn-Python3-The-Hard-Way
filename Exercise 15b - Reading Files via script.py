# This one does not require import module

# We are sending a string that informs the user to input the file name.
print("Please type your file name: ")

# This line of code gives the prompt in the terminal for where to input the code
# we use the input() function and store the user's input into the variable called
    # 'file_name'
file_name = input("> ")


# we then name a variable called 'txt_file' and store the function
# open() function with the parameter of 
    # file_name
    # which was what the user just gave us
    # it uses the full name along with the type of file extension it is
    # (i.e .txt)
txt_file = open(file_name)

# in the end, we print whatever was in that text file using the print function
# inside that print function is a the parameter we gave it to read
# we are commanding the txt_file.read() to be read
print(txt_file.read())

# When you are done reading the file, make sure to close it.
txt_file.close()



# Example 2
# print("Enter your file name: ")
# file_name_prompt = input("> ")

# open_file  = open(file_name_prompt)
# print(open_file.read())
