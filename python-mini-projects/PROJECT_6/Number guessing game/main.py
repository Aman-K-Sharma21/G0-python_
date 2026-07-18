from random import randint #importing random module to let the computer select the number between the given range

def play_round():
    
    actual_number = randint(1, 100)
    
    print("===" * 30)
    print("Difficulty modes: Easy (10 guesses), Medium (6 guesses), Hard (3 guesses)")
    print("===" * 30)
    
    level = input("Choose a difficulty level (Easy, Medium, Hard): ").lower()
    
    
    difficulty_settings = {"easy": 10, "medium": 6, "hard": 3}
    guesses_left = difficulty_settings.get(level, 3) # Defaults to hard if input is invalid
    
    attempts_used = 0

    while guesses_left > 0:
        
        try:
            user_guess = int(input(f"\n[{guesses_left} left] Enter your guess (1-100): "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        guesses_left -= 1
        attempts_used += 1

        if user_guess > actual_number:
            print("Too high")
        elif user_guess < actual_number:
            print("Too Low")
        else:
            print(f"Correct! You guessed it right in {attempts_used} attempts.")
            return  # Exit the round function immediately upon winning

    
    print(f"\nYou ran out of guesses! The number was: {actual_number}.")

def start_game():
    while True:
        print("\n" + "===" * 20)
        print("Welcome to Number Guessing Game (CLI)")
        print("===" * 20)
        print("1. Play")
        print("2. Exit")

        choice = input("Enter 1 to play and 2 to exit: ")
        
        if choice == "1":
            play_round()
           
            wannaplay = input("\nDo you want to play another round? (yes/no): ").lower()
            if wannaplay != "yes":
                print("Thank you for playing!")
                break
        elif choice == "2":
            print("Thank you!")
            break
        else:
            print("Please enter a valid input (1 or 2).")

# Start the application
start_game()
