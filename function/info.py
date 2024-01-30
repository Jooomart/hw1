class Player:
    def __init__(self, name, l_name, age, salary):
        self.name = name
        self.l_name = l_name
        self.age = age
        self.salary = salary

    def print_info(self):
        return f'My name is {self.l_name} {self.name}\nI am {self.age} years old!'

    def my_salary(self):
        return f'My salary:{self.salary}som'


joomart = Player('Joomart', 'Toctogulov', 16, 30000)
print(joomart.print_info())
print(joomart.my_salary())


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return f'My name is {self.name}\nI am {self.age} years old'

    def say_hello(self):
        return f'Здраствуйте {self.name}!'


person1 = Person('Саня', 22)
person2 = Person('Сеня', 21)

print(person1.info(), '\n', person2.info())
print(person1.say_hello(), '\n', person2.say_hello())