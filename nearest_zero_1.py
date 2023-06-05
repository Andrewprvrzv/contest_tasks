# id решения  87970771
from typing import List

def get_distances_to_nearest_zero(series_of_numbers: List[str],
                                  key_value: str= '0') -> List[int]:
    street_length = len(series_of_numbers)
    results = [0]*street_length
    zeros = [position for position, value in enumerate(series_of_numbers)
             if value == key_value]
    zeros_start = zeros[0]
    zeros_end = zeros[-1]
    for pointer in range(zeros_start):
        results[pointer] = zeros_start - pointer
    for left, right in zip(zeros, zeros[1:]):
        for pointer in range(left, right):
            if pointer != left:
                results[pointer] = (min(pointer - left, right - pointer))
    for pointer in range(zeros_end, street_length):
        results[pointer] = pointer - zeros_end
    return results

if __name__ == '__main__':
    input()
    print(*get_distances_to_nearest_zero(series_of_numbers=input().split()))
