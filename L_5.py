# Задача №31. Решение в группах
# Последовательностью Фибоначчи называется
# последовательность чисел a0
# , a1
# , ..., an
# , ..., где
# a0
#  = 0, a1
#  = 1, ak
#  = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21
# Задание необходимо решать через рекурсию

# def fib(k):
#     if k == 0:
#         return 0
#     elif k in [1, 2]:
#         return 1
#     return fib(k-1) + fib(k-2)
#
# n = int(input('Введите порядковый номер числа: '))
# print(f'Порядковому числу {n} соответстует число {fib(n)} в последовательности Фибоначчи')

# list_1 = []
# for i in range(0, 10):
#     list_1.append(fib(i))
# print(list_1)

#######################################################################################################################

# Задача №33. Решение в группах
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

# def change(lst):
#     for i in range(len(lst)):
#         if lst[i] == max(lst):
#             lst.pop(i)
#             lst.insert(i, min(lst))
#     return lst
#
#
# list_1 = [int(input('Введите элемент: ')) for i in range(6)]
#
# print(change(list_1))

#######################################################################################################################

# Задача №35. Решение в группах
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

#
# def prime_number_check(num):
#     count = 0
#     res1 = 'yes'
#     res2 = 'no'
#     for i in range(1, num + 1):
#         if num % i == 0:
#             count += 1
#     if count == 2:
#         return res1
#     return res2
#
#
# n = int(input('Введите число: '))
# print(prime_number_check(n))


# Задача №37. Решение в группах
# 15 минут
# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3