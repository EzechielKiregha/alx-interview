#!/usr/bin/python3
"""
a island perimiter interview
question
"""


def island_perimeter(grid):
    """
    island perimeter interview
    question
    """
    number_of_rows = len(grid)
    number_of_column = len(grid[0])
    assume_perimeter = 0
    connection = 0

    for y in range(0, number_of_rows):
        for x in range(0, number_of_column):
            if grid[y][x] == 1:
                assume_perimeter += 4
                if y != 0 and grid[y - 1][x] == 1:
                    connection += 1
                if x != 0 and grid[y][x - 1] == 1:
                    connection += 1
    return assume_perimeter - (connection * 2)
