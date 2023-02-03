#simple hangman game with one secret word

print("Try to guess the secret word before the hangman picture us complete.\n You can guess one letter at a time.\n If you guess a letter right, you will see the letter printed on the screen in the correct position/s in the word.\n If you guess wrong, an element will be added to the picture.\n")
secret_word = ("sunflower")
guess_counter = 1
lives = 9
finished = False
previous_guesses = ' '
placeholder = "_" * len(secret_word)
while lives > 0 and finished == False:
    guess = input(f'Enter guess {guess_counter}: ').lower()
    guess_counter = guess_counter + 1
    if len(guess) != 1 or guess.isalpha() == False:
         print("Input must be a single letter\n")
         continue
    
    if (guess in previous_guesses):
         print("Please choose a unique guess\n")
         continue 
    
           
    if guess in secret_word:
        print("This letter is in the word")
        position = secret_word.find(guess)
        placeholder = placeholder[:position] + guess + placeholder[position + 1:]

        if ('_' not in placeholder):
                finished = True



    else:
        print("Wrong guess")
        lives = lives - 1  

    print(placeholder)
    print("\n")

    previous_guesses = previous_guesses + guess




if lives == 0:
    print(f"You lost! The word was {secret_word}.\n")
else :
    print("You guessed the word on time!\nYay!\n o\n-|-\n ^\n")

