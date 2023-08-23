# Задача №17. Решение в группах
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

# рандомное число

# import random
# n = random.randint(1, 100)
# print(n)

from random import randint

# n = int(input())
# list_1 = [randint(1, 10) for i in range(n)]
# print(list_1)
#
# # list_1 = [3, 3, 3, 6, 6]
# for i in range(len(list_1)):
#     for j in range(0, len(list_1) - i - 1):
#         if list_1[j] > list_1[j+1]:
#             list_1[j], list_1[j+1] = list_1[j+1], list_1[j]
# print(list_1)
#
# count = 1
# for i in range(1, len(list_1)):
#
#     if list_1[i - 1] != list_1[i]:
#         count += 1
#
# print(count)


# Задача №19. Решение в группах
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

n, k = int(input()), int(input())

list_1 = [i + 1 for i in range(n)]
print(list_1)
