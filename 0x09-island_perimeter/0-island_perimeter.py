#!/usr/bin/python3
"""Island perimeter computing module.
"""

def island_perimeter(grid):
    """Computes the perimeter of an island with no lakes.
    """
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                perimeter += 4  # Count each side of the current cell as part of the perimeter
                if i > 0 and grid[i-1][j] == 1:  # Check if there is a cell above the current cell
                    perimeter -= 2  # If there is, subtract 2 from the perimeter since we counted the top side twice
                if j > 0 and grid[i][j-1] == 1:  # Check if there is a cell to the left of the current cell
                    perimeter -= 2  # If there is, subtract 2 from the perimeter since we counted the left side twice
    return perimeter
