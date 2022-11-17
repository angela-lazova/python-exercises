# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 12:55:54 2022

@author: Angela Lazova
"""
#Imports
import random 

# Rock, Paper, Scizzors Game

#Setup and initial choice!
options = ['rock', 'paper', 'scizzors']
instructions = ["Let's play the rock, paper, scizzors game.You know how it goes..\n", 
                "To make a choice, simply write: rock, paper, or scizzors.\n"]
com_wins = 0
user_wins = 0

#Start the Game
print(*instructions)
choice = input("Your choice: ")
com_choice = random.choice(options) # computer's choice
print("Computer chose:", com_choice)


#Configure the result and choose again if the user wants another go.
while True:
# Possible outcomes for when the user chooses ROCK
    if choice == 'rock':
# and the computer chooses paper
        if com_choice == 'paper': # and the computer chooses paper
            print("Gotcha! Paper beats rock! I win.\n")
            com_wins += 1
            try_again = input("Want to play again? yes or no: ")
            if try_again == "no":
                print("Okay than, next time. Bye!")
                print("Game Summary! Computer won: ", com_wins, "times. You won:", user_wins, "times")
                break
            else:
                choice = input("Your choice: ")
                com_choice = random.choice(options)
                print('This time the computer chose: ', com_choice)
# and the computer chooses scizzors
        elif com_choice == 'scizzors':
            print("Ouch! Rock beats scizzors. You win.\n")
            user_wins += 1;
            try_again = input("Want to play again? yes or no: ")
            if try_again == "no":
                print("See ya!")
                print("Game Summary! Computer won: ", com_wins, "times. You won:", user_wins, "times")
                break
            else:
                choice = input("Let's go! Your choice: ")
                com_choice = random.choice(options)
                print('This time the computer chose: ', com_choice)
# and the computer chooses rock
        elif com_choice == 'rock':
            print("Hey! That's a draw...How do we know who wins?\n")
            try_again = input("Want to play again? yes or no: ")
            if try_again == "no":
                print("I'm sad to see you go... bye bye.")
                print("Game Summary! Computer won: ", com_wins, "times. You won:", user_wins, "times")
                break
            else:
                choice = input("Let's go! Your choice: ")
                com_choice = random.choice(options)
                print('This time the computer chose: ', com_choice)
                
                
 # Possible outcomes for when the user chooses PAPER
    if choice == 'paper':
# and the computer chooses scizzors
        if com_choice == 'scizzors':
            print("Gotcha! Scizzors beats paper! I win.\n")
            com_wins += 1
            try_again = input("Want to play again? yes or no: ")
            if try_again == "no":
                print("Okay than, next time. Bye!")
                print("Game Summary! Computer won: ", com_wins, "times. You won:", user_wins, "times")
                break
            else:
                choice = input("Your choice: ")
                com_choice = random.choice(options)
                print('This time the computer chose: ', com_choice)
# and the computer chooses rock
        elif com_choice == 'rock':
            print("Ouch! Paper beats rock. You win.\n")
            user_wins += 1;
            try_again = input("Want to play again? yes or no: ")
            if try_again == "no":
                print("See ya!")
                print("Game Summary! Computer won: ", com_wins, "times. You won:", user_wins, "times")
                break
            else:
                choice = input("Let's go! Your choice: ")
                com_choice = random.choice(options)
                print('This time the computer chose: ', com_choice)
# and the computer chooses paper
        elif com_choice == 'paper':
            print("Hey! That's a draw...How do we know who wins?\n")
            try_again = input("Want to play again? yes or no: ")
            if try_again == "no":
                print("I'm sad to see you go... bye bye.")
                print("Game Summary! Computer won: ", com_wins, "times. You won:", user_wins, "times")
                break
            else:
                choice = input("Let's go! Your choice: ")
                com_choice = random.choice(options)
                print('This time the computer chose: ', com_choice)
                
                
 # Possible outcomes for when the user chooses SCIZZORS
    if choice == 'scizzors':
# and the computer chooses rock
        if com_choice == 'rock':
            print("Gotcha! Rock beats scizzors! I win.\n")
            com_wins += 1
            try_again = input("Want to play again? yes or no: ")
            if try_again == "no":
                print("Okay than, next time. Bye!")
                print("Game Summary! Computer won: ", com_wins, "times. You won:", user_wins, "times")
                break
            else:
                choice = input("Your choice: ")
                com_choice = random.choice(options)
                print('This time the computer chose: ', com_choice)
# and the computer chooses paper
        elif com_choice == 'paper':
            print("Ouch! Scizzors beat paper. You win.\n")
            user_wins += 1;
            try_again = input("Want to play again? yes or no: ")
            if try_again == "no":
                print("See ya!")
                print("Game Summary! Computer won: ", com_wins, "times. You won:", user_wins, "times")
                break
            else:
                choice = input("Let's go! Your choice: ")
                com_choice = random.choice(options)
                print('This time the computer chose: ', com_choice)
# and the computer chooses scizzors
        elif com_choice == 'scizzors':
            print("Hey! That's a draw...How do we know who wins?\n")
            try_again = input("Want to play again? yes or no: ")
            if try_again == "no":
                print("I'm sad to see you go... bye bye.")
                print("Game Summary! Computer won: ", com_wins, "times. You won:", user_wins, "times")
                break
            else:
                choice = input("Let's go! Your choice: ")
                com_choice = random.choice(options)
                print('This time the computer chose: ', com_choice)

# If the user writer an invalid answer
    if choice != 'rock' and choice != 'paper' and choice != 'scizzors':
        print("Sorry. That's not a valid answer. Please choose:\n"
              "rock or paper or scizzors - exactyl how you see them.\n"
              "Capitalization is important because the computer is not really smart.")
        choice = input("Let's try again. Your choice: ")
        
    



