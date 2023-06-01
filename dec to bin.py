def to_binary(number: int) -> str:
    bin_number = ''
    if number == 1:
        return '1'
    elif number == 0:
        return '0'
    while number != 1:
        if number % 2 == 0:
            bin_number += '0'
            number = int(number / 2)
        else:
            bin_number += '1'
            number = int((number-1) / 2)
    bin_number += '1'
    return bin_number[::-1]


def read_input() -> int:
    return int(input().strip())


print(to_binary(read_input()))