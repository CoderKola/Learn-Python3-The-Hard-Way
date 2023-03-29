# DBES - Decode Bytes, Encode Strings
# Python uses UTF-8 to store strings
# This is different from 'from sys import argv' because we are importing
# the whole 'sys' module
import sys

# To call argv from the system, we must use 'sys.argv'
# Then we have to unpack the variables from 'sys.argv' into
# script, input_encoding, error
    # There are 3 argument variables
    # Script - is the name of the current script used to run this code
    # input_encoding - 
script, input_encoding, error = sys.argv

# We are creating a function called 'main' with three arguments: language_file, encoding, errors
    # This function will take the language file and read each line
        # If there is a line, it will print the line, the encoding of the line, and the errors
            # It will return continue until there is no more line as we have sent it to return back to main()
def main(language_file, encoding, errors):
    # We we called main, we called language_file
    # 'language_file' is assigned to variable 'languages' which uses open() function
        # We are then telling the script to see if there is a line and read each line
        # Finally, we are assigning it to the variable 'line'
    line = language_file.readline()
            # If a line does exist, it will execute the following
    if line:
                # it will use the print_line() function we have created
        print_line(line, encoding, errors)
                # this will loop back again until there is no more line
        return main(language_file, encoding, errors)

# We are creating a function called 'print_line' with three arguments: line, encoding, errors
# This function is only used within main()
# therefore, the arguments pass through main will also pass through here
def print_line(line, encoding, errors):
    # From each line, we are using a strip function
    # What does strip() do?
    # The strip() method removes any leading (spaces at the beginning) 
    # and trailing (spaces at the end) characters (space is the default leading character to remove
    next_lang = line.strip()
    # The encode() method returns the bytes(encoded form) of the string 
    # If no encoding is specified, UTF-8 will be used.
    # format for encode() is:
        # string.encode(encoding=encoding, errors=errors)
        # encoding and errors are both optional but the default is encoding = 'utf-8'
    # We are then setting the encoded data into raw_bytes   
    raw_bytes = next_lang.encode(encoding, errors = errors)
        # We use the same format for decode. We have encoding and erross which defaults to
            # utf-8 and 'strict' unless said otherwise
        # Str.decode(encoding='UTF-8',errors='strict')
    cooked_string = raw_bytes.decode(encoding, errors = errors)
    
    #### This should be the final output saying here are the raw bytes for the string and the decoded version of it
    print(raw_bytes, "<===>", cooked_string)

# The variable 'languages' is set to call the built-in open() function
# We have not fully explored the whole capability of open() but here is the full syntax format
    # open(file, mode='r', buffering=- 1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
        # encoding - is the name of the encoding used to decode or encode the file
        # encoding should only be used in text mode
            # Here, we are encoding in 'utf-8' 
            # UTF-8 (8-bit value) is one of the most commonly used encodings, and Python often defaults to using it. 
            # Unicode Transformation Format (UTF)

# We can make it so that we can also use the terminal to run this
# but since encoding is also used here, it may be more efficient to run via this.
languages = open("ex23_languages.txt",encoding="utf-8")

main(languages,input_encoding,error)



#  These are the 'errors' possible values: 
# 'backslashreplace'	- uses a backslash instead of the character that could not be encoded
# 'ignore'	- ignores the characters that cannot be encoded
# 'namereplace'	- replaces the character with a text explaining the character
# 'strict'	- Default, raises an error on failure
# 'replace'	- replaces the character with a questionmark
# 'xmlcharrefreplace'	- replaces the character with an xml character

# When executing this script in the terminal
# we can use:
# python "scriptname.py" utf-8 strict