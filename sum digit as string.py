from typing import List, Tuple

def get_sum(number_list: List[int], k: int) -> List[int]:
    number = ''
    for i in number_list:
        number += str(i)
    result_str = str(int(number) + k)
    result = [int(i) for i in result_str]
    return result


def read_input() -> Tuple[List[int], int]:
    n = int(input())
    number_list = list(map(int, input().strip().split()))
    k = int(input())
    return number_list, k

number_list, k = read_input()
print(" ".join(map(str, get_sum(number_list, k))))