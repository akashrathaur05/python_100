import random
word_list = ["aardvark", "baboon", "camel"]
random_word = random.choice(word_list)
print(random_word)
print("WELCOME TO HANGMAN GAME")
print("You have to guess the letters of the word")
place_holder = []
word_length = len(random_word)
for position in range(word_length):
    place_holder.append("_") # create a placeholder for the word
game_over = False
while not game_over:
    guessed_letter = input("guess a letter : ").lower() # get the guessed letter from the user
    for i in range(len(random_word)):
        if random_word[i] == guessed_letter:
            place_holder[i] = guessed_letter
    # for letter in random_word:
    #     if letter == guessed_letter:
    #         display += letter
    #     elif letter != guessed_letter and 
    #     else:
    #         display += "_"
    print("".join(place_holder))
    if "_" not in place_holder:
        game_over = True
        print("You win")
