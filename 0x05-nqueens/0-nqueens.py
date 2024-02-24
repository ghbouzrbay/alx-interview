#!/usr/bin/python3
import sys

def is_attacking(row1, col1, row2, col2):
    return row1 == row2 or col1 == col2 or abs(row1 - row2) == abs(col1 - col2)

def place_n_queens(n, row, result):
    for col in range(n):
        if not any(is_attacking(row, col, r, c) for r, c in result):
            result.append((row, col))
            if row + 1 < n:
                place_n_queens(n, row + 1, result)
                result.pop()
            else:
                yield result.copy()
                result.pop()
