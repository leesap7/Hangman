#simple hangman game 

print("Try to guess the secret word before the hangman picture us complete.\n You can guess one letter at a time.\n If you guess a letter right, you will see the letter printed on the screen in the correct position/s in the word.\n If you guess wrong, an element will be added to the picture.\n")
secret_word = ("sunflower")
guess_counter = 1
lives = 10
placeholder = ("_ _ _ _ _ _ _ _ _")
while lives > 0:
    guess = input('Enter guess' guess_counter ' :')
    guess = guess + 1
    if guess in secret_word:
        print("This letter is in the word")
        
    else:
        print("Wrong guess!")
        lives = lives - 1



