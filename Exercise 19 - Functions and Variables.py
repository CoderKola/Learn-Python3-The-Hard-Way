# Method 1
    # We defined a function named 'cheese_and_crackers' that take two parameter named 'cheese_count' and 'boxes_of_crackers'
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # This function stores four print lines. Two uses f-string method and the other two are singlular prints. 
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

    # We then call for the function by passing the numbers directly into the call()
print("We can just give the function numbers directly:")
cheese_and_crackers(20,30)

# Method 2
print("OR, we can just give the function numbers directly:")

amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Method 3
print("We can even do math inside too:")

cheese_and_crackers(10+20,5+6)

# Method 4 (Combined with method 2)
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)