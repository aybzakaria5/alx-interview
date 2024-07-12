#!/usr/bin/python3
"""N-Queens Problem Solver"""
import sys


def solve_queens_problem(board_size):
    """Find all solutions to the N-Queens problem for a given board size"""

    def is_valid_position(current_column, placedClm):
        """Check if the current position is valid for placing a queen"""
        for row in range(len(placedClm)):
            if (
                placedClm[row] == current_column or
                placedClm[row] - row == current_column - len(placedClm) or
                placedClm[row] + row == current_column + len(placedClm)
            ):
                return False
        return True

    def place_queens(board_size, current_row, placedClm, solutions):
        """Recursively place queens on the board"""
        if current_row == board_size:
            solutions.append(placedClm[:])
            return

        for column in range(board_size):
            if is_valid_position(column, placedClm):
                placedClm.append(column)
                place_queens(board_size, current_row + 1, placedClm, solutions)
                placedClm.pop()

    solutions = []
    place_queens(board_size, 0, [], solutions)
    return solutions


def main():
    """Main function to handle input and output"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        board_size = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if board_size < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_queens_problem(board_size)
    for solution in solutions:
        print([[row, solution[row]] for row in range(len(solution))])


if __name__ == "__main__":
    main()
