from sys import argv

script, input_file = argv

# This is a function to read the file assinged to 'f'
def print_all(f):
    print(f.read())

# This is a function to rewind the file back to the beginning, first line
def rewind(f):
    f.seek(0)

# This is a line that count what line number the line is in the file
    # and outputs that line# andline content
def print_a_line(line_count, f):
    # .readline() scans each yte of the file until it finds an \n character. Then it 
    # stops reading and returns what it found
    print(line_count, f.readline())

# Now that we've passed through script and file name, we will open that file
    # and assing it to variable, 'current_file' (global variable)
current_file = open(input_file)
print("First let's print the whole file:")
print_all(current_file)

# This is to rewind to use the next function
print("\nNow let's rewind, kind of like a tape.")
rewind(current_file)

# Useing the print_a_line function, we will pass the parameters
print("Let's print three lines:")

# current_line is a global variable that is assigned what
    # we want the count to start at
# Everytime current_file.readline() is used, each output is different as it sends out the coming line
# if current_file.readlines() was used, this would output ['all the lines']

current_line = 0
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_file.close()