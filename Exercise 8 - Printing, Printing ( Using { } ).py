# We will focus on using .format()
# Previous exercises indicate that .format() can be used by inserting a string or a variable between the .format()
    # It is then linked to {} of the string
    # .format() can be also used like .format(item1, item2, item3, item4) depending on the number of {} you have used

formatter = "{} {} {} {}"

# Related back to the {} in the formatter and sends item in the current .format() below into each {}. 
# Each item going back to the {} is separated by the commas 
print(formatter.format(1,2,3,4))
print(formatter.format("one","two","three","four"))
print(formatter.format(True,False,False,True))              # You don't have to put quotes around True or False because they are python keywords. They are usually not used as strings and if you do convert them into strings, it will not work.
print(formatter.format(formatter,formatter,formatter,formatter))
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a haiku"
))

#Personal Test
print('.' * 25)
something = """Hi there {}
Thank you for joining me! Let me tell you a little about myself.
My name is {}. I code for about {} - {} hours a day. I am two weeks in.
Excited for the journey!
"""
print(something.format('Coders!','Koala',3,4))

# The result of a .format() is that { } with a new variables 