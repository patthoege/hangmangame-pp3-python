"""
ASCII art illustration for the game 
obtained from:
http://patorjk.com/software/taag/#p=display&h=0&v=0&f=Big&t=HANGMAN%0AYOU%20WON!%0AGAME%20OVER%0APLAY%20AGAIN
"""

from game_effects import GameColors as C

#logo start game

LOGO = (
 C.R 
 + r'''
  -x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-
   _    _             _   _    _____   __  __            _   _                        
  | |  | |    /\    | \ | |  / ____| |  \/  |    /\    | \ | |                       
  | |__| |   /  \   |  \| | | |  __  | \  / |   /  \   |  \| |                       
  |  __  |  / /\ \  | . ` | | | |_ | | |\/| |  / /\ \  | . ` |                       
  | |  | | / ____ \ | |\  | | |__| | | |  | | / ____ \ | |\  |                       
  |_|  |_|/_/    \_\|_| \_|  \_____| |_|  |_|/_/    \_\|_| \_|

  -x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x- 
  Hangman Game v1.0
  Coded by Patricia Höge
  Code Institute
  PP3 - Python
'''
)

# rules of the game

RULES = (
 C.B
 + r"""
   =========================================================================
    -x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x
   x   _______________________________________________________________   x
   |  |                                                               |  |
   x  |               ===============================                 |  x
   |  |                         GAME RULES                            |  |
   x  |               ===============================                 |  x
   |  |                                                               |  |
   |  |  1 - The player try to figure out an unknown word by          |  |
   x  |      guessing letters.                                        |  x
   |  |  2 - If too many letters which do not appear in the           |  |
   |  |      word are guessed,the player is hanged and loses.         |  |
   x  |  3 - As letters in the word are guessed,will be written.      |  x
   x  |  4 - The hangman is drawn in 6 parts(for 6 letter guesses)    |  x
   |  |                                                               |  |
   |  |_______________________________________________________________|  |
   -x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-
   =========================================================================
 """
)

#banner for the next game

PLAY_AGAIN = (
 C.B
 + r"""
  -x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x
  _____    _               __     __            _____            _____  _   _ 
 |  __ \  | |         /\   \ \   / /    /\     / ____|    /\    |_   _|| \ | |
 | |__| | | |        /  \   \ \_/ /    /  \   | |  __    /  \     | |  |  \| |
 |  ___/  | |       / /\ \   \   /    / /\ \  | | |_ |  / /\ \    | |  | . ` |
 | |      | |____  / ____ \   | |    / ____ \ | |__| | / ____ \  _| |_ | |\  |
 |_|      |______|/_/    \_\  |_|   /_/    \_\ \_____|/_/    \_\|_____||_| \_|

  -x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x
 """
)


# banner victory

VICTORY = (
 C.Y
 + r"""
-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-
   __     __   ____    _    _    __          __   ____    _   _   _                       
   \ \   / /  / __ \  | |  | |   \ \        / /  / __ \  | \ | | | |                      
    \ \_/ /  | |  | | | |  | |    \ \  /\  / /  | |  | | |  \| | | |                      
     \   /   | |  | | | |  | |     \ \/  \/ /   | |  | | | . ` | | |                      
      | |    | |__| | | |__| |      \  /\  /    | |__| | | |\  | |_|                      
      |_|     \____/   \____/        \/  \/      \____/  |_| \_| (_)     

-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-                                                                    
 """
)

#banner game over

GAME_OVER = (
  C.R
  + r"""           
-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-                                                                                  
    _____            __  __  ______    ____  __      __ ______  _____            
  / ____|    /\    |  \/  ||  ____|  / __ \ \ \    / /|  ____||  __ \           
 | |  __    /  \   | \  / || |__    | |  | | \ \  / / | |__   | |__| |          
 | | |_ |  / /\ \  | |\/| ||  __|   | |  | |  \ \/ /  |  __|  |  _  /           
 | |__| | / ____ \ | |  | || |____  | |__| |   \  /   | |____ | | \ \           
  \_____|/_/    \_\|_|  |_||______|  \____/     \/    |______||_|  \_\     

-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-       
  """
)


 
                                                                                        
                                                                                        
                                                                                  
                                                                                        

                                                                                        
                                                                                        

