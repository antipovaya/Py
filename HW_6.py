# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов
# нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.

# Ввод: 7 2 5
# Вывод: 7 9 11 13 15


# def arithmetic_sequence(a, d, n):
#     list_1 = [a + (i - 1) * d for i in range(1, n + 1)]
#     return list_1
#
#
# a_user = int(input('Введите первый элемент арифметической прогрессии: '))
# d_user = int(input('Введите шаг арифметической прогрессии: '))
# n_user = int(input('Введите количество элементов: '))
#
# list_new = arithmetic_sequence(a_user, d_user, n_user)
#
# print(list_new)

#######################################################################################################################

# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]


from random import randint


def new_lst(num):
    lst_1 = [randint(-10, 10) for _ in range(num)]
    return lst_1


def index_search(n1, n2, list_1):
    res = [i for i in range(len(list_1)) if (list_1[i] > min(n1, n2)) and (list_1[i] < max(n1, n2))]
    return res


n = int(input('Введите количество элементов в списке: '))
list_user = new_lst(n)
print(list_user)
n1_user, n2_user = int(input('Введите границу диапазона: ')), int(input('Введите границу диапазона: '))

index_list = index_search(n1_user, n2_user, list_user)
print(index_list)

