import random

num = random.randint(1, 20)

trys: int = 1
errors = 0
listok = []

while True:
    try:
        def loto(i):
            if i == num:
                return True
            elif num - 3 <= i <= num + 3:
                print('Вы близки к цели!')


        while True:
            num_1 = int(input('Отгадайте загадонное число:'))
            if type(num_1) == int:
                listok.append(num_1)
            resulte = loto(num_1)
            if resulte:
                print('Вы отгадали загадонное число!')
                print(f'Количесвто попыток: {trys} \nКоличесвто ошибок: {errors} \nПриведенные цифры:{listok}')
                break
            else:
                print('Вы не отгадали число.Пробуйте дальше!')
                trys += 1
                continue
    except Exception as o:
        errors += 1
        print('Ошибка, делайте все правильно!')
        continue
    else:
        break
