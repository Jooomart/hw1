import csv

information = [
    ['Name', 'Age', 'City', 'Phone'],
    ['Chynar', '61', 'Bishkek', '0558038838'],
    ['Eliza', '42', 'Bishkek', '0501854307']
]
with open('primer.csv', 'w', newline='') as file:
    w = csv.writer(file)
    w.writerows(information)


def read_csv(a):
    with open(a, 'r') as file:
        reader = csv.reader(file)
        for i in reader:
            print(i)


file_path = input('File path:')
read_csv(file_path)

with open('primer.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    headers = next(reader)
    for i in reader:
        Name = i
        print(f'Мое имя: {Name}')


with open('primer.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for i in reader:
        if int(i['Age']) >= 26:
            print(i['Age'])


def r(file_path, new_data):
    try:
        with open(file_path, 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=new_data.keys())
            writer.writerow(new_data)
    except Exception as e:
        print(f"Произошла ошибка при добавлении данных: {e}")


dictionary = {'Name': 'Joomart', 'Age': '16', 'City': 'Bishkek', 'Phone': '0708341585'}

r('primer.csv', dictionary)
with open('primer.csv', 'r', encoding='utf-8') as file1:
    for i in file1:
        print(i)


row_index = int(input("Укажите строку значения:"))
column_index = int(input("Укажите столбец значения:"))

new_value = input('Новое значение:')
with open('primer.csv', 'r', newline='') as file:
    reader = csv.reader(file)
    formar_rows = list(reader)
    formar_rows[row_index][column_index] = new_value

with open('primer.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(formar_rows)
with open('primer.csv', 'r', newline='') as file:
    for i in file:
        print(i)

with open('primer.csv', 'r', newline='') as file:
    reader = csv.reader(file)
    rows = [i for i in reader if i[1] <= '50']
with open('primer.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(rows)

with open('primer.csv', 'r', newline='') as file:
    for i in file:
        print(i)
