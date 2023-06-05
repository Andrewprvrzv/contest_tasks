##ID решения 87927252
from typing import List, Tuple

def get_points(matrix, k) -> (List[List[str]], int):
    number_count = {}
    points = 0
    for i in range(4):
        for x in range(4):
            if matrix[i][x] == '.':
                matrix[i][x] = 0
            else:
                matrix[i][x] = int(matrix[i][x])
    for i in range(4):
        for x in range(4):
            if not matrix[i][x] in number_count.keys():
                number_count[matrix[i][x]] = 1
            else:
                number_count[matrix[i][x]] = number_count[matrix[i][x]] + 1
    t = max(number_count.keys())
    round = 1
    while round <= t:
        if round in number_count.keys():
            if number_count[round] <= k*2:
                points += 1
        round += 1

    return points


def read_input() -> Tuple[List[List[str]], int]:
    k = int(input())
    matrix = []
    for i in range(4):
        matrix.append(list(''.join(map(str, input().strip().split()))))
    return matrix, k

matrix, k = read_input()
print(get_points(matrix, k))
