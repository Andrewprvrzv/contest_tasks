### id решения 87925817
from typing import List

#### Выполняется долго и неэффективно (чуть больше 3 секунд в тестах контеста)

# def get_distance_to_zero(number_list: List[int]) -> List[int]:
#     zero_idx = [i for i in range(0, len(number_list)) if number_list[i] == 0]
#     result = []
#     for i in range(0, len(number_list)):
#         if number_list[i] == 0:
#             result.append(0)
#         else:
#             distance = []
#             for z in zero_idx:
#                 distance.append(abs(z-i))
#             result.append(min(distance))
#     return result

##### Быстрое решение, проходим слева-направо, а потом справа-налево, из
##### двух списков выберем наименьшее расстояние для каждого элемента первоначального списка
def get_distance_to_zero(number_list: List[int]) -> List[int]:
    length = len(number_list)
    left = [0] * length
    last_zero = -length
    for i in range(length):
        if number_list[i] == 0:
            last_zero = i
        left[i] = i - last_zero
    right = [0] * length
    last_zero = 2 * length
    for i in range(length-1, -1, -1):
        if number_list[i] == 0:
            last_zero = i
        right[i] = last_zero - i
    return [min(left[i], right[i]) for i in range(length)]


def read_input() -> List[int]:
    n = int(input())
    number_list = list(map(int, input().strip().split()))
    return number_list

number_list = read_input()


print(" ".join(map(str, get_distance_to_zero(number_list))))
