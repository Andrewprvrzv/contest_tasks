# Импортируйте необходимые модули
import datetime as dt
import timeit

FORMAT = '%H:%M:%S'  # Запишите формат полученного времени.
WEIGHT = 75  # Вес.
HEIGHT = 175  # Рост.
K_1 = 0.035  # Коэффициент для подсчета калорий.
K_2 = 0.029  # Коэффициент для подсчета калорий.
STEP_M = 0.65  # Длина шага в метрах.

storage_data = {}


def check_correct_data(data):
    if not len(data) != 2 and None not in data:
        return False
    else:
        return True


def check_correct_time(time):
    if storage_data == {}:
        return False
    elif time <= max(storage_data):
        return True

    """Проверка корректности параметра времени."""
    # Если словарь для хранения не пустой
    # и значение времени, полученное в аргументе,
    # меньше самого большого ключа в словаре,
    # функция вернет False.
    # Иначе - True 


def get_step_day(steps):
    if storage_data == {}:
        return steps
    else:
        return storage_data[max(storage_data.keys())] + steps


def get_distance(steps):
    return (STEP_M * steps) / 1000


def get_spent_calories(dist, current_time):
    if current_time != 0:
        current_time_float_hours = current_time.minute/60 + current_time.hour
    else:
        current_time_float_hours = current_time.hour
    mean_speed = dist / current_time_float_hours
    return (K_1 * WEIGHT + (mean_speed**2 / HEIGHT) * K_2 * WEIGHT) * (60 * current_time_float_hours)


def get_achievement(dist):
    if dist >= 6.5:
        return 'Отличный результат! Цель достигнута.'
    elif dist >= 3.9:
        return 'Неплохо! День был продуктивным.'
    elif dist >= 2:
        return 'Маловато, но завтра наверстаем!'
    else:
        return 'Лежать тоже полезно. Главное — участие, а не победа!'


def show_message(pack_time, day_steps, dist, spent_calories, achievement):
    print(
f"""
Время: {pack_time}.
Количество шагов за сегодня: {day_steps}.
Дистанция составила {dist:.2f} км.
Вы сожгли {spent_calories:.2f} ккал.
{achievement}
""")


def accept_package(data):
    """Обработать пакет данных."""

    if check_correct_data(data):  # Если функция проверки пакета вернет False
        return 'Некорректный пакет'

    # Распакуйте полученные данные.
    pack_time = dt.datetime.strptime(data[0], FORMAT).time()  # Преобразуйте строку с временем в объект типа time.

    if check_correct_time(pack_time):  # Если функция проверки значения времени вернет False
        return 'Некорректное значение времени'

    day_steps = get_step_day(data[1])  # Запишите результат подсчёта пройденных шагов.
    dist = get_distance(day_steps)  # Запишите результат расчёта пройденной дистанции.
    spent_calories = get_spent_calories(dist, pack_time)  # Запишите результат расчёта сожжённых калорий.
    achievement = get_achievement(dist)  # Запишите выбранное мотивирующее сообщение.
    show_message(pack_time, day_steps, dist, spent_calories, achievement)
    storage_data[pack_time] = day_steps
    return storage_data



# Данные для самопроверки.Не удаляйте их.
package_0 = ('2:00:01', 505)
package_1 = (None, 3211)
package_2 = ('9:36:02', 15000)
package_3 = ('9:36:02', 9000)
package_4 = ('8:01:02', 7600)

accept_package(package_0)
accept_package(package_1)
accept_package(package_2)
accept_package(package_3)
accept_package(package_4)
