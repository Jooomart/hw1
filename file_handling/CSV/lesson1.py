import csv
information = [
    ['Name', 'Age', 'City', 'Phone'],
    ['Chynar', '61', 'Bishkek', '0558038838'],
    ['Eliza', '42', 'Bishkek', '0501854307']
]
with open('primer.csv', 'w', newline='') as file:
    csv_w = csv.writer(file)
    csv_w.writerows(information)