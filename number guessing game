import random

MIN_NUMBER = 1
MAX_NUMBER = 100

# generate a random number between 1 and 100
def generate_secret_number():
    return random.randint(MIN_NUMBER, MAX_NUMBER)

# read the user's guess
def get_user_guess():
    while True:
        try:
            guess = int(input("Enter your guess: "))
            return guess
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# compare guess with secret number
def check_guess(guess, secret_number):
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        return True

# Initialize the game and number of attempts
def play_game():
    secret_number = generate_secret_number()
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between {MIN_NUMBER} and {MAX_NUMBER}. Can you guess it?")

    while True:
        guess = get_user_guess()
        attempts += 1

        if check_guess(guess, secret_number):
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

    print("Thank you for playing the Number Guessing Game. Goodbye! :)")

play_game()
