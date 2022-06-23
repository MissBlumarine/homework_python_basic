"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*numbers, power=2):

    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    results = []
    for i in numbers:
        results.append(i ** power)
    return print("<<<", results)

print(power_numbers(1,2,3,7))


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

# Функция проверки является ли число простым

def is_prime(num):
    result = []
    for n in num:
        k = 0
        for i in range(2, n // 2+1):
            if (n % i == 0):
                k += 1
        if (k <= 0):
            result.append(n)
    return result


def filter_numbers(list_numbers, type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    result = []
    if type == ODD:
        for number in list_numbers:
            if number % 2 != 0:
                result.append(number)
    if type == EVEN:
        for number in list_numbers:
            if number % 2 == 0:
                result.append(number)
    if type == PRIME:
        result = is_prime(list_numbers)
        
    return print("<<<", result)

print(filter_numbers([1, 2, 3], PRIME))

print(filter_numbers([2, 3, 4, 5], EVEN))