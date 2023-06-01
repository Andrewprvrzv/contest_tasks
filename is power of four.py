def is_power_of_four(number: int) -> bool:
    return ((number & (number - 1)) == 0) and (number % 3 == 1)

print(is_power_of_four(int(input())))