from os.path import exists


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


def main():
    while True:
        command = input('Введите команду (q - выход, r - чтение, w - запись, s - поиск): ')  # удаление и изменение
        if command == 'q':                                                                   # сделала в поиске
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
