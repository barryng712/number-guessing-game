import random
import time

MIN = 1
MAX = 100
LEVELS = {1: "Easy", 2: "Medium", 3: "Hard"}
CHANCES = {1: 10, 2: 5, 3: 3}

def display_welcome_msg():
    print("Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between {MIN} and {MAX}.")
    print("The number of chances depends on the difficulty level you choose.\n")

def choose_difficulty_level():
    print("Please select the difficulty level:\n")
    for level, name in LEVELS.items():
        print(f"{level}. {name} ({CHANCES[level]} chances)")

    while True:
        try:
            choice = int(input("Enter your choice: "))
            if choice in LEVELS:
                print(f"\nGreat! You have selected the {LEVELS[choice]} difficulty level.")
                print("Let's start the game!")
                return choice
            print("Invalid choice. Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_valid_guess():
    while True:
        try:
            guess = int(input("Enter your guess: "))
            if MIN <= guess <= MAX:
                return guess
            print(f"Please enter a number between {MIN} and {MAX}")
        except ValueError:
            print("Invalid input. Please enter a number.")

def play(choice, random_guess):
    start = time.time()
    chances_left = CHANCES[choice]
    attempts = 0
    while chances_left > 0:
        print(f"\nChances left: {chances_left}")
        guess = get_valid_guess()
        attempts += 1
        chances_left -= 1
        if guess != random_guess:
            if guess < random_guess:
                print(f"Incorrect! The number is greater than {guess}")
            else:
                print(f"Incorrect! The number is less than {guess}")
        else:
            stop = time.time()
            print(f"Congratulations! You guess the correct number in {attempts} attempts.")
            print(f"Total time played: {stop - start:.2f} seconds")
            return True
    if chances_left == 0:
        print(f"\nNo more chances left. The correct number should be {random_guess} You lose!")
        return False


def main():
    while True:
        display_welcome_msg() 
        choice = choose_difficulty_level()
        random_guess = random.randint(MIN, MAX)
        play(choice, random_guess)
        play_again = input("\nDo you want to play again? (yes/no): ").lower().strip()
        if play_again not in ['yes', 'y']:
            print("Thanks for playing! Goodbye")
            break

if __name__ == "__main__":
    main()