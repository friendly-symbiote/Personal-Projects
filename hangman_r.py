import random
from hangman_art import *
from hangman_words import *

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(logo)

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("\n\nGuess a letter: ").lower()

    if guess in display:
        print(f"\nYou already chose {guess}.")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"\nCurrent position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        print(f"\n{guess} is not in the chosen word. You lose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("\nYou lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"\n{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("\nYou win.")

    print(stages[lives])