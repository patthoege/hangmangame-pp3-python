# import section
import random
import time
import sys
import game_ascii_art
from words import word_list
from game_effects import GameColors as C
from game_effects import strip_color_codes
from hangman_stages import display_hangman

# functions section


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
    # variables
    secret_word = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    remaining_attempts = 6
    print(display_hangman(remaining_attempts))
    print(secret_word)
    print("\n")
    # a while loop will run until user guess or runs out of tries
    while not guessed and remaining_attempts > 0:
        guess = input(C.M + "Enter a letter: ").upper()
        # first condition: guessing a letter
        if len(guess) == 1 and guess.isalpha():
            # conditional block
            if guess in guessed_letters:
                print(C.Y + "You already guessed the letter {}".format(guess))
            elif guess not in word:
                print(C.Y + " {} is not in the word".format(guess))
                remaining_attempts -= 1
                guessed_letters.append(guess)
            else:
                print(C.G + "Great!{}, is in the word!".format(guess))
                guessed_letters.append(guess)
                new_word_list = list(secret_word)
                index = [i for i, letter in enumerate(word) if letter == guess]
                for i in index:
                    new_word_list[i] = guess
                secret_word = "".join(new_word_list)
                if "_" not in secret_word:
                    guessed = True
                    secret_word = word
        # second condition: guessing a word
        elif len(guess) == len(word) and guess.isalpha():
            # conditional block
            if guess in guessed_letters:
                print(C.G + "Great!{}, is in the word!".format(guess))
            elif guess != word:
                print(C.Y + "Unfortunately{} is not in the word".format(guess))
                remaining_attempts -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                secret_word = word
        # third condition: something other than a single letter
        else:
            print(C.R + "Not a valid guess")
        print(display_hangman(remaining_attempts))
        print(secret_word)
        print(word)

    # check whether the player guess the word correctly or ran out of tries
    if guessed:
        print(game_ascii_art.VICTORY)
        print(C.G + "Good job! {} is in the word!".format(guess))
    else:
        print(game_ascii_art.GAME_OVER)
        print(C.C + "The word was " + word)


def play_again_or_quit():
    """
    Function to chose whether the player wants to play again or quit the game.
    """
    while True:
        choice = input(C.Y + "Next Round?(Y/N) ").upper()
        if choice == "Y":
            print(C.Reset)
            return True
        elif choice == "N":
            return False
        else:
            print(C.R + "Invalid choice. Please enter 'Y' OR 'N'.")


def game_rules():
    """
    Function to ask the player if they want to read the game rules
    """
    while True:
       typewriter(C.C + "Do you want to read the game rules?(Y/N)")
       answer = input().upper().strip()
       if answer == "Y":
            print(game_ascii_art.RULES)
            return True
       elif answer == "N":
            print(C.Y + "Let's get started!\n")
            return False
       else:
            print(C.R + "Invalid choice. Please enter 'Y' OR 'N'.")


def typewriter(text):
    """
    Function to add a typewriter effect to print statements
    """
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.05)
    print()


def main():
    """
    this function gets a random word if the user wants to play
    another round otherwise ends the game.
    """
    # printing starting game
    print(game_ascii_art.LOGO)
    game_rules()
    typewriter(C.R + "Welcome to Hangman!")
    time.sleep(1)
    user_name = input(C.Y + "Enter your name:")
    typewriter("Hi " + user_name + "! Time to play! =D")
    time.sleep(1)
    typewriter("Start guessing...\n")
    time.sleep(0.5)

    print(C.Reset)

    while True:
        word = get_random_word(word_list)
        game(word)
        print(game_ascii_art.PLAY_AGAIN)
        if not play_again_or_quit():
            print(C.C + "Thanks for playing! Guess me soon =D")
            sys.exit()


if __name__ == "__main__":
    main()