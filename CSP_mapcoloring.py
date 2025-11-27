# Map Coloring CSP for a simplified India map
# Counting moves (color assignments) and printing neat solution

# 1. Variables (States)
states = [
    "JammuKashmir",
    "Himachal",
    "Punjab",
    "Haryana",
    "Rajasthan",
    "UttarPradesh",
    "Bihar",
    "MadhyaPradesh",
    "Gujarat",
    "Maharashtra",
    "Chhattisgarh",
    "Odisha"
]

# 2. Domains (Available colors)
colors = ["Red", "Green", "Blue", "Yellow"]

# 3. Constraints: Neighbors (who must have different colors)
neighbors = {
    "JammuKashmir": ["Himachal", "Punjab"],
    "Himachal": ["JammuKashmir", "Punjab", "Haryana"],
    "Punjab": ["JammuKashmir", "Himachal", "Haryana", "Rajasthan"],
    "Haryana": ["Punjab", "Himachal", "Rajasthan", "UttarPradesh"],
    "Rajasthan": ["Punjab", "Haryana", "UttarPradesh", "MadhyaPradesh", "Gujarat"],
    "UttarPradesh": ["Haryana", "Rajasthan", "MadhyaPradesh", "Chhattisgarh", "Bihar"],
    "Bihar": ["UttarPradesh", "Chhattisgarh", "Odisha"],
    "MadhyaPradesh": ["Rajasthan", "UttarPradesh", "Chhattisgarh", "Maharashtra", "Gujarat"],
    "Gujarat": ["Rajasthan", "MadhyaPradesh", "Maharashtra"],
    "Maharashtra": ["Gujarat", "MadhyaPradesh", "Chhattisgarh"],
    "Chhattisgarh": ["MadhyaPradesh", "UttarPradesh", "Bihar", "Odisha", "Maharashtra"],
    "Odisha": ["Chhattisgarh", "Bihar"]
}

# Global counter for "moves" = number of color assignments tried
moves = 0

def is_safe(state, color, assignment):
    """
    Check if we can give 'color' to 'state'
    without clashing with any already-colored neighbor.
    """
    for neighbor in neighbors[state]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def backtrack(assignment):
    """
    Backtracking search to assign colors to all states.
    assignment is a dict like: {"Punjab": "Red", "Haryana": "Green", ...}
    """
    global moves

    # If all states are colored, return solution
    if len(assignment) == len(states):
        return assignment

    # Pick an uncolored state (simple order)
    for s in states:
        if s not in assignment:
            current_state = s
            break

    # Try each color for this state
    for color in colors:
        if is_safe(current_state, color, assignment):
            # Tentatively color the state
            assignment[current_state] = color
            moves += 1   # count this assignment as one "move"

            # Recurse for the next state
            result = backtrack(assignment)
            if result is not None:
                return result  # found a full solution

            # Backtrack (undo the color)
            del assignment[current_state]

    # No color worked → trigger backtracking
    return None

# Run the CSP solver
solution = backtrack({})

# Neat printing of result
print("India Map Coloring Solution")
print("-" * 35)

if solution:
    # Sort states alphabetically for neat output
    sorted_states = sorted(states)
    max_len = max(len(s) for s in sorted_states)

    print(f"{'State'.ljust(max_len)} | Color")
    print("-" * (max_len + 9))

    for s in sorted_states:
        print(f"{s.ljust(max_len)} | {solution[s]}")

    print("\nTotal moves (color assignments tried):", moves)
else:
    print("No solution found")
    print("Total moves (attempts):", moves)
