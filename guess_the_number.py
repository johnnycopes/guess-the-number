# Import 'random' module and generate random number

from random import randint
target_number = randint(1, 10)


# Set variable with text indicating when user needs to write

prompt = "> "


# Prompt the user to enter a guess and store it

print """
Welcome to the guessing game!
I'm thinking of a number between 1 and 10.
Can you guess what it is?
"""

user_guess = int(raw_input(prompt))


# Declare function that prints appropriate instructions and
# stores the user's next guess

def instructions(message):
    global user_guess
    print message
    user_guess = int(raw_input(prompt))


# Set variables storing different instructions for logic

too_low = "Too low! Try again."
too_high = "Too high! Try again."
out_of_range = "Out of range! Guess again, \
this time between 1 and 10."


# Game logic

while user_guess != target_number:
    if user_guess < target_number and user_guess > 0:
        instructions(too_low)
    elif user_guess > target_number and user_guess < 11:
        instructions(too_high)
    else:
        instructions(out_of_range)

print "Congratulations, you win!"
