# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

s, p = int(input('Введите сумму чисел: ')), int(input('Введите произведение чисел: '))
count = 0
for i in range(1, p + 1):
    if p / i == s - i:
        print(i, s - i)

