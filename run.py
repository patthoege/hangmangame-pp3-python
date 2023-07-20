#import section
import random
import time
import game_ascii_art
import game_effects
from words import word_list

#Start section
print("Welcome to Hangman!")
user_name = input("Enter your name:")
print("Hi " + user_name + "! Time to play! =D")
time.sleep(1)
print("Start guessing...\n")
time.sleep(0.5)


def get_random_word():
    """
    Function to select a random word from the list and return the letter in uppercase.
    """
    word = random.choice(word_list)
    return word.upper()
