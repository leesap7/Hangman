#simple hangman game with one secret word

print("Try to guess the secret word before the hangman picture us complete.\n You can guess one letter at a time.\n If you guess a letter right, you will see the letter printed on the screen in the correct position/s in the word.\n If you guess wrong, an element will be added to the picture.\n")
secret_word = ("sunflower")
guess_counter = 1
lives = 9
finished = False
placeholder = ("_ _ _ _ _ _ _ _ _")
rows, cols = (10, 10)
picture = [['.'] * cols] * rows
while lives > 0 and finished == False:
    guess = input(f'Enter guess {guess_counter}: ')
    guess_counter = guess_counter + 1
    if guess in secret_word:
        print("This letter is in the word")
        if guess == 's':
            placeholder = 's' + placeholder[1:]
        elif guess == 'u':
            placeholder = placeholder[:2] + 'u' + placeholder[3:]
        elif guess == 'n':
            placeholder = placeholder[:4] + 'n' + placeholder[5:]
        elif guess == 'f':
            placeholder = placeholder[:6] + 'f' + placeholder[7:]
        elif guess == 'l':
            placeholder = placeholder[:8] + 'l' + placeholder[9:]
        elif guess == 'o':
            placeholder = placeholder[:10] + 'o' + placeholder[11:]
        elif guess == 'w':
            placeholder = placeholder[:12] + 'w' + placeholder[13:]
        elif guess == 'e':
            placeholder = placeholder[:14] + 'e' + placeholder[15:]
        elif guess == 'r':
            placeholder = placeholder[:16] + 'r'

        if ('_' not in placeholder):
                finished = True



    else:
        print("Wrong guess")
        lives = lives - 1
        print(lives)     

    print(placeholder)
    print("\n")
    i, j = (0, 0)
    while i < rows:
        j = 0
        while j < cols:
            print(picture[i][j], end=' ')
            j = j + 1
        i = i + 1 
        print("\n")   
    
    print("\n")




if lives == 0:
    print(f"You lost! The word was {secret_word}.\n")
else :
    print("You guessed the word on time!\nYay!\n o\n-|-\n ^\n")

