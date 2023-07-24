#import section
import random
import time
import game_ascii_art
from words import word_list
from game_effects import GameColors as Colors
from hangman_stages import display_hangman

#Functions section
def get_random_word(word_list):
    """
    Function to select a random word from the list and 
    return the letter in uppercase.
    """
    word = random.choice(word_list) 
    return word.upper()

def game(word):
    """
     This function manages the Hangman game, taking player inputs,
     updating the game state, and providing appropriate feedback 
     to the player until the game is over.
    """
    #Variables 
    secret_word = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    remaining_attempts = 6
    print(display_hangman(remaining_attempts))
    print(secret_word)
    print("\n")
    #a while loop will run until user guess or runs out of tries
    while not guessed and remaining_attempts > 0:
        guess = input("Enter a letter: ").upper()
        #first condition: guessing a letter
        if len(guess) == 1 and guess.isalpha():
            #conditional block
            if guess in guessed_letters:
                print("You already guessed the letter {}".format(guess))
            elif guess not in word:
                print("Unfortunately {} is not in the word".format(guess))
                remaining_attempts -= 1
                guessed_letters.append(guess) 
            else:
                print("Great!{}, is in the word!".format(guess))
                guessed_letters.append(guess)
                #convert string to list and enumerates the words if secret_word is equal to guessed letter 
                new_word_list = list(secret_word)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for i in indices:
                    new_word_list[i] = guess
                secret_word = "".join(new_word_list)
                
                if "_" not in secret_word:
                    guessed = True
                    secret_word = word

        #second condition: guessing a word
        elif len(guess) == len(word) and guess.isalpha():
            #conditional block
            if guess in guessed_letters:
                print(game_ascii_art.VICTORY)
            elif guess != word:
                print("Unfortunately {} is not in the word".format(guess))
                remaining_attempts -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                secret_word = word
        # third condition: something other than a single letter
        else:
           print("Not a valid guess")
           print("word")
        #after every guess is handled, the word and hangman current state is printed
        print(display_hangman(remaining_attempts))
        print(secret_word)   
        
        


def main():
    """
    this functions gets a random word if the user wants to play 
    another round otherwise ends the game.
    """
    word = get_random_word(word_list)
    game(word)

#printing starting game
print(game_ascii_art.LOGO)
print(game_ascii_art.RULES)
print(Colors.Red + "Welcome to Hangman!")
user_name = input(Colors.Yellow + "Enter your name:")
print("Hi " + user_name + "! Time to play! =D")
time.sleep(1)
print("Start guessing...\n")
time.sleep(0.5)
 

if __name__ == "__main__":
    main()   
