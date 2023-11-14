#Step 5

import random
import hangman_words as hw
from replit import clear


chosen_word = random.choice(hw.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6


from hangman_art import logo,stages
print(logo)

print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()
   
    if guess in display:
      print(f"The letter {guess} has already been guessed.")
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        
      print(f"{guess} not in the word")
      lives -= 1
      if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

  
    
    print(stages[lives])