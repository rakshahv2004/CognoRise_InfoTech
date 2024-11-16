import random

def display_instructions():
    print("\nWelcome to Rock, Paper, Scissors!")
    print("Instructions:")
    print("1. Enter 'rock', 'paper', or 'scissors' to make your choice.")
    print("2. The computer will make its choice randomly.")
    print("3. The winner is determined as follows:")
    print("   - Rock beats Scissors")
    print("   - Scissors beats Paper")
    print("   - Paper beats Rock")
    print("4. Type 'exit' to quit the game at any time.\n")

def get_user_choice():
    choice = input("Enter your choice (rock, paper, scissors): ").lower()
    while choice not in ['rock', 'paper', 'scissors', 'exit']:
        print("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.")
        choice = input("Enter your choice: ").lower()
    return choice

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "win"
    else:
        return "lose"

def display_results(user_choice, computer_choice, outcome):
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    if outcome == "tie":
        print("It's a tie!")
    elif outcome == "win":
        print("You win!")
    else:
        print("You lose!")

def main():
    user_score = 0
    computer_score = 0

    display_instructions()

    while True:
        user_choice = get_user_choice()
        if user_choice == 'exit':
            print("\nThanks for playing!")
            print(f"Final Score: You {user_score} - {computer_score} Computer")
            break

        computer_choice = get_computer_choice()
        outcome = determine_winner(user_choice, computer_choice)
        
        if outcome == "win":
            user_score += 1
        elif outcome == "lose":
            computer_score += 1

        display_results(user_choice, computer_choice, outcome)
        print(f"Score: You {user_score} - {computer_score} Computer\n")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("\nThanks for playing!")
            print(f"Final Score: You {user_score} - {computer_score} Computer")
            break

if __name__ == "__main__":
    main()
