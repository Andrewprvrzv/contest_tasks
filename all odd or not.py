def check_parity(a: int, b: int, c: int) -> bool:
    if (a & 1) == (b & 1) == (c & 1):
        return True
    else:
        return False


def print_result(result: bool) -> None:
    if result:
        print("WIN")
    else:
        print("FAIL")


a, b, c = map(int, input().strip().split())
print_result(check_parity(a, b, c))