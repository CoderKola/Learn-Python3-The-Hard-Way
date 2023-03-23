# What is a string?
# A string is something you put around a double-quotes "..." in which whatever is inside is converted to a string 

# What is a formatted string?
# We used formatted strings to embed variables inside them. It is done by using a special {} sequence and then putting the variable you want inside the {} characters.
# The string must also start with the letter 'f' which stands for 'format' before the first double-quotation mark (You can also use single, double, or triple quotation marks) 


#Note: Your variable name cannot start with a numeric character.

name = 'Zed A. Shaw'
age = 35 
height_in = 74 # Inches
weight_lb = 180 # Lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

#Inches to cm converter
height_cm = 2.54 * height_in

#Pounds to Kg converter
weight_kg = 0.453592 * weight_lb
weight_kg_rounded = round(weight_kg,2)

print(f"Let's talk about {name}.")
print(f"""He's {height_in}" tall.""")
print(f"In centimeters, he's {height_cm}cm tall")
print(f"He's {weight_lb}lb heavy.")
print(f"He's {weight_kg_rounded}kg heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# This line is tricky, try to get it exactly right
total = age + height_in + weight_lb
print(f"If I add my {age}, {height_in}, and {weight_lb} I get {total}.")


#Test User Input

name = input("What is your name? ")
print(f"Welcome, {name}!")