import random
import sys
import time
from words import collection

#pyfiglet setup
from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint
from pyfiglet import figlet_format

# randomly select a word from the collection
full_word = random.choice(collection)
# get the length of the selected word
full_word_length = len(full_word)

# this prints the list view of the words letters separated
single_letter_word = list(dict.fromkeys(full_word))
single_letter_word_length = len(single_letter_word)

# game info store
wrong = []
correct = []
attempted = []
correct_count = 0
lives = 10
playing = True
term = 0

def drawing():
    if lives == 9:
         print("|")
         print("|")
         print("|")
         print("|")
         print("|")
         print("|")
         print("|")
         print("|")
         print("|")
         print("|")
         print("|")
    elif lives == 8:
        print(" ------------------")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
    elif lives == 7:
        print("-------------------")
        print("|                 |")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
    elif lives == 6:
        print("-------------------")
        print("|                 |")
        print("|                (_)")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
    elif lives == 5:
        print("-------------------")
        print("|                 |")
        print("|                (_)")
        print("|                 |")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
    elif lives == 4:
        print("-------------------")
        print("|                 |")
        print("|                (_)")
        print("|                \|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
    elif lives == 3:
        print("-------------------")
        print("|                 |")
        print("|                (_)")
        print("|                \|/")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
    elif lives == 2:
        print("-------------------")
        print("|                 |")
        print("|                (_)")
        print("|                \|/")
        print("|                 |")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
    elif lives == 1:
        print("-------------------")
        print("|                 |")
        print("|                (_)")
        print("|                \|/")
        print("|                 |")
        print("|                /  ")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")

def display_stats():
    
    word_list = [letter if letter in correct else '_' for letter in full_word]
    print('Current word: ', ' '.join(word_list))
    time.sleep(0.5)
    print("Incorrect letters:", ", ".join(wrong))
    time.sleep(0.75)
    if lives < 10:
        print(" ")
        drawing()
        print(" ")
        time.sleep(0.5)

def winner():
    global playing
    time.sleep(1)
    print(" ")
    print(" ")
    # displays "You Win!" graphic
    cprint(figlet_format('You Win!', font='standard'))
    time.sleep(1)
    print("Your person survived!")
    print(" ")
    time.sleep(5)
    # ends the game loop
    playing = False

def game_over():
    global playing, term
    time.sleep(1)
    if term == 1:
        print("-------------------")
        print("|                 |")
        print("|                ( )")
        print("|                \|/")
        print("|                 |")
        print("|                / \ ")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
    cprint(figlet_format('Game Over', font='standard'))
    time.sleep(0.65)
    print("The word was:", full_word)
    time.sleep(1)
    print(" ")
    print("Reload the game to try again")
    print(" ")
    time.sleep(5)
    playing = False

def get_lives():
    global term
    global lives, playing
    if lives == 1:
        term = 1
        game_over()
    else:
        lives = lives-1
        time.sleep(0.65)
        print(" ")
        print("INCORRECT")
        print(" ")
        time.sleep(1)
        display_stats()



# ------------------------------------------- START OF THE GAME ------------------------------------------- #

# this displays the title
cprint(figlet_format('Hangman', font='standard'))

# this displays the version number
print("Version 2.0")
print("")
time.sleep(1)

# asks user if they would like to play
play = input("Would you like to play? (y/n): ")

if play == "y":
    time.sleep(1)
    print(" ")
    # ----------- game intro
    print("Welcome to Hangman! Try and guess the word before your time runs out!")
    time.sleep(2)
    print("To end the game at anytime, type 'quit'")
    time.sleep(2)
    print(" ")
    word_list = ['_' for letter in full_word]
    print('Current word: ', ' '.join(word_list))
    print(" ")
    time.sleep(1.5)
# while the user has enough lives this loop runs
    while playing == True:
        print(" ")
        time.sleep(1)
        
        # asks the user to guess a letter
        guess = input("Enter your guess: ")
        
        # checks the length of the guess
        guesslen = len(guess)
        
        # if the guess has already been attempted then the user will be informed and it will be skipped
        if guess in attempted:
            time.sleep(0.65)
            print("ERROR: You've already guessed this! Try again")

        else:

            # if the users wants to quit the game then this runs
            if guess == "quit":
                game_over()
            
            # if the guess is more than one letter long then it will be considered as a word and this will run
            elif guesslen > 1:
                
                # if the word guessed is correct then this runs
                if guess == full_word:
                    winner()
                
                # if the word guessed is incorrect then this runs
                else:
                    get_lives()
            
            # if the guess is one letter long and correct then this rusn
            elif guess in single_letter_word:
                correct.append(guess)
                attempted.append(guess)
                time.sleep(0.45)
                print(" ")
                print("CORRECT")
                time.sleep(1)
                print(" ")
                display_stats()
                correct_count += 1

                # if the user has guessed all the letters correctly then this runs
                if correct_count == single_letter_word_length:
                    time.sleep(1)
                    print(" ")
                    print(" ")
                    print(" ")
                    print(" ")
                    cprint(figlet_format('You Win!', font='standard'))
                    time.sleep(1)
                    print("Your person survived!")
                    time.sleep(5)
                    playing = False
            
            # if the guess is one letter long and incorrect then this runs
            elif guess is not single_letter_word:
                wrong.append(guess)
                attempted.append(guess)
                get_lives()

# if the user does not want to play then this runs
elif play == "n":
    time.sleep(0.5)
    print("Closing Game...")
    time.sleep(2)
    cprint(figlet_format('Goodbye', font='standard'))

# if the users choice is not valid then this runs
else:
    print(" ")
    time.sleep(1)
    print("ERROR: Input not recognised")
    time.sleep(1)
    print("The game will now terminate. Reboot the game to try again")
    time.sleep(2)