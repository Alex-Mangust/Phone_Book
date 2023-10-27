

# 1. Распечатать справочник

def print_phone_book(file_open):
    keys_to_fio = ["Фамилия", "Имя"]
    keys_to_data = ["Телефон", "Описание"]
    for i in range(len(file_open)):
        print(i+1, end=": ")
        entry = file_open[i]
        values = [entry[key] for key in keys_to_fio]
        print(*values, end=", ")
        values = [entry[key] for key in keys_to_data]
        print(*values, end="")

# 2. Найти телефон по фамилии

def find_phone_family(file_open):
    print()

# 3. Изменить номер телефона

def change_phone_number():
    print()

# 4. Удалить запись

def delete_record():
    print()

# 5. Найти абонента по номеру телефона

def find_subscriber_by_phone():
    print()

# 6. Добавить абонента в справочник

def add_subscriber_in_phonebook():
    print()
