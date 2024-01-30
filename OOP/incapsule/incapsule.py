class MBank:
    def __init__(self, name: str, s_name: str):
        self.n = name
        self.s_n = s_name
        self.__cash = 0
        self.vip = False
        self.s_limit = 0

    def verification(self):
        self.vip = True
        if self.__cash >= 10000:
            self.__cash -= 10000

            print(f'Вы прошли верификацию и теперь ваш статус VIP')
        else:
            print(f'У вас не достаточно средств чтобы получить статус VIP. Стоимость статуса VIP: 10000сом')

    def get__cash(self):
        return f'Баланс: {self.__cash} сом'

    def set__cash(self, x):
        self.__cash += x
        return f'Ваш баланс пополнен на:{x}сом...'

    def info(self):
        return f'Имя:{self.n} \nФамилия:{self.s_n}'

    def __shop(self, x):
        if self.__cash >= x:
            if self.vip:
                return True
            elif not self.vip:
                if self.s_limit + x <= 50000:
                    return True
                else:
                    return 'no vip'
        else:
            return False

    def kom(self, x):
        if x <= 50000:
            if self.__shop(x) == True:
                self.__cash -= (x + (x / 100 * 3))
                self.s_limit += (x + (x / 100 * 3))
                print(f'Транзакция прошла успешно!\nОстаток на балансе:{self.__cash}сом...')
            elif self.__shop(x) == False:
                print(f'Не достаточно средств.')
            elif self.__shop(x) == 'no vip':
                print(f'Ваш лимит был превышен.\nКупите VIP статус!')
        elif x > 50000:
            if self.__shop(x) == True:
                self.__cash -= (x + (x / 100 * 1.2 + 100))
                self.s_limit += (x + (x / 100 * 1.2 + 100))
                print(f'Транзакция прошла успешно!\nОстаток на балансе:{self.__cash}сом...')
            elif self.__shop(x) == False:
                print(f'Не достаточно средств.')
            elif self.__shop(x) == 'no vip':
                print(f'Ваш лимит был превышен.\nКупите VIP статус!')


joomart = MBank('Жоомарт', 'Токтогулов')
joomart.set__cash(100000)
joomart.kom(50001)

#1
