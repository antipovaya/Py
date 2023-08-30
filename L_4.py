# Задача №25. Решение в группах
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()

# text = input('Введите символы через пробел: ').split()  # пробел разделитель, превращаем в список строку
#
# print(type(text))
#
# counter = 0
# for i in text:
#     print(i)
#     for j in range(1, len(text)):
#         counter = 0
#         if text[i - 1] == text[j]:
#             counter += 1
#             text.pop(j)
#
# print(text)

# Задача №27. Решение в группах
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13

text = ("She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells "
        "sea shells on the sea shore I'm sure that the shells are sea")

text = text.upper()  # переводим все буквы в верхний регистр

print(len(set(text.split())))
# text = text.split('.')  # разбиваю на элементы относительно точки
#
# for i in range(len(text)):
#     text[i] = text[i].split()  # каждый элеменд разбиваю относительно пробела
#
# text2 = list()
# for i in range(len(text)):
#     text2 += text[i]
# print(text2)
#
# text2 = set(text2)
# print(text2)
# print(len(text2))




