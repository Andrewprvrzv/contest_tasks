
from typing import Tuple

def get_sum(first_number: str, second_number: str) -> str:
    in_memory = 0
    result = ''
    length = max(len(first_number), len(second_number))
    first_number = first_number.zfill(length)
    second_number = second_number.zfill(length)
    for i in range(length-1, -1, -1):
        sum = in_memory
        sum += int(first_number[i]) + int(second_number[i])
        in_memory = 1 if sum > 1 else 0
        result = ('1' if sum %2 == 1 else '0') + result
    if in_memory:
        result = '1' + result
    return result

def read_input() -> Tuple[str, str]:
    first_number = input().strip()
    second_number = input().strip()
    return first_number, second_number

first_number, second_number = read_input()
print(get_sum(first_number, second_number))