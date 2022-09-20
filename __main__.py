import random
import sys
import time
from words import collection


#pyfiglet setup
from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint
from pyfiglet import figlet_format

selecword = random.choice(collection)
length = len(selecword)

# this prints the list view of the words letters separated
letters = list(selecword)
nonrep = list(dict.fromkeys(letters))
nonrep_length = len(nonrep)

# this prints the comp view of the letter count

wrong = []
correct = []
attempted = []
tick = nonrep_length
correct_count = 0

print(" ")
print(" ")
print(" ")
time.sleep(random.randint(0, 1))
cprint(figlet_format('Hangman', font='standard'))
time.sleep(1)
play = input("Would you like to play? (y/n): ")

if play == "y":
    print(" ")
    print(" ")
    time.sleep(1)
    print("Welcome to Hangman! Try and guess the word before your time runs out!")
    time.sleep(3)
    print(" ")
    print("(_) \n"
          "\|/ \n"
          " | \n"
          "/ \ \n")
    time.sleep(0.85)
    char_name = input("This is your buddy, what would you like to name him?: ")
    print(" ")
    time.sleep(1)
    print("(_) 'Hi! I'm", char_name,"!'" "\n"
          "\|/ \n"
          " | \n"
          "/ \ \n")
    time.sleep(1.7)
    print("Selecting a word...")
    time.sleep(1)
    print("...")
    time.sleep(0.8)
    print("...")
    time.sleep(1.2)
    print("...")
    time.sleep(1.6)
    print("A word has been selected!")
    print(" ")
    # this prints the markers for the word
    for j in range(length):
        print("_ ", end="")
    print()
    # this counts down your persons lives
    remaining = 10

    playing = True

    # this makes it repeat until you run out of tries or win
    while playing == True:
        time.sleep(0.6)
        guess = input("Enter your guess: ")
        time.sleep(0.4)
        if guess in attempted:
            print("ERROR: You've already guessed this! Try again")
        else:
            if guess in nonrep:
                correct.append(guess)
                attempted.append(guess)
                print(" ")
                print("CORRECT")
                print(" ")
                print("You have", tick - correct_count, "unguessed letters remaining")
                print("Correct letters:", correct)
                print("Incorrect letters:", wrong)
                print(" ")
                print(" ")
                correct_count += 1
                if correct_count == tick:
                    print(" ")
                    print(" ")
                    print(" ")
                    print(" ")
                    cprint(figlet_format('You Win!', font='standard'))
                    print("Your person survived!")
                    time.sleep(5)
                    playing = False
            elif guess == "give up":
                cprint(figlet_format('Game Over', font='standard'))
                print("The word was:", selecword)
                print("Better luck next time :/")
                time.sleep(5)
                playing = False
            else:
                wrong.append(guess)
                attempted.append(guess)
                print(" ")
                print("INCORRECT")
                print(" ")
                print("You have", tick - correct_count, "unguessed letters remaining")
                print("Correct letters:", correct)
                print("Incorrect letters:", wrong)
                remaining=remaining-1
                print(char_name, "has", remaining, " lives left")
                print(" ")
                print(" ")
    if remaining == 0:
        cprint(figlet_format('Game Over', font='standard'))
        print("You ran out of guesses :(")
        print("The word was:", selecword)
        print("Reload game to try again")
        time.sleep(5)
        playing = False

elif play == "n":
    time.sleep(0.5)
    print("Closing Game...")
    time.sleep(2)
    cprint(figlet_format('Goodbye', font='standard'))
else:
    print(" ")
    print(" ")
    print("ERROR: Input not recognised")
    print("The game will now terminate. Reboot the game to try again")
    time.sleep(5)
