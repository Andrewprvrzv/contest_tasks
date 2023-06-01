from typing import List

def get_distance_to_zero(number_list: List[int]) -> List[int]:
    length = len(number_list)

    pass


def read_input() -> List[int]:
    n = int(input())
    number_list = list(map(int, input().strip().split()))
    return number_list

number_list = read_input()


print(" ".join(str, get_distance_to_zero(number_list)))
