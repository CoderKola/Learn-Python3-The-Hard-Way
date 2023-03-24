from sys import argv

script, file_name = argv

print(f"\nThe script you are running is {script}.")
print(f"We will be creating a {file_name}.\nIf it already exists, it will not create {file_name}.\n")

print(f"We will now attempt to create {file_name}...")

try:
    # Try to open the file for exclusive creation
    file = open(file_name,'x')
except FileExistsError:
    # Handle the case where the file already exists
    print("File already exists!")
else:
    # Write to the file if it was created successfully
    print("The file does not exist... creating new one.\n")
    print("What would you like to input?")
    line1 = input("Line 1: ")
    line2 = input("Line 2: ")
    line3 = input("Line 3: ")

    lines = [line1, line2, line3]
    for i in lines:
        file.write(i)
        file.write('\n')
    #close the file
    file.close()

# I also want to know what the content of the file is after I have made it. Let's read it. 
file = open(file_name, 'r')

# I want it to print oput what it is reading
print(f"Here are the contents of {file_name}: ")
print(file.read())

# Close the file again
file.close()

# I want it to output only what the first line is
file = open(file_name, 'r')
file_first_line = file.readline()
print(f"The first line of your text file is:\n{file_first_line}")

# closing file
file.close()