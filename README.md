# Hangman Game

The Hangman Game application provides users with the opportunity to engage in a classic game of chance against the computer. The gameplay commences with the user inputting their name. Subsequently, the game displays successive stages of the hangman from its initial stage while also selecting a random word, concealed at the onset of the game. Throughout the game, the player's objective is to guess the letters forming the chosen word correctly, with six lives corresponding to the hangman's body parts - head, body, right arm, left arm, right leg, and left leg. The outcome of each round is determined by the player's success in guessing the correct letters of the word.

Throughout the game, the user may encounter three potential scenarios when making a letter choice: the letter is present in the word, the letter is not part of the word, or the letter has been previously guessed by the player. Additionally, any input other than a single letter will be considered invalid, and it will not result in the deduction of a life.

Once the game is over the user is presented with the option to initiate another round or exit the application.
![Hangman Game](assets/images/)



## Table of Contents
+ [UX](#ux "UX")
  + [Site Purpose](#site-purpose "Site Purpose")
  + [Audience](#audience "Audience")
  + [Communication](#communication "Communication")
  + [Current User Goals](#current-user-goals "Current User Goals")
  + [New User Goals](#new-user-goals "New User Goals")
  + [Future Goals](#future-goals "Future Goals")
+ [Design](#design "Design")
   + [Wireframes](#wireframes "Wireframes")
+ [Features](#features "Features")
  + [Existing Features](#existing-features "Existing Features")
    + [Landing Page](#landing-page "Landing Page")
    + [Play Again](#play-again "Play Again or Quit App")
  + [Features Left to Implement](#features-left-to-implement "Features Left to Implement")
+ [Testing](#testing "Testing")
  + [Validator Testing](#validator-testing "Validator Testing")
  + [Manual Testing](#manual-testing "Manual Testing")
  + [Bugs](#bugs "Bugs")
  + [Unfixed Bugs](#unfixed-bugs "Unfixed Bugs")
+ [Technologies Used](#technologies-used "Technologies Used")
  + [Main Language](#main-language "Main Language")
  + [Frameworks, Libraries & Programs](#frameworks-libraries-programs "Frameworks, Libraries & Programs")
+ [Deployment](#deployment "Deployment")
    + [Version Control](#version-control "Version Control")
    + [Page Deployment](#page-deployment "Page Deployment")
+ [Credits](#credits "Credits")
  + [Content](#content "Content")
  + [Acknowledgements](#acknowledgements "Acknowledgements")


## Creating the Heroku app
When you create the app, you will need to
You must then create a _Config Var_ called `PORT`. Set this to `8000`
If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.
Connect your GitHub repository and deploy as normal.