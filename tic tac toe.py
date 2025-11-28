import math

# --------- GAME HELPER FUNCTIONS ---------

def print_board(board):
    """Print the 3x3 Tic-Tac-Toe board."""
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()


def check_winner(board):
    """Return 'X' if X wins, 'O' if O wins, 'draw' if board full, else None."""
    winning_combos = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
        (0, 4, 8), (2, 4, 6)              # diagonals
    ]

    for a, b, c in winning_combos:
        if board[a] == board[b] == board[c] != " ":
            return board[a]   # 'X' or 'O'

    if " " not in board:
        return "draw"

    return None  # game not over yet


# --------- MINIMAX ALGORITHM ---------

def minimax(board, depth, is_maximizing):
    """
    Minimax function:
    - board: current board state (list of 9 cells)
    - depth: how deep we are in the game tree
    - is_maximizing: True for AI's turn (X), False for human (O)
    Returns: best score for the current player.
    """

    result = check_winner(board)

    # Base cases: someone won or it's a draw
    if result == "X":      # AI wins
        return 10 - depth  # prefer quicker wins
    elif result == "O":    # Human wins
        return depth - 10  # prefer slower losses
    elif result == "draw":
        return 0

    # Maximizing player: AI ('X')
    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"  # try move
                score = minimax(board, depth + 1, False)
                board[i] = " "  # undo move
                best_score = max(best_score, score)
        return best_score

    # Minimizing player: Human ('O')
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"  # try move
                score = minimax(board, depth + 1, True)
                board[i] = " "
                best_score = min(best_score, score)
        return best_score


def best_move(board):
    """Find the best move for AI ('X') using minimax."""
    best_score = -math.inf
    move = None

    for i in range(9):
        if board[i] == " ":
            board[i] = "X"  # AI tries this move
            score = minimax(board, 0, False)
            board[i] = " "  # undo move

            if score > best_score:
                best_score = score
                move = i

    return move


# --------- MAIN GAME LOOP ---------

def play_game():
    board = [" "] * 9
    human = "O"
    ai = "X"
    current_player = human   # human starts

    print("Tic-Tac-Toe with Minimax AI")
    print("You are O, AI is X")
    print("Enter positions 1-9 as:")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")

    while True:
        print_board(board)
        result = check_winner(board)
        if result is not None:
            if result == "draw":
                print("Game Over! It's a DRAW.")
            else:
                print_board(board)
                if result == ai:
                    print("Game Over! AI (X) WINS 😈")
                else:
                    print("Game Over! YOU (O) WIN 🎉")
            break

        if current_player == human:
            # Human turn
            while True:
                try:
                    pos = int(input("Your move (1-9): ")) - 1
                    if pos < 0 or pos > 8:
                        print("Please enter a number from 1 to 9.")
                    elif board[pos] != " ":
                        print("That spot is already taken.")
                    else:
                        board[pos] = human
                        break
                except ValueError:
                    print("Please enter a valid number.")

            current_player = ai

        else:
            # AI turn
            print("AI is thinking...")
            move = best_move(board)
            board[move] = ai
            current_player = human


if __name__ == "__main__":
    play_game()
