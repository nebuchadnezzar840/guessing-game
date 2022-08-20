from Colours import *
from random import randint

# Welcome Screen msg
def welcome_screen():
    print(BLUE, '***Welcome To your world of guessing***')
    user_input = int(input('Choose your Level\n'
                       '1. Normal (1-50)\n'
                       '2. Intermediate (1-200)\n'
                       '3. Hard (1-500)\n'
                       '4. Exit Application\n\n'
                       'Enter Request : '))
    guess_range = user_option(user_input)
    if guess_range != 0:
        welcome_screen()
    generate_random_number(guess_range)
# calling a function and passing user_input to it

# user's option
def user_option(user_input):
    guess_range =0
    if user_input == 1:
        guess_range=50
    elif user_input == 2:
        guess_range=200
    elif user_input == 3:
        guess_range=500
    elif user_input == 4:
        print(WHITE, '**** Thanks for using our app, Hope to see you again ****')
        exit(1)
    else:
        print(RED, 'Invalid Request, Try Again!!!')

def generate_random_number(guess_range):
    #Generate random number between certain range
    generate_number = randint(1,guess_range)

    #user chances
    user_chances = 4

    #accepting the user input and validating, if it matches the generated number
    for i in range(4):
        user_guess = int(input('Provide your guess number: '))

        if user_guess == generate_number:
            print(GREEN,f'Hurray!!!, Your guess is correct!')
            break
        elif user_guess > generate_number:
            print(YELLOW, 'Your Guess is too high, Try Again.')
            user_chances -= 1
        elif user_guess < generate_number:
            print(YELLOW,'Your Guess is too low, Try Again.')

        #reduce user chances and prompt user chances left
        user_chances -=1
        print(f'Number of chances Left is {user_chances}')

    #inform user the correct number
    if user_chances == 0:
        print(RED,f'Sorry The correct guess is {generate_number}')


welcome_screen()