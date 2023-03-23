# A string is a bit of text you want to display to someone or 'export' out of the program you are writing.
# These strings can contain a number of variables using the "f-string" method with the {}
#
# i.e 
# print(f"some stuff here{a_variable}") 
# OR
# print(f"some other stuff {another_var})")

# ASIDE from "f-string" method, pythod also has another kind of formatting using '.format()' syntax
# Also, what is a { } - 'Curley Bracket?'
# They are used to define a data structure called a dictionary (a key/value mapping) in a list 

#Start Exercise:
# We set a variable called 'types_of_people' and store the value 10
types_of_people = 10

# We are then using a format-string method here and storing it in variable 'x'. This can can easily be accessed later using print syntax. 
x = f"There are {types_of_people} types of people."

# We are storing "binary" in a variable called 'binary'
binary = "binary"
# We are storing "don't" in the variable 'do_not' We then use format-string method and include the two-said variables in the formatted-string. 
do_not = "don't"
#String is put inside a string (1)
y = f"Those who know {binary} and those who {do_not}."


# We retreive the variables x and y
print(x)
print(y)

# We are printing the x and y variables using f-string method but with an adjustment using "I said:" 
# String is put inside a string (2 & 3)
print(f"I said: {x}")
print(f"I said: {y}")


#Here, we will start using '.format()'
hilarious = True
joke_evaluation = "Isn't that joke so funny?! {}"

# .format() was used and inside the parameter was the 'hilarious' variable which was printed out.
# The '.format()' is used by:
# variable1.format(variable2)
# String is put inside a string (4)
print(joke_evaluation.format(hilarious))  #KEY POINT


#Concanating Strings
w = "This is the left side of..."
e = "a string with a right side."

print(w + e)