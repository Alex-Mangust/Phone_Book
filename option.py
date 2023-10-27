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

def change_phone_number(file_open, filename):
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    confirm_w = False
    while(confirm_w == False):
        family = input("Введите фамилию абонента, номер которого хотетите изменить: ")
        found_phone_record = []
        found_fio_record = []
        found_info_record = []
        for record in file_open:
            if record.get("Фамилия") == family:
                found_phone_record.append(record.get("Телефон"))
                found_fio_record.append(record.get("Фамилия"))
                found_fio_record.append(record.get("Имя"))
                found_info_record.append(record.get("Описание"))
        fio = "".join(found_fio_record)
        info = "".join(found_info_record)
        if found_phone_record:
            for record in found_phone_record:
                print(f"Абонент - {fio}. Телефон - {record}. Описание - {info}")
        else:
            print("Абонент не найден")
        confirm = input("Все верно?\n1 - да   2 - нет\n")
        if confirm == "1":
            confirm_w = True
        else:
            confirm_w = False
    new_phone = input("Введите новый номер телефона: ")
    for record in file_open:
        if record["Фамилия"] == family:
            record["Телефон"] = new_phone
    with open(filename, 'w', encoding='utf-8') as phb:
        for record in file_open:
            line = ','.join(record[field] for field in fields)
            phb.write(line)

# 4. Удалить запись

def delete_record(file_open, filename):
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    confirm_w = False
    while(confirm_w == False):
        family = input("Введите фамилию абонента, запись о котором вы хотите удалить: ")
        found_phone_record = []
        found_fio_record = []
        found_info_record = []
        for record in file_open:
            if record.get("Фамилия") == family:
                found_phone_record.append(record.get("Телефон"))
                found_fio_record.append(record.get("Фамилия"))
                found_fio_record.append(record.get("Имя"))
                found_info_record.append(record.get("Описание"))
        fio = "".join(found_fio_record)
        info = "".join(found_info_record)
        if found_phone_record:
            for record in found_phone_record:
                print(f"Абонент - {fio}. Телефон - {record}. Описание - {info}")
        else:
            print("Абонент не найден")
        confirm = input("Все верно?\n1 - да   2 - нет\n")
        if confirm == "1":
            confirm_w = True
        else:
            confirm_w = False
    # new_phone = input("Введите новый номер телефона: ")
    # for record in file_open:
    #     if record["Фамилия"] == family:
    #         record["Телефон"] = new_phone
    record_delete = 0
    for i in range(len(file_open)):
        if file_open[i].get("Фамилия") == family:
            record_delete = i
    del file_open[record_delete]
    with open(filename, 'w', encoding='utf-8') as phb:
        for record in file_open:
            line = ','.join(record[field] for field in fields)
            phb.write(line)

# 5. Найти абонента по номеру телефона

def find_subscriber_by_phone(file_open):
    phone = input("Введите номер телефона абонента: ")
    found_phone_record = []
    found_fio_record = []
    found_info_record = []
    for record in file_open:
        if record.get("Телефон") == phone:
            found_phone_record.append(record.get("Телефон"))
            found_fio_record.append(record.get("Фамилия"))
            found_fio_record.append(record.get("Имя"))
            found_info_record.append(record.get("Описание"))
    fio = "".join(found_fio_record)
    info = "".join(found_info_record)
    if found_phone_record:
        for record in found_phone_record:
            print(f"Абонент {fio}. Телефон - {record}. Описание - {info}")
    else:
        print("Абонент не найден")

# 6. Добавить абонента в справочник

def add_subscriber_in_phonebook(file_open, filename):
    print()