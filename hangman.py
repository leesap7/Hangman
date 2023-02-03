#simple hangman game with one secret word

print("Try to guess the secret word before the hangman picture us complete.\n You can guess one letter at a time.\n If you guess a letter right, you will see the letter printed on the screen in the correct position/s in the word.\n If you guess wrong, an element will be added to the picture.\n")
secret_word = ("sunflower")
guess_counter = 1
lives = 9
finished = False
previous_guesses = ' '
placeholder = "_" * len(secret_word)
rows, cols = (6, 6)
picture = [['.' for i in range(cols)] for j in range(rows)]

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
        print(lives) 
        if lives == 8:
             m = 0
             while m < cols:
                picture[5][m] = "_"
                m = m + 1
        elif lives == 7:
             n = 0
             while n < rows:
                  picture[n][0] = "|"
                  n = n + 1
        elif lives == 6:
             m = 0
             while m < cols - 1:
                  picture[0][m] = "_"
                  m = m + 1
        elif lives == 5:
             picture[1][cols - 2] = "|"
        elif lives == 4:
             picture[2][cols - 2] = "o"
        elif lives == 3:
             picture[3][cols - 2] = "|"
        elif lives == 2:
             picture[3][cols - 3] = "-"
        elif lives == 1:
             picture[3][cols - 1] = "-"
        elif lives == 0:
             picture[4][cols - 2] = "^"

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

    previous_guesses = previous_guesses + guess




if lives == 0:
    print(f"You lost! The word was {secret_word}.\n")
else :
    print("You've guessed the word on time!\nYay!\n o\n-|-\n ^\n")
