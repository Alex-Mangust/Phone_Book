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
    family = input("Введите фамилию абонента: ")
    found_phone_record = []
    found_fio_record = []
    for record in file_open:
        if record.get("Фамилия") == family:
            found_phone_record.append(record.get("Телефон"))
            found_fio_record.append(record.get("Фамилия"))
            found_fio_record.append(record.get("Имя"))
    fio = "".join(found_fio_record)
    if found_phone_record:
        for record in found_phone_record:
            print(f"Телефон абонента {fio} -{record}")
    else:
        print("Абонент не найден")

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
