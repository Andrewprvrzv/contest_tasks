def is_palindrome(line: str) -> bool:
    line = "".join(c.lower() for c in line if c.isalpha())
    for i in range(0, int(len(line)/2)):
        if not line[i] == line[0-(i+1)]:
            return False
    return True


print(is_palindrome(input().strip()))