##ID решения 87969839
def get_points(values: str,
               clicks: int,
               allowed_values: str='123456789') -> int:
    values_count = {value:values.count(value) for value in values
                    if value in allowed_values}
    return sum(values_count[value] <= clicks for value in values_count.keys())

if __name__ == '__main__':
    print(get_points(clicks=int(input())*2,
        values=''.join(i for i in f'{input()}{input()}{input()}{input()}'))
          )
