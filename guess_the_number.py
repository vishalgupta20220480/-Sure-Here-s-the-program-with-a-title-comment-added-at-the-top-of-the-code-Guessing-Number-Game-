# ----------------- Guessing Number Game ----------------------------
# This program generates a random number between 1 and 100.
# The user has to guess the number. The program will guide the user if the guess is too high or too low.
# The game continues until the user guesses the correct number, and it tracks the number of attempts.
import random

def guess_the_number():
    print("Welcome to the Guess the Number Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    # Generate a random number
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed = False
    
    while not guessed:
        try:
            # Take user input
            user_guess = int(input("Enter your guess: "))
            attempts += 1
            
            # Check the user's guess
            if user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                guessed = True
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    guess_the_number()
