# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное
# число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите
# минимальное количество монет, которые нужно перевернуть.

# n = int(input('Введите количество монет: '))
# count1 = 0
# count2 = 0
# for i in range(n):
#     side = int(input('Введите сторону монеты (0 или 1): '))
#     if side == 0:
#         count1 += 1
#     elif side == 1:
#         count2 += 1
# print('Всего перевернуть нужно', count2 if count1 > count2 else count1, 'монет')

#######################################################################################################################

# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

# 12.1)

# x + y = s
# x * y = p
# y = s - x
# x * (s - x) = p
# s*x - x**2 = p
# x**2 - s*x + p = 0 - привели к квадратному уравнению и решаем через дискриминант

# from math import *
# s, p = int(input('Введите сумму чисел: ')), int(input('Введите произведение чисел: '))
#
# d = s ** 2 - 4 * 1 * p
# if d < 0:
#     print('Нет таких чисел')
# else:
#     x1 = (s + sqrt(d)) / (2 * 1)
#     x2 = (s - sqrt(d)) / (2 * 1)
#     if x1 == x2:
#         print(int(x1), 'и', int(s - x1), 'загаданные числа')
#     elif int(min(x1, x2)) == int(s - max(x1, x2)) or int(max(x1, x2)) == int(s - min(x1, x2)):
#         print(int(min(x1, x2)), 'и', int(s - min(x1, x2)), 'загаданные числа')
#     else:
#         print('Таких чисел несколько')
#         print(int(min(x1, x2)), 'и', int(s - min(x1, x2)), 'загаданные числа')
#         print(int(max(x1, x2)), 'и', int(s - max(x1, x2)), 'загаданные числа')

# 12.2)
# Решение задачи через цикл:

# s, p = int(input('Введите сумму чисел: ')), int(input('Введите произведение чисел: '))
# count = 0
# for i in range(1, p + 1):
#     if p / i == s - i:
#         print(i, s - i)


#######################################################################################################################

# Требуется вывести все целые степени двойки (т.е. числа
# вида 2k
# ), не превосходящие числа N.

# n = int(input('Введите число: '))
# i = 0
# while 2**i < n:
#     print(2**i, '- это 2 в степени', i)
#     i += 1

