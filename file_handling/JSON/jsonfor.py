import json


def write(data):
    with open('jsonles.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)
    with open('jsonles.json', 'r', encoding='utf-8') as file:
        print(json.load(file))


data = {
    'email': 'tcjm@gmail.com',
    'Password': '1234'
}
write(data)

book_info = {
    'nazvanie': 'песня пламени и льда',
    'god vypuska': '1996',
    'avtor': 'Джордж Мартин',
    'colichestvo str': '800'
}

write(book_info)

import json


def pretti_print(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        json_data = json.load(file)

    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(json_data, file, indent=4, ensure_ascii=False)

    print(json.dumps(json_data, indent=4, ensure_ascii=False))


pretti_print('jsonles.json')


students_info = [
    {"имя": "Иван", "фамилия": "Иванов", "возраст": 20},
    {"имя": "Мария", "фамилия": "Петрова", "возраст": 22},
    {"имя": "Алексей", "фамилия": "Сидоров", "возраст": 21}
]


def info(students_info, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(students_info, file, indent=4, ensure_ascii=False)
        print(f"Информация о студентах успешно сохранен.")
    with open(file_path, 'r', encoding='utf-8') as file:
        json_reader = json.load(file)
        print(json_reader)


info(students_info, 'jsonles.json')