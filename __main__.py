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
selecword = random.choice(collection)
# get the length of the selected word
length = len(selecword)

# this prints the list view of the words letters separated
nonrep = list(dict.fromkeys(selecword))
nonrep_length = len(nonrep)

# this stores the letters that have been guessed
wrong = []
correct = []
attempted = []

# this stores the number of correct guesses
correct_count = 0

# this counts down the user's lives
remaining = 10

# This controls the game loop
playing = True



# --- Start of the game ---
cprint(figlet_format('Hangman', font='standard'))
print("Version 1.2")
print(selecword)
print("")
time.sleep(1)
play = input("Would you like to play? (y/n): ")
if play == "y":
    time.sleep(1)
    print(" ")
    print("Welcome to Hangman! Try and guess the word before your time runs out!")
    time.sleep(2)
    print(" ")
    print("To end the game at anytime, type 'quit'")
    time.sleep(2)
    print(" ")
    print("A word has been selected!")
    print(" ")

    # this prints the markers for the word
    time.sleep(1.5)
    for j in range(length):
        print("_ ", end=" ")
    print()

    # this makes it repeat until you run out of tries or win
    while playing == True:
        print(" ")
        time.sleep(1)
        guess = input("Enter your guess: ")
        guesslen = len(guess)

        if guess in attempted:
            time.sleep(0.65)
            print("ERROR: You've already guessed this! Try again")
        else:
            if guesslen > 1:
                if guess == selecword:
                    time.sleep(1)
                    print(" ")
                    print(" ")
                    cprint(figlet_format('You Win!', font='standard'))
                    time.sleep(1)
                    print("Your person survived!")
                    print(" ")
                    time.sleep(5)
                    playing = False
                else:
                    if remaining == 1:
                        time.sleep(1)
                        cprint(figlet_format('Game Over', font='standard'))
                        time.sleep(0.65)
                        print("You ran out of guesses :(")
                        time.sleep(0.5)
                        print("The word was:", selecword)
                        time.sleep(1)
                        print("Reload game to try again")
                        time.sleep(5)
                        playing = False
                    else:
                        remaining=remaining-1
                        time.sleep(0.65)
                        print(" ")
                        print("INCORRECT")
                        print(" ")
                        time.sleep(0.65)
                        print("Correct letters:", correct)
                        time.sleep(0.5)
                        print("Incorrect letters:", wrong)
                        time.sleep(1)
                        print("You have", remaining, "/ 10 lives remining")
                        print(" ")
                        print(" ")
            elif guess in nonrep:
                correct.append(guess)
                attempted.append(guess)
                time.sleep(0.65)
                print(" ")
                print("CORRECT")
                time.sleep(1)
                print(" ")
                print("You have", nonrep_length - correct_count, "unguessed letters remaining")
                time.sleep(1)
                print("Correct letters:", correct)
                time.sleep(1)
                print("Incorrect letters:", wrong)
                time.sleep(1)
                print("You still have", remaining, "/ 10 lives remining")
                print(" ")
                correct_count += 1
                if correct_count == nonrep_length:
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
            elif guess == "quit":
                time.sleep(1)
                cprint(figlet_format('Game Over', font='standard'))
                time.sleep(0.65)
                print("The word was:", selecword)
                time.sleep(0.5)
                print("Better luck next time :/")
                time.sleep(2)
                playing = False
            elif guess is not nonrep:
                wrong.append(guess)
                attempted.append(guess)
                if remaining == 1:
                    time.sleep(1)
                    cprint(figlet_format('Game Over', font='standard'))
                    time.sleep(0.65)
                    print("You ran out of guesses :(")
                    time.sleep(0.5)
                    print("The word was:", selecword)
                    time.sleep(1)
                    print("Reload game to try again")
                    time.sleep(5)
                    playing = False
                else:
                    remaining=remaining-1
                    time.sleep(0.65)
                    print(" ")
                    print("INCORRECT")
                    print(" ")
                    time.sleep(1)
                    print("You have", nonrep_length - correct_count, "unguessed letters remaining")
                    time.sleep(0.65)
                    print("Correct letters:", correct)
                    time.sleep(0.5)
                    print("Incorrect letters:", wrong)
                    time.sleep(1)
                    print("You have", remaining, "/ 10 lives remining")
                    print(" ")
                    print(" ")
elif play == "n":
    time.sleep(0.5)
    print("Closing Game...")
    time.sleep(2)
    cprint(figlet_format('Goodbye', font='standard'))
else:
    print(" ")
    time.sleep(1)
    print("ERROR: Input not recognised")
    time.sleep(1)
    print("The game will now terminate. Reboot the game to try again")
    time.sleep(2)
