#Hangman stages

def display_hangman(remaining_attempts):
   """
   Function to display the hangman based on the number of remaining attempts.
   """

   stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / \
                 - - - 
                """,
                # head, torso, both arms, and left leg
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / 
                 - - -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |      
                 - - -
                """,
                # head, torso, and left arm
                """
                   --------
                   |      |
                   |      O
                   |     \|
                   |      |
                   |     
                 - - -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                 - - -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                 - - -
                """,
                # initial state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                 - - -
                """
    ]
   return stages[remaining_attempts]

