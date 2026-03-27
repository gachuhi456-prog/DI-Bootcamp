# ============================================
# Tic Tac Toe Game
# ============================================

def display_board(board):
    """Print the current state of the game board."""
    print("\n  0   1   2")
    print("  -----------")
    for i, row in enumerate(board):
        print(f"{i} | {' | '.join(row)} |")
        print("  -----------")
    print()


def player_input(player, board):
    """Get and validate the player's move."""
    while True:
        try:
            print(f"Player {player}'s turn")
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))
            
            # Check if position is within valid range
            if row < 0 or row > 2 or col < 0 or col > 2:
                print("Invalid position! Row and column must be 0, 1, or 2.")
                continue
            
            # Check if cell is empty
            if board[row][col] != " ":
                print("That cell is already occupied! Choose another.")
                continue
            
            return row, col
            
        except ValueError:
            print("Invalid input! Please enter numbers only.")


def check_win(board, player):
    """Check if the current player has won."""
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    
    # Check diagonals
    # Main diagonal (top-left to bottom-right)
    if all(board[i][i] == player for i in range(3)):
        return True
    
    # Anti-diagonal (top-right to bottom-left)
    if all(board[i][2-i] == player for i in range(3)):
        return True
    
    return False


def check_tie(board):
    """Check if the game is a tie (all cells filled, no winner)."""
    for row in board:
        if " " in row:
            return False
    return True


def switch_player(current_player):
    """Switch between players X and O."""
    return "O" if current_player == "X" else "X"


def play():
    """Main game loop."""
    # Initialize empty 3x3 board
    board = [[" " for _ in range(3)] for _ in range(3)]
    
    # Start with player X
    current_player = "X"
    
    print("=" * 40)
    print("       WELCOME TO TIC TAC TOE!")
    print("=" * 40)
    print("Players take turns placing X and O on the board.")
    print("First to get 3 in a row wins!")
    print()
    
    # Main game loop
    while True:
        # Display current board
        display_board(board)
        
        # Get player move
        row, col = player_input(current_player, board)
        
        # Update board
        board[row][col] = current_player
        
        # Check for winner
        if check_win(board, current_player):
            display_board(board)
            print(f"🎉 Player {current_player} wins! 🎉")
            break
        
        # Check for tie
        if check_tie(board):
            display_board(board)
            print("It's a tie! 🤝")
            break
        
        # Switch player
        current_player = switch_player(current_player)
    
    print("\nGame over! Thanks for playing!")


# Start the game
if __name__ == "__main__":
    play()