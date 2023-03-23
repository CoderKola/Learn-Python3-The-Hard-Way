# Arithmetic Operators
# These include: + - / * % < > <= >=

# + 'plus' adds
# - 'minus' subtracts
# / 'slash' divides
# * 'asterisk' multiplies
# % 'modulo' gives the REMAINDER of a division 
# < less than
# > greater than
# <= less than or equal to
# >= greater than or equal to
# ** Exponentional 

#Note: PEMDAS or PE(M&D)(A&S)
# Left to Right
# In order of parentheses, left to right, first is exponentional, then (Multiplication and Division), then (Addition and Subtration)

print("I will now count my chickens:")

print("Hen", 25 + 30 / 6)                   #30
print("Roosters", 100 - 25 * 3 % 4)         #97

print("Now I will count the eggs: ")

# Step 1: (1 + 4 % 2 - 1 / 4 + 6)
# Step 2: (1 + 0 - 0.25 + 6)
# Step 3: (1 - 0.25 + 6)
# Step 4: (0.75 + 6)
# Step 5: (6.75)
print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)    #6.75

print("Is it true that 3 + 2 < 5 - 7?")     #False

print(3 + 2 < 5 - 7)                        #False 

print("What is 3 + 2?", 3 + 2)              #5
print("What is 5 - 7?", 5 - 7)              #-2

print("Oh, that's why it's False.")         #Because 5 < -2 is false. 5 is not less than -2

print("How about some more.")

print("Is it greater?", 5 > -2)             #True
print("Is it greater or equal?", 5 >= -2)   #True
print("Is it less or equal?", 5 <= -2)      #False