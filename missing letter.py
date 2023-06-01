from typing import Tuple


def get_excessive_letter(shorter: str, longer: str) -> str:
    sorted_shorter = ''.join(sorted(shorter))
    sorted_longer = ''.join(sorted(longer))
    for i in range(0, len(sorted_shorter)):
        if not sorted_shorter[i] == sorted_longer[i]:
            return sorted_longer[i]
    return sorted_longer[-1]


def read_input() -> Tuple[str, str]:
    shorter = input().strip()
    longer = input().strip()
    return shorter, longer


shorter, longer = read_input()
print(get_excessive_letter(shorter, longer))
