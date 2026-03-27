import random

# Word list
wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 
             'interference', 'complete', 'share', 'credit card', 'rush', 'south']

# Hangman stages (6 wrong guesses max)
HANGMAN_STAGES = [
    """
       --------
       |      |
       |      
       |    
       |      
       |     
       -
    """,
    """
       --------
       |      |
       |      O
       |    
       |      
       |     
       -
    """,
    """
       --------
       |      |
       |      O
       |      |
       |      
       |     
       -
    """,
    """
       --------
       |      |
       |      O
       |     /|
       |      
       |     
       -
    """,
    """
       --------
       |      |
       |      O
       |     /|\\
       |      
       |     
       -
    """,
    """
       --------
       |      |
       |      O
       |     /|\\
       |     / 
       |     
       -
    """,
    """
       --------
       |      |
       |      O
       |     /|\\
       |     / \\
       |     
       -
    """
]

def display_hangman(wrong_guesses):
    """Display the current hangman stage based on wrong guesses."""
    print(HANGMAN_STAGES[wrong_guesses])

def display_word(word, guessed_letters):
    """Display the word with guessed letters revealed and others as stars."""
    display = ""
    for char in word:
        if char == " ":
            display += "  "  # Show spaces for multi-word phrases
        elif char in guessed_letters:
            display += char + " "
        else:
            display += "* "
    return display.strip()

def get_user_guess(guessed_letters):
    """Get a valid letter guess from the user."""
    while True:
        guess = input("Guess a letter: ").lower()
        
        # Validate input
        if len(guess) != 1:
            print("Please enter exactly one letter.")
        elif not guess.isalpha():
            print("Please enter a letter (a-z).")
        elif guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.")
        else:
            return guess

def check_win(word, guessed_letters):
    """Check if all letters in the word have been guessed."""
    for char in word:
        if char != " " and char not in guessed_letters:
            return False
    return True

def play_hangman():
    """Main game function."""
    # Choose random word
    word = random.choice(wordslist)
    
    # Game state
    guessed_letters = set()
    wrong_guesses = 0
    max_wrong = 6
    
    print("=" * 50)
    print("       WELCOME TO HANGMAN!")
    print("=" * 50)
    print(f"The word has {len(word.replace(' ', ''))} letters.")
    print(f"You can make {max_wrong} wrong guesses before game over.")
    print("Let's begin!\n")
    
    # Main game loop
    while wrong_guesses < max_wrong:
        # Display current state
        display_hangman(wrong_guesses)
        print(f"\nWord: {display_word(word, guessed_letters)}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
        print(f"Wrong guesses: {wrong_guesses}/{max_wrong}")
        
        # Get player guess
        guess = get_user_guess(guessed_letters)
        guessed_letters.add(guess)
        
        # Check if guess is in word
        if guess in word:
            print(f"\n✅ Good job! '{guess}' is in the word.")
            
            # Check if player won
            if check_win(word, guessed_letters):
                print(f"\nWord: {display_word(word, guessed_letters)}")
                print("\n🎉 Congratulations! You guessed the word! 🎉")
                print(f"The word was: '{word}'")
                return
        else:
            print(f"\n❌ Sorry, '{guess}' is not in the word.")
            wrong_guesses += 1
    
    # Game over - player lost
    display_hangman(wrong_guesses)
    print(f"\n💀 GAME OVER! You ran out of guesses. 💀")
    print(f"The word was: '{word}'")

def main():
    """Main program loop with option to play again."""
    while True:
        play_hangman()
        
        play_again = input("\nWould you like to play again? (yes/no): ").lower()
        if play_again not in ['yes', 'y']:
            print("Thanks for playing! Goodbye!")
            break

# Start the game
if __name__ == "__main__":
    main()