##ID решения 87990128
def get_points(
        values: str,
               clicks: int,
               players: int=2,
               allowed_values: str='123456789'
) -> int:
    max_clicks = clicks * players
    return sum(values.count(value) and values.count(value) <= max_clicks for value in allowed_values)

if __name__ == '__main__':
    print(
        get_points(
            clicks=int(input()),
        values=f'{input()}{input()}{input()}{input()}'
        )
    )
