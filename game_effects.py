"""
Import section
"""
import colorama
from colorama import Fore

class GameColors():
    """
    Holds a color shortcut library for the text in the game
    """
    Red = Fore.RED
    Green = Fore.GREEN
    Blue = Fore.BLUE
    Yellow = Fore.YELLOW
    Magenta = Fore.MAGENTA
    Cyan = Fore.CYAN
    Reset = Fore.RESET

def strip_color_codes(text):
    """
    Function to remove color codes from the given text
    https://www.w3schools.com/python/ref_string_strip.asp
    """
    return Fore.strip(text)






