# id решения  87996103
from typing import List, Sequence, Any


def get_distances_to_nearest_zero(
        numbers: Sequence[Any],
        key_value: Any = '0'
) -> List[int]:
    length = len(numbers)
    results = [0] * length
    zeros = [pos for pos, value in enumerate(numbers) if value == key_value]
    start, end = zeros[0], zeros[-1]
    results[:start] = [start - pos for pos in range(start)]
    for left, right in zip(zeros, zeros[1:]):
        results[left + 1:right] = [
            min(pos - left, right - pos)
            for pos in range(left + 1, right)
        ]
    results[end + 1:] = [pos - end for pos in range(end + 1, length)]
    return results


if __name__ == '__main__':
    input()
    print(*get_distances_to_nearest_zero(numbers=input().split()))
