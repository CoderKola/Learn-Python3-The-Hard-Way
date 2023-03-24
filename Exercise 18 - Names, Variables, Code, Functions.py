# This one is like your scripts with argv
# We tell python that we want to make a function by using 'def'

# We use '*args' as a wildcard when we doubt the number of arguments
    # that we might have
def print_two(*args):
    arg1,arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")


# Call the function with the new parameters
print_two("Zed","Shaw")

# Ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")


# Call the function with the new parameters
print_two_again("Zed","Shaw")

# This one takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")


# Call the function with the new parameters
print_one("First!")

# This one takes no arguments
def print_none():
    print("I got nothin'.")

# Call the function with the new parameters
print_none()