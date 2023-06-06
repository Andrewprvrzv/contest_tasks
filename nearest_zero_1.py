# id решения  87993386
from typing import List

def get_distances_to_nearest_zero(numbers: List[str],
                                  key_value: str= '0') -> List[int]:
    street_length = len(numbers)
    results = [0] * street_length
    zeros = [pos for pos, value in enumerate(numbers)
             if value == key_value]
    start, end = zeros[0], zeros[-1]
    results[:start] = [start - pos for pos in range(start)]
    results[start:end] = [
        min(pos - left, right - pos) if pos != left else 0
        for left, right in zip(zeros, zeros[1:])
        for pos in range(left, right)
    ]
    results[end + 1:] = [
        pos - end for pos in range(end + 1, street_length)
    ]
    return results

if __name__ == '__main__':
    input()
    print(*get_distances_to_nearest_zero(numbers=input().split()))
