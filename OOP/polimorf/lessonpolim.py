class P:
    def __init__(self, name):
        self.n = name

    def breathe(self):
        return f'I can breathe'


class Bear(P):
    def __init__(self):
        super().__init__('Миша')

    def breathe(self):
        return f'Я {self.n} и я могу дышать!'


class Human(P):
    def __init__(self):
        super().__init__('Гоша')

    def breathe(self):
        return f'Я {self.n} и я могу дышать!'


misha = Bear()
print(misha.breathe())

gosha = Human()
print(gosha.breathe())
