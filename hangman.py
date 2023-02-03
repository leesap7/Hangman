#simple hangman game with one secret word
import random

print("Try to guess the secret word before the hangman picture us complete.\n" 
      "You can guess one letter at a time.\n"
      "If you guess a letter right, you will see the letter printed on the screen in the correct"
      "position/s in the word.\nIf you guess wrong, an element will be added to the picture.\n")
words = ["sunflower", "arabesque", "ocean", "chocolate", "secrets", "magnet", "scarecrow", "castle"]
secret_word = random.choice(words)
finished = False
previous_guesses = ' '
placeholder = "_" * len(secret_word)
rows, cols, lives, guess_counter = (6, 6, 9, 1)
picture = [['.' for i in range(cols)] for j in range(rows)]

while lives > 0 and finished == False:
    guess = input(f'Enter guess {guess_counter}: ').lower()
    guess_counter = guess_counter + 1
    if len(guess) != 1 or guess.isalpha() == False or guess in previous_guesses:
         print("Guess must be a unique, single letter.\n")
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
        else:
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
