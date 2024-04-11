#!/usr/bin/python3

def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        temp = [1]
        for j in range(len(triangle[i - 1]) - 1):
            temp.append(triangle[i - 1][j] + triangle[i - 1][j + 1])
        temp.append(1)
        triangle.append(temp)

    return triangle
