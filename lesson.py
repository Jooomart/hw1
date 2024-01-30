a = int(input('Введите число:'))
ad = lambda num: num * 2
print(ad(a))

ad1 = lambda num:  num % 2 == 0
print(ad1(a))

ad2 = lambda x, turn: x + turn
b = int(input('Введите число:'))
print(ad2(a, b))

Listok = ['hell', 'gun', 'blood']

nom4 = lambda x: sorted(x, key=lambda x: x[-1])

print(nom4(Listok))

numb = [1, 2, 3, 4, 5]

j = list(filter(lambda x: x % 2 == 0, numb))

print(j)


try:
    raise NameError('HiThere')
except NameError:
    print('Исключение пролетело незаметно!')
