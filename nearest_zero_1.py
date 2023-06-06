# id решения  87985154
from typing import List

def get_distances_to_nearest_zero(numbers: List[str],
                                  key_value: str= '0') -> List[int]:
    street_length = len(numbers)
    results = [0] * street_length
    zeros = [position for position, value in enumerate(numbers)
             if value == key_value]
    start, end = zeros[0], zeros[-1]
    for pointer in range(start):
        results[pointer] = start - pointer
    for left, right in zip(zeros, zeros[1:]):
        for pointer in range(left+1, right):
                results[pointer] = (min(pointer - left, right - pointer))
    for pointer in range(end+1, street_length):
        results[pointer] = pointer - end
    return results

if __name__ == '__main__':
    input()
    print(*get_distances_to_nearest_zero(numbers=input().split()))
