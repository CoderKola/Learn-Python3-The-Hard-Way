# Asking Questions with user inputs

# We used an end = ' ' to tell the print to not end the line awith a newline character and go to the next one. 
# This allows us to make it all consistent in one line in the output. It then connects the user-input to that line.
# Question..... Input   (This is the format)
print("How old are you?", end = ' ')
age = input()
print("How tall are you?", end= ' ')
height = input()
print("How much do you weigh?", end= ' ')
weight = input()

print(f"So, you're {age} years old, {height} tall and {weight} heavy.")


# Example:

# get input from user
inputString = input("How many cows do you own? ")

#you can also get an input via prompt
print('The inputted string is:', inputString)


