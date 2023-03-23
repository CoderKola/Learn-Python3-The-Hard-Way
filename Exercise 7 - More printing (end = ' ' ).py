# More printing
# Similar to exercise 6

print("Mary had a little lamb.")                        # Just prints the string
print("Its fleece was white as {}.".format('snow'))     # Prints the string but uses .format() method. Inside the string we had {}. By using the .format() and storing a string 'snow' inside the .format(), we were able to call it into the {}. 
print("And everywhere that Mary went.")                 # Just prints the string
print("." * 10) #what'd that do?                        # This prints the '.' but 10 times

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

#Watch end = ' ' at the end. Try removing it to see what happens
# end = ' ' is a built in python
# It will create connect the current line with the coming line 

print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
print(end7 + end8 + end9 + end10 + end11 + end12)



#####  end= '' examples:
# ends the output with a space
print("Welcome to", end = ' ')
print("GeeksforGeeks")
# ends the output with '@'
print("Python", end='@')
print("GeeksforGeeks")