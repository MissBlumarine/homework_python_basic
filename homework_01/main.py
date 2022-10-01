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
    # results = []
    # for i in numbers:
    #     results.append(i ** power)
    # return print("<<<", results)
    return [number ** power for number in numbers]
print(power_numbers(1,2,3,7))


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

# Функция проверки является ли число простым

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    k = 0
    for i in range(2, n // 2+1):
        if (n % i == 0):
            k += 1
    if (k <= 0):
        n = n
    else:
        n = None
    return n

is_prime(5)

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
        result = list(filter(is_prime, list_numbers))
    return result

filter_numbers([1, 2, 3], PRIME)

filter_numbers([2, 3, 4, 5], EVEN)
