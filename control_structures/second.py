"""
Цикл while

Напишите функцию collect_numbers, которая запрашивает у пользователя целые числа и сохраняет их в список. 
Функция должна завершить сбор чисел, когда пользователь вводит число 0. После завершения ввода, 
функция должна вернуть кортеж с элементами, расположенными в следующем порядке:
1. Список введенных чисел.
2. Сумму всех введенных чисел.
3. Среднее значение введенных чисел (исключая 0).
4. Максимальное и минимальное введенное число (исключая 0).
5. Количество введенных четных и нечетных чисел.
6. Количество введенных положительных и отрицательных чисел.

"""


def collect_numbers() -> tuple:
    numbers = []
    element = None
    even_count = 0
    odd_count = 0
    positive_count = 0
    negative_count = 0

    while element != 0:
        element = int(input())
        if element != 0:
            numbers.append(element)
        if (element % 2) == 0 and element != 0:
            even_count += 1
        if (element % 2) != 0:
            odd_count += 1
        if element > 0:
            positive_count += 1
        if element < 0:
            negative_count += 1

    element = None
    sum = 0
    for element in numbers:
        sum += element

    avg = sum / len(numbers)

    min_max = {"min": min(numbers), "max": max(numbers)}

    odd_even = {"Чётные": even_count, "Нечётные": odd_count}

    positive_negative = {
        "Положительные": positive_count,
        "Отрицательные": negative_count,
    }

    return (numbers, sum, avg, min_max, odd_even, positive_negative)


numbers = collect_numbers()
print(numbers)
