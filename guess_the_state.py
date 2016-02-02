#Imports
import os
import sys
import random

#Array of countries/States to pick from at random
states = [
"ALABAMA",
"ALASKA",
"ARIZONA",
"ARKANSAS",
"CALIFORNIA",
"COLORADO",
"CONNECTICUT",
"DELAWARE",
"FLORIDA",
"GEORGIA",
"HAWAII",
"IDAHO",
"ILLINOIS",
"INDIANA",
"IOWA",
"KANSAS",
"KENTUCKY",
"LOUISIANA",
"MAINE",
"MARYLAND",
"MASSACHUSETTS",
"MICHIGAN",
"MINNESOTA",
"MISSISSIPPI",
"MISSOURI",
"MONTANA",
"NEBRASKA",
"NEVADA",
"NEW HAMPSHIRE",
"NEW JERSEY",
"NEW MEXICO",
"NEW YORK",
"NORTH CAROLINA",
"NORTH DAKOTA",
"OHIO",
"OKLAHOMA",
"OREGON",
"PENNSYLVANIA",
"RHODE ISLAND",
"SOUTH CAROLINA",
"SOUTH DAKOTA",
"TENNESSEE",
"TEXAS",
"UTAH",
"VERMONT",
"VIRGINIA",
"WASHINGTON",
"WEST VIRGINIA",
"WISCONSIN",
"WYOMING",
"DISTRICT OF COLUMBIA",
"AMERICAN SAMOA",
"GUAM",
"NORTH MARIANA ISLANDS",
"PUERTO RICO",
"US VIRGIN ISLANDS",
]

winning_statements = [
"Congrats!  You're a geographical genius!",
"Well done, Lewis and or Clark!",
"You must be Rand or McNalley, cause you won!",
"We've got ourselves a regular geo expert here.  Congrats!",
"Someone knows their states! Congrats!",
"Well done!",
"Great job!",
"Holy cow!  Great job!",
"Great going!",
]

losing_statements = [
"Sorry, no.",
"This is why your wife prints out directions before you leave the house.",
"From now on, let computers do the navigating.  You focus on the road.",
"Too many guesses, not enough right answers.",
"Now would not be the time to quit your day job to get on Jeabordy!",
"Did you sleep through second grade geography?",
"Yeah, no.",
"Your geographical knowledge is about as limited as my dating knowledge!",
"Why don't you just try the game again and we can forget this happened.",


]

#array of lines for guessing
line_array = []

secret_state_array = []
 
#Counter VAR to keep track of bad Guesses
bad_guesses = 0
game_over = False
max_allowed = 8

#Status var to keep track whether game is won or not
game_won = False

#Secret State Array (to compare with display_array)
secret_state_array = []
#clear function
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
def begin_game():
    clear()
    #choose secret state        
    secret_state = random.choice(states)
    #populate line array
    for letter in secret_state:
        if letter == " ":
            line_array.append(" ")
        else:
            line_array.append("_")
    
    for letter in secret_state:
        secret_state_array.append(letter)
    
    free_letter = random.choice(secret_state_array)
    
    for index, letter in enumerate(secret_state_array):
        if free_letter == letter:
            letter_index = index
            line_array[letter_index] = letter
    

def pretty_word_display():
    for letter in line_array:
        print(letter, end=" ")
        

  
    
#start game 
begin_game()

#main game loop
while game_won != True and bad_guesses < max_allowed:
    clear()
    #Start Game Loop
    print("Welcome to the secret state game!  See if you can guess the state!")
    
    pretty_word_display()
    #Take Guess
    print("\n")
    guesses_left = max_allowed - bad_guesses
    print("You have {} guesses left.".format(guesses_left))
    
    user_guess = input("Guess a letter!> ")
   
    #Compare Guess
    if user_guess.upper() in secret_state_array:
        for index, letter in enumerate(secret_state_array):
            if user_guess.upper() == letter:
                letter_index = index
                line_array[letter_index] = letter
    elif user_guess.upper() not in secret_state_array:
        bad_guesses += 1
    
    #See if User won game    
        
    if line_array == secret_state_array:
        game_won = True
    else:
        game_won = False

###### End Of Game ##############


clear()
result_display_array = []

if game_won == True:
    print("You Win! " + random.choice(winning_statements))
elif game_won == False:
    print("You Lose! " + random.choice(losing_statements))

print("The secret state was: \n")
for letter in secret_state_array:
        print(letter, end="")
        
print("\n")
   
    
    
    
    
    



        
    
