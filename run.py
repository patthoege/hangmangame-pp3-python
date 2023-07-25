#import section
import random
import time
import sys
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
        guess = input(Colors.Magenta + "Enter a letter: ").upper()
        #first condition: guessing a letter
        if len(guess) == 1 and guess.isalpha():
            #conditional block
            if guess in guessed_letters:
                print(Colors.Yellow + "You already guessed the letter {}".format(guess))
            elif guess not in word:
                print(Colors.Yellow + "Unfortunately {} is not in the word".format(guess))
                remaining_attempts -= 1
                guessed_letters.append(guess) 
            else:
                print(Colors.Green +"Great! {}, is in the word!".format(guess))
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
                print(Colors.Green + "Great!{}, is in the word!".format(guess))
            elif guess != word:
                print(Colors.Yellow + "Unfortunately {} is not in the word".format(guess))
                remaining_attempts -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                secret_word = word
        # third condition: something other than a single letter
        else:
           print(Colors.Red +"Not a valid guess")
        #after every guess is handled, the word and hangman current state is printed
        print(display_hangman(remaining_attempts))
        print(secret_word)  
        print(word)

    #check whether the player guess the word correctly or ran out of tries    
    if guessed:
        print(game_ascii_art.VICTORY)
        print(Colors.Green + "Good job! {} is in the word!".format(guess))
    else:
        print(game_ascii_art.GAME_OVER) 
        print(Colors.Cyan +"The word was " + word) 


def play_again_or_quit():
    """
    Function to chose whether the player wants to play again or quit the game.
    """
    while True:
       choice = input(Colors.Yellow + "Next Round?(Y/N) ").upper()
       if choice == "Y":
           return True
       elif choice == "N":
           return False
       else:
           print(Colors.Red + "Invalid choice. Please enter 'Y' OR 'N'.")
        
def main():
    """
    this function gets a random word if the user wants to play 
    another round otherwise ends the game.
    """
    #printing starting game
    print(game_ascii_art.LOGO)
    print(game_ascii_art.RULES)
    print(Colors.Red + "Welcome to Hangman!")
    user_name = input(Colors.Yellow + "Enter your name:")
    print("Hi " + user_name + "! Time to play! =D")
    time.sleep(1)
    print("Start guessing...\n")
    time.sleep(0.5)

    while True:
        word = get_random_word(word_list)
        game(word)
        print(game_ascii_art.PLAY_AGAIN)
     
        if not play_again_or_quit():
           break

    while play_again_or_quit():
        word = get_random_word(word_list)
        game(word)
    # If the player chooses not to play again, exit the program
    print(Colors.Cyan + "Thanks for playing!")
    sys.exit()

if __name__ == "__main__":
    main()   