# Variables - they are nothing more than a name for something. Use good names or you will get lost trying to read your code again

#Note: if you get lost
#1. Write a commect above each line explaning to yourself in English what it does
#Read your .py file backward
#Read your .py file out loud, saying each the characters

cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available")
print("There are only", drivers, "drivers avaliable.")
print("There will be", cars_not_driven, "empty cars today.")
print("There will be", cars_not_driven, "empty_ cars today.")
print("We can transport", carpool_capacity, "people today.")
print("we have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car")


#Author first wrote: average_passengers_per_car = car_pool_capacity / passenger
#There was an error with the 'car_pool_capacity'. Why is that?

# Answer: Because 'car_pool_capacity' was not a variable that was defined. We used 'Carpool_capacity' instead of 'car_pool_capacity'.


#The difference between a single '=' and double '==' is that one is an arithmetic operator and the other is a comparison operator. 