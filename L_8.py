# группа у Читалова
from os.path import exists
from csv import DictReader, DictWriter  # импортировали для работы с csv

def get_info():
    info = []
    first_name = input('Введите имя: ')
    last_name = input('Введите фамилию: ')
    info.append(first_name)  # положили переменную в список
    info.append(last_name)
    flag = False
    while not flag:
        try:
            phone_number = int(input('Введите номер телефона: '))
            if len(str(phone_number)) != 11:
                print('Неверный номер телефона')
            else:
                flag = True
        except ValueError:
            print('Вы ввели неверный формат')
    info.append(phone_number)
    return info


def create_file():  # создаем файл
    with open('phone.txt', 'w', encoding='utf-8') as data:  #поток данных
        data.write('Фамилия;Имя;Номер\n')


def write_file(lst):
    with open('phone.txt', 'a', encoding='utf-8') as data:
        data.write(f'{lst[0]};{lst[1]};{lst[2]}\n')

def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as data:  # режим чтения стоит по дефолту, r можно не ставить
        phone_book = data.readlines()
        return phone_book

def record_info():
    lst = get_info()
    write_file(lst)


# def main():
#     while True:
#         command = input('Введите команду: ')
#         if command == 'q':
#             break
#         elif command == 'r':
#             if not exists('phone.txt'):
#                 print('Файл не создан')
#                 break
#             print(read_file('phone.txt'))
#         elif command == 'w':
#             if not exists('phone.txt'):
#                 create_file()
#                 record_info()
#             else:
#                 record_info()

# main()




# группа у Миловидова

from pathlib import Path
#
#
# file_path = Path('info', 'data.txt')
# # file_path = r'info\new.txt'
# print(file_path)
#
# with open(file_path, 'r', encoding='utf8') as text_file:
#     for line in text_file:
#         print(line.strip())
#
#
def creat_file():
    with open('data_new.txt', 'w', encoding='utf-8') as data:
        data.write('Фамилия    Имя    Отчество    Номер     \n')
    return 'data_new.txt'


def readall(nm):
    with open(nm, 'r', encoding='utf8') as txt_file:
        for line in txt_file:
            print(line.strip())

def write_1(nm):
    info_user = []
    str_new1 = input('Фамилия: ')
    info_user.append(str_new1)
    str_new2 = input('Имя: ')
    info_user.append(str_new2)
    str_new3 = input('Отчество: ')
    info_user.append(str_new3)
    str_new4 = input('Телефон: ')
    info_user.append(str_new4)

    with open(nm, 'a', encoding='utf8') as txt_file:
        txt_file.write(f'{info_user[0]} - {info_user[1]} - {info_user[2]} - {info_user[3]} \n')


def find_item(nm):
    item = input('Введите характеристику для поиска: ')
    count = 0
    with open(nm, 'r', encoding='utf8') as txt_file:
        for line in txt_file:
            count += 1
            if item.lower() in line.lower():
                print(f'id - {count} {line}')
        user_comand = input('Выберете действие со строкой (d - удаление, m - изменение, для выхода нажмите ENTER): ')
        if user_comand == 'd':
            user_index = int(input('Введите id строки, которую хотите удалить: '))
            find_del(nm, user_index - 1)
            print('Запись успешно удалена')
        elif user_comand == 'm':
            user_index = int(input('Введите id строки, которую хотите изменить: '))
            find_mod(nm, user_index - 1)



def find_del(nm, i):
    with open(nm, "r", encoding='utf-8') as file:
        lines = file.readlines()
    del lines[i]
    with open(nm, "w", encoding='utf-8') as file:
        file.writelines(lines)


def find_mod(nm, i):
    item_type = int(input('Введите позицию, которую хотите изменить '
                          '(0 - фамилия, 2 - имя, 4 - отчество, 6 - телефон): '))
    with open(nm, 'r', encoding='utf8') as data:
        lines = data.readlines()
        mod_lst = lines[i].split()
    if item_type == 0:
        mod_lst.pop(0)
        mod_lst.insert(0, input('Введите фамилию: '))
        print(mod_lst)
    elif item_type == 2:
        mod_lst.pop(2)
        mod_lst.insert(2, input('Введите имя: '))

    elif item_type == 4:
        mod_lst.pop(4)
        mod_lst.insert(4, input('Введите отчество: '))

    elif item_type == 6:
        mod_lst.pop(6)
        mod_lst.insert(6, input('Введите номер: '))

    mod_line = " ".join(mod_lst)

    with open(nm, "a", encoding='utf-8') as file:
        file.writelines(f'{mod_line}\n')
    user_op = input('Запись успешно изменена. Удалить старую запись? (y - да, нажмите ENTER, если нет):  ')
    if user_op == 'y':
        find_del(nm, i)
        print('Запись успешно удалена')

        # for line in data:
        #     line = line.split()
        #     print(line[0][2])
        #     # if item.lower() in line[item_type].lower():
        #     #     print(*line)


# def delete_contact(file_name):
#     contact_list = read_file_to_list(file_name)
#     number_to_change = search_to_modify(contact_list)
#     contact_list.remove(number_to_change)
#     with open(file_name, 'w', encoding='utf-8') as file:
#         for contact in contact_list:
#             line = ' '.join(contact) + '\n'
#             file.write(line)
# def find_item_2(nm):
#     item = input('Что ищем: ')
#     item_type = int(input('Введите номер (0-фамилия, 1-имя, 2-отчество, 3-телефон): '))
#     with open(nm, 'r', encoding='utf8') as txt_file:
#         for line in txt_file:
#             line = line.split(', ')
#             if item.lower() in line[item_type].lower():
#                 print(*line)


def main():
    while True:
        command = input('Введите команду (q - выход, r - чтение, w - запись, s - поиск): ')
        if command == 'q':
            break
        elif command == 'r':
            if not exists('data_new.txt'):
                print('Файл не создан')
                break
            print(readall('data_new.txt'))
        elif command == 'w':
            if not exists('data_new.txt'):
                creat_file()
                write_1('data_new.txt')
            else:
                write_1('data_new.txt')
        elif command == 's':
            find_item('data_new.txt')


main()
