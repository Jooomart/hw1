# class Animal:
#     def __init__(self, name, age):
#         self.n = name
#         self.a = age
#
#     def breathe(self):
#         print(f'Это животное способно дышать!')
#
#     def info(self):
#         return f'Это наш питомец {self.n}, ему {self.a} лет!'
#
#
# class Dog(Animal):
#
#     def voice(self):
#         print('Собака может лаять!')
#
#
# class Cat(Animal):
#     def voice(self):
#         print('Кошка может мяукать!')
#
#
# dog = Dog('Барсик', 7)
# print(dog.info())
# dog.voice()
# cat = Cat('Снежок', 9)
# print(cat.info())
# cat.voice()
#
#
# class Avto:
#     def __init__(self, mark, made_age):
#         self.n = mark
#         self.a = made_age
#
#     def avto_info(self):
#         print(f'Это машина марки {self.n}. Ее год выпуска: {self.a}')
#
#
# class SportCar(Avto):
#     def __init__(self, n, a, max_speed):
#         super().__init__(n, a)
#         self.maxs = max_speed
#
#     def alii_info(self):
#         print(f'Это машина марки {self.n}. Ее год выпуска: {self.a}. Ее максимальная скорость: {self.maxs}')
#
#
# car1 = SportCar('Tayota', 1998, 270)
# car1.alii_info()
#
#
# class Fruit:
#     def eat(self):
#         print("съесть")
#
#
# class Apple(Fruit):
#     def eat(self):
#         print("Яблоко съедено")
#
# apple = Apple()
# apple.eat()

#
# class Person:
#     name = 'Joomart'
#     age = 26
#     balance = 3450000
#
#     def __init__(self, breathe, eat):
#         self.b = breathe
#         self.e = eat
#
#     def info(self):
#         print(f'{self.name}, {self.age}, {self.balance}, \n{self.b}, {self.e}')
#
#
# class Bakyt(Person):
#     name = 'Bakyt'
#     age = 5
#     balance = 50
#
#     def __init__(self):
#         super().__init__('дышу ', 'кушаю')
#
#
# ata = Person('могу дышать', 'могу есть')
# ata.info()
# bakyt = Bakyt()
# bakyt.info()

# class Computer:
#     b = 'Lenova'
#     m = 'ideapad3'
#
#     def desplay_info(self):
#         print(f'{self.b} {self.m}')
#
#
# comp = Computer()
# comp.desplay_info()
#
#
# class CPU(Computer):
#     cores = '8 ядер'
#
#     def __init__(self):
#         super().__init__()
#
#     def desplay_info(self):
#         print(f'{self.b} {self.m} {self.cores}')
#
#
# comp = CPU()
# comp.desplay_info()
#
#
# class GPU(Computer):
#     vram = '256 Mbite'
#
#     def __init__(self):
#         super().__init__()
#
#     def desplay_info(self):
#         print(f'{self.b} {self.m} {self.vram}')
#
#
# comp = GPU()
# comp.desplay_info()
#

class Computer:
    def __init__(self, brand, model):
        self.b = brand
        self.m = model
        self.power = True

    def info(self):
        print(f'{self.b} {self.m}')

    def powered_on(self):
        if not self.power:
            print(f'{self.b} {self.m} включен')
            self.power = True
        else:
            print(f'{self.b} {self.m} уже включенный')

    def powered_off(self):
        if self.power:
            print(f'{self.b} {self.m} выключен')
            self.power = False
        else:
            print(f'{self.b} {self.m} уже выключенный')

    def display_status(self):
        status = 'включен' if self.power else 'выключен'
        print(f"{self.b} {self.m} сейчас {status}.")


my_comp = Computer('lenova', 'ideapad3')
my_comp.powered_on()
my_comp.powered_off()
my_comp.display_status()


class Laptop(Computer):
    def __init__(self, b, m, battary_live):
        super().__init__(b, m)
        self.b_l = battary_live

    def info(self):
        print(f"Брэнд:{self.b} Модель:{self.m} Время работы от аккамулятора:{self.b_l}минут.")


laptop = Laptop('Lenova', 'Ideapad3', 300)
laptop.info()