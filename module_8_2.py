def personal_sum(items):
    total = 0
    count = 0

    for item in items:
        if isinstance(item, (int, float)):
            total += item
            count += 1
        else:
            print(f'Некорректный тип данных для подсчёта суммы - {item}')
    return total, count


def calculate_average(data):
    if isinstance(data, str):
        numbers = data.split(',')
    elif isinstance(data, (list, tuple)):
        numbers = data
    else:
        print(f'В numbers записан некорректный тип данных')
        return None

    total, count = personal_sum(numbers)

    if count == 0:
        return 0

    average = total / count
    return average

print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')
