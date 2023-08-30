# """
# Задача №25. Решение в группах
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()
# """

# lst = input("Введите символы через пробел: ").split()
# res = {}
# for i in lst:
#     if i in res:
#         print(f"{i}_{res[i]}", end=' ')
#     else:
#         print(i, end=' ')
#     res[i] = res.get(i, 0) + 1



#dct = {1: [1, 2, 3], 2: True}
#dct[1] = None

# n = 'a a a b b d d a d f'.split()
# print(n)
# for i in range(len(n)):
#     s = n[:i]
#     if s.count(n[i]) == 0:
#         print(n[i], end=' ')
#     else:
#         print(f'{n[i]}_{s.count(n[i])}', end=' ')

#
# all_letters = 'a b c a d b d d b c a a'.split()
#
# letters_count = {}
#
# result_str = ''
#
# for letter in all_letters:
#     if letter not in letters_count:
#         letters_count[letter] = 1
#         result_str += f'{letter} '
#     else:
#         result_str += f'{letter}_{letters_count[letter]} '
#         letters_count[letter] += 1
#
# print(result_str)


lst = input("Введите символы через пробел: ").split()
d_count = {}
count = ''
for i in lst:
    if i not in d_count:
        d_count[i] = 1
        count += f'{i} '
    else:
        count += f'{i}_{d_count[i]} '
        d_count[i] += 1

print(count)
print(type(count))






