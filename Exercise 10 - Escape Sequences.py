# What we just went over '\n' is one of the many escape sequences
# Here are a few more:

# Escape        |       What it does.
# \\                    Backslash (\)
# \'                    Single-quote (')
# \"                    Double-quote (")
# \a                    ASCII bell (BEL); Generally not recommend. It creates an audible or visual alert.
# \b                    ASCII backspace (BS); removes a character behind each \b used
# \f                    ASCII formfeed (FF); not common in modern programming, used to advance the paper to the next page
# \n                    ASCII linfeed (LF); used to create a new line
# \N{name}              Character named name in the Unicode database (Unicode Only)
    # print('\N{SMILING FACE WITH SMILING EYES}')
    # 😊
# \r                    Carriage return; moves the cursor/pointer back to the beginning of the line and the subsequent output overwrites the previous output. It appears as if the prior string was erased and replaced with the following one
    # input:  print("12345\r67890")
    # output: 67890
    # Commonly seen in progress bar/countdown timers
# \t                    Horizontal tab (TAB)
# \uxxxx                Character with 16-bit hex value xxxx        | Similar to the \N{name} ; but requires the 16-bit hex values
# \Uxxxxxxxx            Character with 32-bit hex value xxxxxxxx    | Similar to the \N{name} ; but requires the 32-bit hex values
# \v                    ASCII vertical tab (VT)
# \000                  Character with octal value 000              | Similar to \N{name} ; but requires octal values
# \xhh                  Character with hex value hh                 | Similar to \N{name} ; but requires hex values

tabby_cat = "\tI'm tabbed in."          # \t is used to tab 
persian_cat = "I'm split\non a line."   # \n is used to make a new line
backslash_cat = "I'm \\ a \\ cat."      # \\ is used to make a backslash ( \ )

# This variable uses triple-quotation 
# And a \t which is used for horiztonal tabbing 
# And a \n which is used to go to to a new line
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishes
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)          #prints the fat_cat variable

bacon = '''
Hello!
How are you1?
'''
bacon2 = """
Hello!
How are you2?
"""
print(bacon)
print(bacon2)


# using f-string and escape sequence

happy_day = """
I am mostly happy on {} days.\nI tend to frolic a lot with my partner.\nWe get {}\\{} time to time."""
happy_day_mod = happy_day.format('sunny','coffee','carbonated drinks')
print(happy_day_mod)