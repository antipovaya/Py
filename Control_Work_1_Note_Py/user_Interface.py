from note import Note

def menu():
    print(
        "\nЭто программа 'Заметки'.Имеются следующие функции:\n\n1 - вывод всех заметок из файла\n2 - "
        "добавление заметки\n3 - удаление заметки\n4 - редактирование заметки\n5 - выборка заметок "
        "по дате\n6 - показать заметку по id\n7 - выход\n\nВведите номер функции: ")

def check_len_text_input(text, number):
    while len(text) <= number:
        print(f'Текст должен быть больше {number} символов\n')
        text = input('Введите тескт: ')
    else:
        return text
def create_note(num):
    title = check_len_text_input(
        input('Введите Название заметки: '), num)
    body = check_len_text_input(
        input('Введите Описание заметки: '), num)
    return Note(title=title, body=body)

def goodbye():
    print("До свидания!")