fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']


def work_with_phonebook():
    print('Вы вошли в телефонную книгу')
    choice = show_menu()
    while choice != 8:
        phone_book = read_txt('phone.txt')
        if choice == 1:
            print_result(phone_book)
        elif choice == 2:
            last_name = input('Фамилия: ')
            print(find_by_lastname(phone_book, last_name))
        elif choice == 3:
            number = input('Hомер: ')
            print(find_by_number(phone_book, number))
        elif choice == 4:
            last_name = input('Фамилия: ')
            new_number = input('Новый номер: ')
            print_result(change_number(phone_book, last_name, new_number))
        elif choice == 5:
            lastname = input('Фамилия: ')
            name = input('Имя: ')
            number = input('Телефонный номер: ')
            description = input('Описание: ')
            print_result(add_number(phone_book, lastname, name, number, description))
        elif choice == 6:
            lastname = input('Фамилия: ')
            print_result(delete_by_lastname(phone_book, lastname))
        # elif choice == 7:
        #     lastname = input('Фамилия: ')
        #     f = input('В какой файл скопировать: ')
        #     copy_to_another_book(lastname, f)
        choice = show_menu()
    print('Вы вышли из телефонной книги')


def show_menu():
    print("\nВыберите действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Изменить номер абонента\n"
          "5. Добавить абонента\n"
          "6. Удалить абонента\n"
          "7. Скопировать контакт в другой справочник\n"
          "8. Завершить работу")
    choice = int(input())
    return choice


def print_result(phb):
    max_len = 0
    for person in phb:
        for field in fields:
            if len(person[field]) > max_len:
                max_len = len(person[field])
    for field in fields:
        print(f'{field}{' ' * (max_len - len(field))}', end='')
    print()
    print('=' * max_len * len(fields))
    for person in phb:
        for field in fields:
            print(f'{person[field]}{' ' * (max_len - len(person[field]))}', end='')
        print()
        print('-' * max_len * len(fields))


def find_by_lastname(phb, ln):
    for person in phb:
        if person['Фамилия'] == ln:
            return '\t'.join([person[f] for f in fields])
    return 'Абонент не найден'


def find_by_number(phb, n):
    for person in phb:
        if person['Телефон'] == n:
            return '\t'.join([person[f] for f in fields])
    return 'Абонент не найден'


def change_number(phb, ln, nn):
    for person in phb:
        if person['Фамилия'] == ln:
            person['Телефон'] = nn
            write_txt('phone.txt', phb)
            return phb
    return 'Абонент не найден'


def delete_by_lastname(phb, ln):
    for person in range(len(phb)):
        if phb[person]['Фамилия'] == ln:
            del phb[person]
            write_txt('phone.txt', phb)
            return phb
    return 'Абонент не найден'


def add_number(phb, ln, n, phn, d):
    m = [ln, n, phn, d]
    phb.append(dict(zip(fields, m)))
    write_txt('phone.txt', phb)
    return phb


# def copy_to_another_book(ln, f):
#     with open('phone.txt') as source, open(f, 'w') as destination:
#         for line in source:
#             if line.split(',')[0] == ln:
#                 destination.write(line)


def read_txt(filename):
    phone_book = []
    with open(filename, 'r', encoding='utf-8') as phb:
        for line in phb:
            line = line.replace('\n', '')
            record = dict(zip(fields, line.split(',')))
            phone_book.append(record)
    return phone_book


def write_txt(filename, phone_book):
    with open(filename, 'w', encoding='utf-8') as phout:
        for i in range(len(phone_book)):
            s = ''
            for v in phone_book[i].values():
                s = s + v + ','
            phout.write(f'{s[:-1]}\n')


work_with_phonebook()