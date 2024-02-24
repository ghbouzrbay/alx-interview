#!/usr/bin/python3
import sys

def is_attacking(row1, col1, row2, col2):
    return row1 == row2 or col1 == col2 or abs(row1 - row2) == abs(col1 - col2)

def place_n_queens(n, row, result):
    if row == n:
        yield result.copy()
    else:
        for col in range(n):
            if not any(is_attacking(row, col, r, c) for r, c in result):
                result.append((row, col))
                yield from place_n_queens(n, row + 1, result)
                result.pop()

def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    for solution in place_n_queens(n, 0, []):
        print(solution)

if __name__ == "__main__":
    main()
