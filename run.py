# import section
import random
import time
import sys
import game_ascii_art
from words import word_list
from game_effects import GameColors as Col
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


def display_word(word, guessed_letters):
    """
    Functions creates a string for the current state of the word,
    showing guessed letters and underscores for unknown letters.
    """
    secret_word = ""
    for letter in word:
        if letter in guessed_letters:
            secret_word += letter
        else:
            secret_word += "_ "
    return secret_word


def get_guess(guess):
    """
    Get a valid letter guess from the player and returns a single letter
    guessed by the player.
    """
    while True:
        if len(guess) != 1 or not guess.isalpha():
            print(Col.R + "Invalid input. Please enter a single letter.")
            print(Col.Reset)
            guess = input(Col.B + "Enter a letter: ").upper()
        else:
            return guess


def is_guess_correct(word, guess):
    """
    This function check two args if the guessed letter is correct.
    the boolean return true if guess is correct.
    """
    return guess in word


def update_guessed_letters(guessed_letters, guess):
    """
    This functions add two args the guess that the player guessed so far
    to the set of guessed letters.
    """
    guessed_letters.add(guess)


def game(word):
    """
     This function manages the Hangman game, updating the game state,
     and providing appropriate feedback to the player until the game is over.
    """
    # variables
    guessed = False
    guessed_letters = set()
    remaining_attempts = 6
    # print hangman and display the secret word
    print(display_hangman(remaining_attempts))
    print(display_word(word, guessed_letters))
    # a while loop to handle the users input
    while not guessed and remaining_attempts > 0:
        guess = get_guess(input(Col.B + "Enter a letter: ")).upper()
        if guess in guessed_letters:
            print(Col.Y + "You already guessed the letter {}".format(guess))
            print(Col.Reset)
        elif guess in word:
            print(Col.G + "Great! {} is in the word!".format(guess))
            print(Col.Reset)
            update_guessed_letters(guessed_letters, guess)
        else:
            print(Col.Y + "{} is not in the word".format(guess))
            print(Col.Reset)
            remaining_attempts -= 1
            update_guessed_letters(guessed_letters, guess)

        secret_word = display_word(word, guessed_letters)
        print(display_hangman(remaining_attempts))
        print(secret_word)

        if secret_word == word:
            guessed = True

        print("Guessed letters: ", ", ".join(guessed_letters))

    # displays the current banner if wins or loses the game
    if guessed:
        print(game_ascii_art.VICTORY)
        print(Col.C + "Good job! " + word + " is the word!")
    else:
        print(game_ascii_art.GAME_OVER)
        print(Col.C + "The word was " + word)


def play_again_or_quit():
    """
    Function to chose whether the player wants to play again or quit the game.
    """
    while True:
        choice = input(Col.Y + "Next Round?(Y/N) ").upper()
        if choice == "Y":
            print(Col.Reset)
            return True
        elif choice == "N":
            return False
        else:
            print(Col.R + "Invalid choice. Please enter 'Y' or 'N'.")


def game_rules():
    """
    Function to ask the player if they want to read the game rules.
    """
    while True:
        typewriter(Col.C + "Do you want to read the game rules?(Y/N)")
        answer = input().upper().strip()
        if answer == "Y":
            print(game_ascii_art.RULES)
            return True
        elif answer == "N":
            typewriter(Col.Y + "Let's get started!\n")
            return False
        else:
            print(Col.R + "Invalid choice. Please enter 'Y' or 'N'.")


def typewriter(text):
    """
    Function to add a typewriter effect to print statements.
    """
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.02)
    print()


def main():
    """
    this function gets a random word if the user wants to play
    another round otherwise ends the game.
    """
    # printing starting game
    print(game_ascii_art.LOGO)
    typewriter(Col.R + "Welcome to Hangman!")
    time.sleep(1)
    game_rules()
    time.sleep(1)
    typewriter(Col.Y + "Enter your name:")
    user_name = input().strip()
    if user_name == "":
        user_name = "Anonymous"
    typewriter(Col.Y + f"Hi {user_name}! Time to play! =D")
    time.sleep(1)
    typewriter(Col.C + "Start guessing...\n")
    time.sleep(0.5)

    print(Col.Reset)

    while True:
        word = get_random_word(word_list)
        game(word)
        if not play_again_or_quit():
            print(Col.C + "Thanks for playing! Guess me soon =D")
            sys.exit()


if __name__ == "__main__":
    main()
