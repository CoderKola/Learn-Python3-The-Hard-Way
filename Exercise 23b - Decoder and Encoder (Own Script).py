# FILE ENCODER & DECODER
# Code 1: Recursive Function

print("This is a file encoder & file decoder by line.")

# USER INPUTS
file_path = input("What is the file path you are try to accessing?\nFILE_PATH = ")
error_type = input("""\nError types: 
'backslashreplace'	- uses a backslash instead of the character that could not be encoded
'ignore'	        - ignores the characters that cannot be encoded
'namereplace'           - replaces the character with a text explaining the character
'strict'	        - Default, raises an error on failure
'replace'	        - replaces the character with a questionmark
'xmlcharrefreplace'	- replaces the character with an xml character
ERROR_TYPE = """)

# Turn string into raw-bytes
encode_type = input("""\nEncoding & Decoding Types: 
* ascii         * utf-8         * utf-16        * utf-32
* iso-8859-1    * cp1252        * cp437         * cp850
* cp852         * cp1250        * cp1251        * cp1253
* cp1254        * cp1255        * cp1256        * cp1257
* cp1258        * iso-8859-2    * iso-8859-3    * iso-8859-4
* iso-8859-5    * iso-8859-6    * iso-8859-7    * iso-8859-8
* iso-8859-9    * iso-8859-10   * iso-8859-13   * iso-8859-14
* iso-8859-15   * iso-8859-16   * macroman      * macintosh
* utf-7         * utf-8-sig
ENCODING_TYPE (1) = """)

# From cooked_string into different encodes 
encode_type2 = input("ENCODING_TYPE (2) = ")

# FUNCTION to encode & decode file
def body(file_open):
    file_line = file_open.readline()
    # If there is a line...
    if file_line:
        # Clean each line of empty spaces
        file_line.strip()
        # Take the strings and code them into raw bytes
        raw_bytes = file_line.encode(encoding=encode_type,errors=error_type)
        # Let us also turn it back to normal
        cooked_string = raw_bytes.decode(encoding=encode_type,errors=error_type)
        # Let us encode that string into something else
        cooked_string2 = raw_bytes.decode(encoding=encode_type2,errors=error_type)
        print(cooked_string , "<===>" , raw_bytes , "<===>" , cooked_string2)
        return body(file_open)
        
# OPEN FILE
file_open = open(file_path,encoding=encode_type,errors=error_type)

# HEADER
print(f"Original <===> Encoding Type {encode_type} <===> Encoding Type 2 {encode_type2}")

# Function calling
body(file_open)

# Function is complete and we are closing the file
file_open.close()

# Thank you message
# Possible functionality can be added:
# Your text <===> bytes <====> another encoded language

print("-------------------------------------")
print("Thank you for using this script. End.")



# FILE ENCODER & DECODER
# Code 2: Loop
# This is useful if you solely want the encodings

# print("This is a file encoder & file decoder by line.")

# # USER INPUTS
# file_path = input("What is the file path you are try to accessing?\nFILE_PATH = ")
# error_type = input("""\nError types: 
# 'backslashreplace'	- uses a backslash instead of the character that could not be encoded
# 'ignore'	        - ignores the characters that cannot be encoded
# 'namereplace'           - replaces the character with a text explaining the character
# 'strict'	        - Default, raises an error on failure
# 'replace'	        - replaces the character with a questionmark
# 'xmlcharrefreplace'	- replaces the character with an xml character
# ERROR_TYPE = """)

# encode_type = input("""\nEncoding & Decoding Types: 
# * ascii         * utf-8         * utf-16        * utf-32
# * iso-8859-1    * cp1252        * cp437         * cp850
# * cp852         * cp1250        * cp1251        * cp1253
# * cp1254        * cp1255        * cp1256        * cp1257
# * cp1258        * iso-8859-2    * iso-8859-3    * iso-8859-4
# * iso-8859-5    * iso-8859-6    * iso-8859-7    * iso-8859-8
# * iso-8859-9    * iso-8859-10   * iso-8859-13   * iso-8859-14
# * iso-8859-15   * iso-8859-16   * macroman      * macintosh
# * utf-7         * utf-8-sig
# ENCODING_TYPE = """)

# # FUNCTION to encode & decode file
# def body(file_content):
#     if file_content:
#         # Take the strings and code them into raw bytes
#         raw_bytes = file_content.encode(encoding=encode_type,errors=error_type)
#         # Let us also turn it back to normal
#         cooked_string = raw_bytes.decode(encoding=encode_type,errors=error_type)
#         print("\nEncocding:\n",raw_bytes,"\n\nYour_Text:\n",cooked_string)

# # OPEN FILE
# file_open = open(file_path, mode='r', encoding=encode_type, errors=error_type)
# # Read the file
# file_content = file_open.read()

# # Function calling
# body(file_content)

# # Function is complete and we are closing the file
# file_open.close()

# # Thank you message
# print("-------------------------------------")
# print("Thank you for using this script. End.")

