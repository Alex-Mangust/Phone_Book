import option
def show_menu():
    print('1. Распечатать справочник',
    '2. Найти телефон по фамилии',
    '3. Изменить номер телефона',
    '4. Удалить запись',
    '5. Найти абонента по номеру телефона',
    '6. Добавить абонента в справочник',
    '7. Закончить работу', sep = '\n')
    choice = int(input("Выберите опцию: "))
    return choice

def read_txt(filename):
    phone_book = []
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']

    with open(filename, 'r', encoding='utf-8') as phb:
        for line in phb:
            record = dict(zip(fields, line.split(',')))
            phone_book.append(record)
    return phone_book

def work_with_phonebooke():
    choice = show_menu()
    while choice != 7:
        if choice == 1:
            print("Опция 1 выбрана: Распечатать справочник", end="\n\n")
            option.print_phone_book(read_txt("phonebook.txt"))
        elif choice == 2:
            print("Опция 2 выбрана: Найти телефон по фамилии", end="\n\n")
            option.find_phone_family(read_txt("phonebook.txt"))
        elif choice == 3:
            print("Опция 3 выбрана: Изменить номер телефона")
            option.change_phone_number(read_txt("phonebook.txt"), "phonebook.txt")
        elif choice == 4:
            print("Опция 4 выбрана: Удалить запись")
            option.delete_record(read_txt("phonebook.txt"), "phonebook.txt")
        elif choice == 5:
            print("Опция 5 выбрана: Найти абонента по номеру телефона")
            # Здесь вы можете добавить код для поиска абонента по номеру телефона.
        elif choice == 6:
            print("Опция 6 выбрана: Добавить абонента в справочник")
            # Здесь вы можете добавить код для добавления абонента в справочник.
        else:
            print("Недопустимый выбор. Выберите от 1 до 7.")
        print(end="\n\n")
        next = int(input("Чтобы продолжить, введите 1: "))
        if next == 1:
            choice = show_menu()
        else:
            choice = 7

work_with_phonebooke()
