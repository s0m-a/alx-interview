def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]
    for row_index in range(1, n):
        new_row = [1]
        previous_row = triangle[row_index - 1]
        for col_index in range(1, len(previous_row)):
            new_element = previous_row[col_index - 1] + previous_row[col_index]
            new_row.append(new_element)
        new_row.append(1)
        triangle.append(new_row)

    return triangle
