# Задача №17. Решение в группах
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

# рандомное число

# import random
# n = random.randint(1, 100)
# print(n)

# from random import randint
#
# n = int(input())
# list_1 = [randint(1, 10) for i in range(n)]
# print(list_1)


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
# 2 3 3 4 5 3 6  2 3 3 3 4 5 6
# print(count)



# Решение через сет
# from random import randint
# n = int(input())
# list_1 = [randint(1, 10) for i in range(n)]
#
# print(list_1)
# list_1 = set(list_1)
# print(len(list_1))

# Не мое через срезы
str1 = [1, 1, 2, 0, -1, 3, 4, 4]
counter = 0
for i in range(len(str1)):
    if str1[i] not in str1[:i]:
        counter += 1
print(counter)


# #          0  1  2  3   4  5  6  7
# my_list = [1, 1, 2, 0, -1, 3, 4, 0]
#
# print(my_list[-1:-3:-1])



# Не мое
list_with_duplicates = [1, 1, 2, 0, -1, 3, 4, 4]
list1 = []
for i in list_with_duplicates:
    if i not in list1:
        list1.append(i)
print(len(list1))

# range(5) -> 0, 1, 2, 3, 4
# range(5, 10) -> 5, 6, 7, 8, 9
# range(1, 11, 2) -> 1, 3, 5, 7, 9

# for i in range(5): - просто выводятся число от 0 до  4
#     print(i)

# for new_num in range(5, 10): - выодятся от 5 до 9
#     print(new_num)

# for temp in range(1, 11, 2): - с шагом 2
#     print(temp)
#######################################################################################################################

# Задача №19. Решение в группах
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

# n, k = int(input()), int(input())
#
# list_1 = [i + 1 for i in range(n)]
# print(list_1)
# list_2 = [i + 1 for i in range(n)]
#
# for i in range(k):
#
#     list_2[len(list_2) - k + i] = list_1[i]
# print(list_2)
#
# for i in range(n-k):
#     list_2[i] = list_1[i + k]
# print(list_2)


# Решение через срезы

# n, k = int(input()), int(input())
#
# list_1 = [i + 1 for i in range(n)]
# print(list_1)
# #
# # print(list_1[:k])
# #
# # print(list_1[k:len(list_1)])
#
# print(list_1[k:len(list_1)] + list_1[:k])

# решение с семинара

# lst = [1, 2, 3, 4, 5, 6]
# k = 3
# for i in range(k):
#     el = lst.pop()
#     lst.insert(0, el)
# print(lst)


#######################################################################################################################

# Задача №21. Решение в группах
# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

#
# d = {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
# for (k, v) in d.items():
#     print(v)

# решение на семинаре

my_list = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, \
{"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}]

all_val = []
for now_dict in my_list:
    for val in now_dict.values():
        all_val.append(val)


print(set(all_val))

#######################################################################################################################

# Задача №23. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)

#
# from random import randint
#
# n = int(input())
# list_1 = [randint(1, 10) for i in range(n)]
# print(list_1)
#
# count = 0
# for i in range(1, len(list_1)):
#
#     if list_1[i - 1] < list_1[i]:
#         count += 1
#
# print(count)
