from typing import List, Tuple


def get_neighbours(matrix: List[List[int]], row: int, col: int) -> List[int]:
    neighbours = []
    rows_length, cols_length = len(matrix), len(matrix[0])
    if row != 0:
        neighbours.append(matrix[row - 1][col])
    if row != rows_length - 1:
        neighbours.append(matrix[row + 1][col])
    if col != 0:
        neighbours.append(matrix[row][col - 1])
    if col != cols_length - 1:
        neighbours.append(matrix[row][col + 1])
    return sorted(neighbours)


def read_input() -> Tuple[List[List[int]], int, int]:
    n = int(input())
    m = int(input())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().strip().split())))
    row = int(input())
    col = int(input())
    return matrix, row, col


matrix, row, col = read_input()
print(" ".join(map(str, get_neighbours(matrix, row, col))))
