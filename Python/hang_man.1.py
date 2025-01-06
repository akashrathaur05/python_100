import random
word_list = ['python', 'java', 'kotlin', 'javascript']
word = random.choice(word_list) # randomly choose a word from the list
print(word)
place_holder = ""
word_length = len(word)
for letter in range(word_length):
    place_holder += "_" # create a placeholder for the word
print(place_holder)