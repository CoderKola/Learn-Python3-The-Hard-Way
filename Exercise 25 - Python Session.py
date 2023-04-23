# if we use "import Exercise_25_EvenMorePractice as *", then we don't
# need to reference the functions using ex25 before every line
# we can directly use the function 
import Exercise_25_EvenMorePractice as ex25 

sentence = "All good things come to those who wait."

############
# first we want to break the word using the functions we have made 
# remember that in the function 'break_word()' we tell the system to return a list of words
words = ex25.break_words(sentence)
print(f"The sentence broken is: {words}")

# I want the first letter in the word
ex25.print_first_word(words)

# I want the last letter in the word
ex25.print_last_word(words)


############
# let's sort the words now
sorted_words = ex25.sort_words(words)
print(f"The words sorted: {sorted_words}")

# give me the first word in the sorted list
ex25.print_first_word(sorted_words)

# give me the last word in the sorted list
ex25.print_last_word(sorted_words)

############
# I want the first and last word in the sentence
ex25.print_first_and_last(sentence)

# I want the first and last word in the sorted sentence
ex25.print_first_and_last_sorted(sentence)

help(ex25.break_words)