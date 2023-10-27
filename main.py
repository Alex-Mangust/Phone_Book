import option
import sys

def show_menu():
    print('1. Распечатать справочник',
          '2. Найти телефон по фамилии',
          '3. Изменить номер телефона',
          '4. Удалить запись',
          '5. Найти абонента по номеру телефона',
          '6. Добавить абонента в справочник',
          '7. Закончить работу', sep='\n')
    choice = input("Выберите опцию: ")
    return choice


def read_txt(filename):
    phone_book = []
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    with open(filename, 'r', encoding='utf-8') as phb:
        for line in phb:
            values = line.strip().split(',')
            record = dict(zip(fields, values))
            phone_book.append(record)
    return phone_book


def work_with_phonebooke():
    choice = show_menu()
    while choice != 7:
        if choice == "end" or choice == "End":
            sys.exit()
        elif choice.isdigit() == False:
            print("Недопустимый выбор. Выберите от 1 до 7.\n\n")
        else:
            choice = int(choice)
            if choice == 1:
                print("Опция 1 выбрана: Распечатать справочник", end="\n\n")
                option.print_phone_book(read_txt("phonebook.csv"))
            elif choice == 2:
                print("Опция 2 выбрана: Найти телефон по фамилии", end="\n\n")
                option.find_phone_family(read_txt("phonebook.csv"))
            elif choice == 3:
                print("Опция 3 выбрана: Изменить номер телефона")
                option.change_phone_number(read_txt("phonebook.csv"), "phonebook.csv")
            elif choice == 4:
                print("Опция 4 выбрана: Удалить запись")
                option.delete_record(read_txt("phonebook.csv"), "phonebook.csv")
            elif choice == 5:
                print("Опция 5 выбрана: Найти абонента по номеру телефона")
                option.find_subscriber_by_phone(read_txt("phonebook.csv"))
            elif choice == 6:
                print("Опция 6 выбрана: Добавить абонента в справочник")
                option.add_subscriber_in_phonebook(read_txt("phonebook.csv"), "phonebook.csv")
            else:
                print("Недопустимый выбор. Выберите от 1 до 7.")
            print(end="\n\n")
            next = input("Чтобы продолжить, введите любое значение: ")
        choice = show_menu()


work_with_phonebooke()
