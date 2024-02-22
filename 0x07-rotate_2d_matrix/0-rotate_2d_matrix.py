#!/usr/bin/python3
"""2D matrix rotation module."""

def rotate_2d_matrix(matrix):
    """Rotates an m by n 2D matrix in place."""
    n = len(matrix)
    for i in range(n // 2):
        for j in range(i, n - i - 1):
            # Swap elements in a "spiral" pattern
            matrix[i][j], matrix[n-j-1][i], matrix[n-i-1][n-j-1], matrix[j][n-i-1] = \
            matrix[n-j-1][i], matrix[n-i-1][n-j-1], matrix[j][n-i-1], matrix[i][j]
