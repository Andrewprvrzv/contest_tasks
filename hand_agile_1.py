##ID решения 87958230

def get_points(values: str, clicks: int) -> int:
    max_clicks_count = clicks*2
    values_count = {}
    values = ''.join(i for i in values)
    values_set = set(values)
    for i in values_set:
        if i.isdigit():
            values_count[int(i)] = values.count(i)
    points = sum(1 for i in values_set if values.count(i) <= max_clicks_count
                 and i != '.')
    return points

if __name__ == '__main__':
    k = int(input())
    input_data = f'{input()}{input()}{input()}{input()}'
    print(get_points(input_data, k))
