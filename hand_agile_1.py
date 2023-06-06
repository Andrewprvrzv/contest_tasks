#ID решения 87996137
from typing import Iterable, Any, Sequence


def get_points(
        values: Sequence[Any],
        clicks: int,
        players: int = 2,
        allowed_values: Iterable[Any] = '123456789'
) -> int:
    max_clicks = clicks * players
    return sum(
        0 != values.count(value) <= max_clicks
        for value in allowed_values
    )


if __name__ == '__main__':
    print(
        get_points(
            clicks=int(input()),
            values=f'{input()}{input()}{input()}{input()}'
        )
    )
