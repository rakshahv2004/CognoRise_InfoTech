import random

def get_random_word():
    """Returns a random word from the predefined word list."""
    words = ["python", "hangman", "programming", "challenge", "developer", "debugging", "algorithm"]
    return random.choice(words)

def display_hangman(attempts):
    """Displays the hangman figure based on incorrect guesses."""
    stages = [
        """
           +---+
               |
               |
               |
              ===
        """,
        """
           +---+
           O   |
               |
               |
              ===
        """,
        """
           +---+
           O   |
           |   |
               |
              ===
        """,
        """
           +---+
           O   |
          /|   |
               |
              ===
        """,
        """
           +---+
           O   |
          /|\  |
               |
              ===
        """,
        """
           +---+
           O   |
          /|\  |
          /    |
              ===
        """,
        """
           +---+
           O   |
          /|\  |
          / \  |
              ===
        """,
    ]
    return stages[attempts]

def play_hangman():
    """Main function to play the Hangman game."""
    print("Welcome to Hangman!")

    while True:
        word = get_random_word()
        guessed_word = ["_" for _ in word]
        guessed_letters = set()
        attempts = 0
        max_attempts = 6

        while attempts < max_attempts and "_" in guessed_word:
            print(display_hangman(attempts))
            print("Word: " + " ".join(guessed_word))
            print(f"Guessed Letters: {', '.join(sorted(guessed_letters))}")

            guess = input("Guess a letter: ").lower()

            if len(guess) != 1 or not guess.isalpha():
                print("Invalid input. Please enter a single letter.")
                continue

            if guess in guessed_letters:
                print("You already guessed that letter. Try another.")
                continue

            guessed_letters.add(guess)

            if guess in word:
                print(f"Good job! {guess} is in the word.")
                for idx, letter in enumerate(word):
                    if letter == guess:
                        guessed_word[idx] = guess
            else:
                print(f"Wrong! {guess} is not in the word.")
                attempts += 1

        print(display_hangman(attempts))
        if "_" not in guessed_word:
            print(f"Congratulations! You guessed the word: {word}")
        else:
            print(f"Game over! The word was: {word}")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing Hangman! Goodbye!")
            break

if __name__ == "__main__":
    play_hangman()
