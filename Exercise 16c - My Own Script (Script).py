# exercise 16b; I made my own script where you have to input arguemnt variables from the terminal
# exericse 16c; I want to do it soly through the script
# text checker/reader/editor


# We want to beging by asking if you are trying to create a text file or not?
print("Are you trying to create a text file?")
prompt1 = input("Please type in '1' if true or '0' if false. ")

# This route begins if the user has typed 1
if int(prompt1) == 1:
    print("First, we will check if the name of your file exist.")
    # We are assinging the user's filename.txt as 'file_name'
    file_name = input("What is the name of your file? Include .txt in the end of your file name.")
    
    # 'try' 'except' 'else' is required for 'x' open function. 
    # We will try to attempt to create the file first and see if it opens using 'x'
    try:
        file = open(file_name, 'x')
    # If the file does not exist, it will tell the user it already exist and will read the 
    # contents of the file back to the user. 
    except FileExistsError:
        print("Your file already exist!")
        
        # We open the file in read mode to be able to print it back out
        file = open(file_name, 'r')
        file_read = file.read()
        print(f"Here are the contents if your file:\n{file_read}")
        #closing the file after it has been opened
        file.close()
    else:
        print("Your file does not exist... we will create a new one")
        print("You have five lines to introduce what you want to include in the text file.")
        line1 = input("Line 1: ")
        line2 = input("Line 2: ")
        line3 = input("Line 3: ")
        line4 = input("Line 4: ")
        line5 = input("Line 5: ")
        
        # loop to write the files
        lines = [line1, line2, line3, line4, line5]
        for i in lines:
            file.write(i)
            file.write('\n')
        # Closing the file now
        file.close()
        
        # Opening the file and reading it back
        file = open(file_name,'r')
        file_read = file.read()
        print(f"Here are the contents of your file: {file_read}")
        
        #Closing the file now
        file.close()
elif int(prompt1) == 0:
    print("Then you must be here to edit one of your existing files. And yes I'm only giving you these two options.\nThere are other modes to open the file but I will keep it limited for this exercise.")
    file_name = input("What is the name of the file? Please include fullname.txt: ")
    
    # opens file for read and write
    # we are renaming it as 'your_file'
    with open(file_name, 'r+') as your_file:
    
    # reading the content back to you
        content = your_file.read()
        print(f"The contents of your file is:\n{content}")

        # go to the end of the file now
        your_file.seek(0,2)

        # we want to add to the end of your file
        print("\nLet us add to the end of your file.")
        your_file.write(input("Write what you would like to add: "))

        # Let's go back to the top
        your_file.seek(0)

        # Let's read back everything you have in this file
        file_read= your_file.read()
        print(f"\n The full content of your file is:\n{file_read}")
    
else:
    print("That was not one of the options, please try again.")