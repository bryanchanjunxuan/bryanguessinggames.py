import random

def display_high_score(high_score):
    """Display the current high score."""
    if high_score is None:
        print("No high score yet.")
    else:
        print(f"Current high score: {high_score} attempts")

def get_guess():
    """Prompt the player to input their guess and handle invalid inputs."""
    while True:
        try:
            return input("Enter your guess: ").strip()
        except ValueError:
            print("Invalid input. Please enter a valid string.")

def play_round(favorite_games):
    """Play a single round of the guessing game."""
    # Randomly select a game from the list
    target_game = random.choice(favorite_games).lower()
    
    print("\nGuess my favorite game from the list below:")
    print(", ".join(favorite_games))
    
    attempts = 0
    
    while True:
        guess = get_guess().lower()
        attempts += 1
        
        if guess == target_game:
            print(f"Correct! You guessed the game in {attempts} attempts.")
            return attempts
        else:
            print("Wrong guess. Try again.")

def guessing_game():
    """Main function to run the guessing game."""
    favorite_games = [
        "The Legend of Zelda: Breath of the Wild",
        "Minecraft",
        "The Witcher 3: Wild Hunt",
        "Dark Souls",
        "Among Us",
        "Hades",
        "Animal Crossing: New Horizons",
        "Stardew Valley",
        "Fortnite",
        "Overwatch"
    ]
    
    high_score = None
    
    print("Welcome to the Favorite Game Guessing Game!")
    
    while True:
        attempts = play_round(favorite_games)
        
        # Update high score
        if high_score is None or attempts < high_score:
            high_score = attempts
        
        display_high_score(high_score)
        
        play_again = input("Do you want to play another round? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    guessing_game()

