# id решения  87964284
from typing import List

def get_distances_to_nearest_zero(string_with_number: List[str]) -> List[int]:
    street_length = len(string_with_number)
    zero_positions = [i for i in range(0, street_length)
                if string_with_number[i] == '0']
    result = []
    for i in range(zero_positions[0]):
        result.append(zero_positions[0] - i)
    for i in range(len(zero_positions) - 1):
        left_zero = zero_positions[i]
        right_zero = zero_positions[i+1]
        for j in range(left_zero, right_zero):
            result.append(min(j - left_zero, right_zero - j))
    for i in range(zero_positions[-1], street_length):
        result.append(i - zero_positions[-1])
    return result

if __name__ == '__main__':
    k = input()
    input_data = input().strip().split()
    print(*get_distances_to_nearest_zero(input_data))
