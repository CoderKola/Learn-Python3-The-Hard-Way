######## part 1
print("Let's practice everything.")
print('You\'d need to know \'bout escapes with \\ that do:')
print('\n newlines and \t tabs')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love\n
nor comprehend passion from intuition
and requires and explanation
\n\t\twhere there is none.
"""

# So far, we have seen thatL
#  \' makes a single quote
#  \n makes a new line
#  \t makes a tab
print("*"*20)
print(poem)
print("*"*20)

####### part 2
five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000

# using the function, we have stored each result within the function into each of 
# the variables provided 
beans, jars, crates = secret_formula(start_point)

# remember this is another way to format a string
print("WIth a starting point of: {}".format(start_point))
# it's just like with the f"" string
# using this print below, we can see what values were stored into each variable
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

###### part 3
# if printed, the output is '1000'
start_point = start_point/10

print("We can also do that this way:")
formula = secret_formula(start_point)

# this is an easy way to apply a list to a format string
# note that in the function, we also have, in order, jelly_beans, jars, crates
print("We'd have {} beans, {} jars, {} crates.".format(*formula))