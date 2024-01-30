def plus(a, b):
    return a + b


def minus(a, b):
    return a - b


def delen(a, b):
    return a / b


def umnoj(a, b):
    return a * b


def delen_module(a, b):
    return a // b


def delen_ostat(a, b):
    return a % b


while True:
    try:
        a = int(input('Введите число:'))
        b = int(input('введите число:'))
        c = input('Какой процесс вам необходим?(+, -, /, *, //, %)')
        if c == '+':
            print(f'Результат:{plus(a, b)}')
        elif c == '-':
            print(f'Результат:{minus(a, b)}')
        elif c == '/':
            print(f'Результат:{delen(a, b)}')
        elif c == '*':
            print(f'Результат:{umnoj(a, b)}')
        elif c == '//':
            print(f'Результат:{delen_module(a, b)}')
        elif c == '%':
            print(f'Результат:{delen_ostat(a, b)}')
        else:
            print('Вы не правильно ввели нужный процесс!')
            l = input('Хотите продолжить/повторить?(y/n):')
            if l == 'y':
                continue
            else:
                break
    except (ValueError, TypeError, ZeroDivisionError) as i:
        print(f'Произошла ошибка:{i}')
        continue
