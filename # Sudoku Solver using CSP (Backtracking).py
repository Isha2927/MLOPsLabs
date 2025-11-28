# Sudoku Solver using CSP (Backtracking)

# 0 will represent empty cells in the Sudoku board
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],

    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],

    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]


def print_board(b):
    """Print the Sudoku board neatly."""
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)  # horizontal separator

        row = ""
        for j in range(9):
            if j % 3 == 0 and j != 0:
                row += "| "  # vertical separator
            row += str(b[i][j]) + " "
        print(row)


def find_empty(b):
    """
    Find an empty cell in the board.
    Return (row, col) or None if no empty cell.
    """
    for i in range(9):
        for j in range(9):
            if b[i][j] == 0:
                return i, j  # row, col
    return None


def is_safe(b, row, col, num):
    """
    Check if we can place 'num' in cell (row, col)
    without breaking Sudoku rules.
    """

    # 1. Check row
    for j in range(9):
        if b[row][j] == num:
            return False

    # 2. Check column
    for i in range(9):
        if b[i][col] == num:
            return False

    # 3. Check 3x3 subgrid
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if b[i][j] == num:
                return False

    return True  # safe to place


def solve_sudoku(b):
    """
    Solve the Sudoku using backtracking.
    Returns True if solved, False if no solution.
    """

    # 1. Find an empty cell
    empty_pos = find_empty(b)
    if not empty_pos:
        return True  # no empty cell -> solved

    row, col = empty_pos

    # 2. Try numbers 1 to 9 (domain)
    for num in range(1, 10):
        if is_safe(b, row, col, num):
            # Try assigning num (CSP assignment)
            b[row][col] = num

            # Recursively try to solve the rest
            if solve_sudoku(b):
                return True

            # If failure, undo and try next number (backtrack)
            b[row][col] = 0

    # If no number fits, trigger backtracking
    return False


print("Initial Sudoku:")
print_board(board)

if solve_sudoku(board):
    print("\nSolved Sudoku:")
    print_board(board)
else:
    print("No solution exists.")
