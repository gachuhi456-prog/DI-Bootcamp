import random

# ============================================
# Part I - Game Logic (game.py)
# ============================================

class Game:
    """
    Handles all game logic for Rock Paper Scissors.
    No print statements in methods - returns values only.
    """
    
    CHOICES = ["rock", "paper", "scissors"]
    
    # Winning combinations: key beats value
    WIN_RULES = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }
    
    def get_user_item(self):
        """
        Get and validate user's choice.
        Returns: "rock", "paper", or "scissors"
        """
        while True:
            user_input = input("Select (rock/paper/scissors): ").lower().strip()
            
            if user_input in self.CHOICES:
                return user_input
            else:
                print("Invalid choice! Please enter 'rock', 'paper', or 'scissors'.")
    
    def get_computer_item(self):
        """
        Randomly select computer's choice.
        Returns: "rock", "paper", or "scissors"
        """
        return random.choice(self.CHOICES)
    
    def get_game_result(self, user_item, computer_item):
        """
        Determine game result based on choices.
        Returns: "win", "draw", or "loss"
        """
        if user_item == computer_item:
            return "draw"
        elif self.WIN_RULES[user_item] == computer_item:
            return "win"
        else:
            return "loss"
    
    def play(self):
        """
        Execute one round of the game.
        Returns: result string ("win", "draw", or "loss")
        """
        # Get choices
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        
        # Determine result
        result = self.get_game_result(user_item, computer_item)
        
        # Display outcome
        print(f"\nYou chose: {user_item}")
        print(f"Computer chose: {computer_item}")
        
        if result == "win":
            print("🎉 You WIN!")
        elif result == "loss":
            print("😞 You LOSE!")
        else:
            print("🤝 It's a DRAW!")
        
        return result


# ============================================
# Part II - UI and Menu (rock-paper-scissors.py)
# ============================================

def get_user_menu_choice():
    """
    Display menu and get user choice.
    Returns: "play", "scores", or "quit"
    """
    print("\n" + "=" * 40)
    print("       MAIN MENU")
    print("=" * 40)
    print("1. Play a new game")
    print("2. Show scores")
    print("3. Quit")
    print("=" * 40)
    
    while True:
        choice = input("Enter your choice (1/2/3): ").strip()
        
        if choice == "1":
            return "play"
        elif choice == "2":
            return "scores"
        elif choice == "3":
            return "quit"
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")


def print_results(results):
    """
    Display game results summary.
    Args: results dictionary with win/loss/draw counts
    """
    print("\n" + "=" * 40)
    print("       GAME SUMMARY")
    print("=" * 40)
    print(f"🏆 Wins:   {results.get('win', 0)}")
    print(f"💔 Losses: {results.get('loss', 0)}")
    print(f"🤝 Draws:  {results.get('draw', 0)}")
    print("=" * 40)
    
    total_games = sum(results.values())
    if total_games > 0:
        win_rate = (results.get('win', 0) / total_games) * 100
        print(f"Total games played: {total_games}")
        print(f"Win rate: {win_rate:.1f}%")
    
    print("\nThank you for playing Rock Paper Scissors!")
    print("Goodbye! 👋")


def main():
    """
    Main program loop.
    """
    # Initialize results dictionary
    results = {"win": 0, "loss": 0, "draw": 0}
    
    print("=" * 40)
    print("  ROCK PAPER SCISSORS")
    print("=" * 40)
    print("Welcome! Can you beat the computer?")
    
    while True:
        choice = get_user_menu_choice()
        
        if choice == "play":
            # Create new game and play
            game = Game()
            result = game.play()
            
            # Update results
            results[result] += 1
            print(f"\nCurrent score - Wins: {results['win']}, Losses: {results['loss']}, Draws: {results['draw']}")
            
        elif choice == "scores":
            # Show current scores without quitting
            print("\n" + "-" * 40)
            print("CURRENT SCORES:")
            print(f"Wins: {results['win']}")
            print(f"Losses: {results['loss']}")
            print(f"Draws: {results['draw']}")
            print("-" * 40)
            
        elif choice == "quit":
            # Show final results and exit
            print_results(results)
            break


# ============================================
# Main Execution
# ============================================

if __name__ == "__main__":
    main()