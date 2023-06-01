from typing import List


def factorize(number: int) -> List[int]:
    d = 2
    factors = []
    while number > 1:
        while number % d == 0:
            factors.append(d)
            number /= d
            number = int(number)
        d += 1
        if d * d > number:
            if number > 1:
                factors.append(number)
                break
    return factors


result = factorize(int(input()))
print(" ".join(map(str, result)))