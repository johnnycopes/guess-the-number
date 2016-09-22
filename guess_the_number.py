# Import 'random' module
import random
# Set playing to True while playing the game
playing = True
# Set variable with text to prompt user input
prompt = "> "

# Define a function asking if the user wants
# to play again
def ask_to_play_again():
    valid_answer = False
    while valid_answer == False:
        play_again = raw_input("Enter 'Y' or 'N' : ")
        play_again = play_again.upper()
        if play_again == "Y":
            valid_answer = True
            print "Great! Resetting..."
        elif play_again == "N":
            valid_answer = True
            print "OK. Bye!"
            global playing
            playing = False

# Game logic

while playing == True:
    # Generate random number and store it
    target_number = random.randint(1, 10)
    # Store number of remaining available user guesses
    num_guesses = 5
    # Prompt the user to enter a guess and store it in a variable
    print """
Welcome to the guessing game!
I'm thinking of a number between 1 and 10.
You have 5 guesses. Can you guess what it is?
    """
    
    while num_guesses > 0:

        # Print number of guesses remaining and subtract 1
        if num_guesses == 1:
            print "You have %d guess remaining." % num_guesses
        elif num_guesses < 5:
            print "You have %d guesses remaining." % num_guesses
        num_guesses -= 1
        # Ask the user for a guess and store it
        user_guess = int(raw_input(prompt))

        # Give user feedback on their guess. If they have no
        # guesses remaining, don't tell them to try again
        if user_guess == target_number:
            num_guesses = -1
            print "Congratulations, you win!"
        elif user_guess < target_number and user_guess > 0:
            if num_guesses >= 1:
                print "Too low! Try again."
            else:
                print "Too low!"
        elif user_guess > target_number and user_guess < 11:
            if num_guesses >= 1:
                print "Too high! Try again."
            else:
                print "Too high!"
        else:
            if num_guesses >= 1:
                print "Out of range! Guess again, \
this time between 1 and 10."
            else:
                print "Out of range!"

    # If user ran out of guesses, tell them
    if num_guesses == 0:
        print "You're out of guesses! Better luck next time."

    # Ask the user if they want to play again
    print "Want to play again?"
    ask_to_play_again()
