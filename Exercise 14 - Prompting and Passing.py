# use argv and input together
# this is needed for the next exercise where you will learn to read and write files

# we are calling a import for 'agrv' from the sys module which refers to the terminal
# in agrv, we have two variables stored which is 'script' and 'user_name'. 
# These are inputted via terminal when it is prompted for.

# If you want the audience to input data into the script while it is running, 
# use the input()
from sys import argv 

script, user_name = argv
prompt = '> '

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")