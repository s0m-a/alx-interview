#!/usr/bin/python3
"""
The N queens puzzle is the
challenge of placing N non-attacking queens
on an NxN chessboard
"""
from typing import List, Tuple
import sys


class NQueen:
    """ Class for solving N Queen Problem """

    def __init__(self, n: int):
        """ Initialize the NQueen class with board size """
        self.n: int = n
        self.x: List[int] = [0 for _ in range(n + 1)]
        self.res: List[List[Tuple[int, int]]] = []

    def place(self, k: int, i: int) -> bool:
        """ Check if k Queen can be placed in i column """
        for j in range(1, k):
            if self.x[j] == i or abs(self.x[j] - i) == abs(j - k):
                return False
        return True

    def nQueen(self, k: int) -> List[List[Tuple[int, int]]]:
        """ Solve the N Queens problem """
        for i in range(1, self.n + 1):
            if self.place(k, i):
                self.x[k] = i
                if k == self.n:
                    solution = []
                    for j in range(1, self.n + 1):
                        solution.append((j - 1, self.x[j] - 1))
                    self.res.append(solution)
                else:
                    self.nQueen(k + 1)
        return self.res


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    N = sys.argv[1]

    try:
        N = int(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    queen = NQueen(N)
    result = queen.nQueen(1)

    for sol in result:
        print(sol)
