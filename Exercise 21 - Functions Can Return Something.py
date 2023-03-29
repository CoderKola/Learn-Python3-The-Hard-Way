# We are creating an add function
def add(a,b):
    # Everytime this runs, it will first output what it is adding
    print(f"ADDING {a} + {b}")
    # return will result of the function call
    # since there is no true/false statement, it will solely return the result
    return a + b

def subtract(a,b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a,b):
    print(f"MULTIPLYING {a} + {b}")
    return a * b

def divide(a,b):
    print(f"DIVIDING {a}/{b}")
    return a / b

# This line is the first to be printed in the terminal
print("Let's do some math with just functions!")

# We are calling the functions and assigning it to variables
# Since we are calling it & there is a print() function, 
# it will also output into the terminal what it is doing
age = add(30,5)
height = subtract(78,4)
weight = multiply(90,2)
iq = divide(100,2)

# After we have assigned the function calls to the varaibles, we are using f-string to pass the variables
# each variable will only output the 'return' of the call. It will not output the print()
print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")


# A puzzle for the extra credit, type it in anyway.
print("Here is a puzzle.")

# All the functions are being called and stored into the 'what' variable
# The calculation follows PEMDAS as it also outputs which steps
# the calculation is going through since we have a print() function 
    # If the print function was not there, the 'what' will the store
    # the result of the function calls
what = add(weight, subtract(height, multiply(weight,divide(iq,2))))

# Here, we only want the results of 'return' that has been calculated in the 'what' variable
# Therefore, we only receive the 'what'
print("That becomes:", what, "Can you do it by hand?")


#### Testing

def sq_root(n):
    # print("now i'll print")
    return n**0.5 

c = sq_root(25)
