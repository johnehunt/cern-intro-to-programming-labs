import random

# Initialise the number to be guessed
number_to_guess = random.randint(1, 10)

# Initialise the number of tries the player has made
count_number_of_tries = 1


def print_welcome_message():
    print('Welcome to the number guess game')


def get_user_guess(prompt):
    return int(input(prompt))


def print_end_of_game_message():
    print('Game Over')


print_welcome_message()

# Obtain their initial guess
guess = get_user_guess('Please guess a number between 1 and 10: ')
while number_to_guess != guess:
    print('Sorry wrong number')

    # Check to see they have not exceeded the maximum
    # number of attempts if so break out of loop otherwise
    # give the user come feedback
    if count_number_of_tries == 4:
        break
    elif guess < number_to_guess:
        print('Your guess was lower than the number')
    else:
        print('Your guess was higher than the number')

    # Obtain their next guess and increment number of attempts
    guess = get_user_guess('Please guess again: ')
    count_number_of_tries += 1

# Check to see if they did guess the correct number
if number_to_guess == guess:
    print('Well done you won!')
    print('You took', count_number_of_tries, 'goes to complete the game')
else:
    print("Sorry - you loose")
    print('The number you needed to guess was',
          number_to_guess)

print_end_of_game_message()
