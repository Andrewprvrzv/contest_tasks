def get_longest_word(line: str) -> str:
    longest_word = max(line.split(), key=len)
    return longest_word


def read_input() -> str:
    _ = input()
    line = input().strip()
    return line

def print_result(result: str) -> None:
    print(result)
    print(len(result))

print_result(get_longest_word(read_input()))