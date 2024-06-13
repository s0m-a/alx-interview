#!/usr/bin/python3
"""Defines a function to calculate the
perimeter of an island in a grid."""


def island_perimeter(grid):
    """
    Calculate the perimeter of an island.
    
    The grid represents water by 0 and land by 1.

    Args:
        grid (list): A list of lists of integers representing an island.

    Returns:
        int: The perimeter of the island defined in the grid.
    """
    num_columns = len(grid[0])
    num_rows = len(grid)
    adjacent_edges = 0
    land_cells = 0

    for row in range(num_rows):
        for col in range(num_columns):
            if grid[row][col] == 1:
                land_cells += 1
                # Check for adjacent land cells on the left and above
                if col > 0 and grid[row][col - 1] == 1:
                    adjacent_edges += 1
                if row > 0 and grid[row - 1][col] == 1:
                    adjacent_edges += 1
    return land_cells * 4 - adjacent_edges * 2
