#!/usr/bin/python3
'''A module for generating Pascal's triangle.
'''


def pascal_triangle(n):
    '''Generates Pascal's triangle up to the nth row.

    Args:
        n (int): The number of rows to generate.

    Returns:
        list: A list of lists representing Pascal's triangle.
    '''
    triangle = []
    if type(n) is not int or n <= 0:
        return triangle
    
    # Generate each row of Pascal's triangle
    for row_index in range(n):
        row = []
        for col_index in range(row_index + 1):
            # First and last elements in each row are always 1
            if col_index == 0 or col_index == row_index:
                row.append(1)
            # Calculate other elements based on the values from the previous row
            elif row_index > 0 and col_index > 0:
                row.append(triangle[row_index - 1][col_index - 1] + triangle[row_index - 1][col_index])
        triangle.append(row)
    return triangle

