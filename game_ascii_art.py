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
   =======================================================================
    -x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x
   |   _______________________________________________________________   |
   |  |            -x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-          |  |
   |  |             _  _       _  _   __ _    _       _  _            |  |
   x  |            | || | /_\ | \| |/ __|  \/  | /_\ | \| |           |  x
   |  |            | __ |/ _ \| .` | (_ | |\/| |/ _ \| .` |           |  |
   |  |            |_||_/_/_\_\_|\_|\___|_|  |_/_/_\_\_|\_|           |  |
   x  |                                                               |  x
   |  |            -x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-          |  |
   |  |_______________________________________________________________|  |
   -x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-
   =======================================================================             
   Hangman Game v1.0
   Coded by Patricia Höge
'''
)

# rules of the game

RULES = (
 C.B
 + r"""
   ========================================================================
    -x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x
   x   _______________________________________________________________   x
   |  |                                                               |  |
   x  |               ===============================                 |  x
   |  |                         GAME RULES                            |  |
   x  |               ===============================                 |  x
   |  |                                                               |  |
   |  |  1 - Try to find the secret word by choosing letters.         |  |
   |  |  2 - If you guess lots of wrong letters, you might            |  |
   |  |     lose and see a hangman.                                   |  |
   x  |  3 - As letters in the word are guessed, will be written.     |  x
   x  |  4 - The hangman is drawn in 6 parts(for 6 letter guesses)    |  x
   |  |                                                               |  |
   |  |_______________________________________________________________|  |
   -x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-
   ========================================================================
 """
)


# banner victory

VICTORY = (
 C.Y
 + r"""
-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-
 __   __ __  __ __  __      __ __  _  _  _
 \ \ / / _ \| | | | \ \    / / _ \| \| || |      
  \ V / (_) | |_| |  \ \/\/ / (_) | .` ||_|      
   |_| \___/ \___/    \_/\_/ \___/|_|\_|(_) 

-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-                                                              
 """
)

#banner game over

GAME_OVER = (
  C.R
  + r"""           
-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-                                                                                  
    __       _   __ ___    __ __   __ __ ___
  / __| /_\ |  \/  | __|  / _ \ \ / / __| _ \   
 | (_ |/ _ \| |\/| | _|  | (_) \ V /| _||   /   
  \___/_/ \_\_|_ |_|___| _\___/_\_/_|___|_|_\  

-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x  
  """
)


 
                                                                                        
                                                                                        
                                                                                  
                                                                                        

                                                                                        
                                                                                        

