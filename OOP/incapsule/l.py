class Passport:
    def __init__(self, name, age, job, living_adres):
        self.__name = name
        self.age = age
        self.job = job
        self._l_a = living_adres

    def info_about_person(self):
        print(f"Имя:{self.__name}, Возраст:{self.age}, Место работы:{self.job}, Место проживания:{self._l_a}")

    # def biografy(self):


class Joma(Passport):
    def __init__(self, __name, age, job, _l_a):
        super().__init__(__name, age, job, _l_a)


person_joma = Joma('Жоомарт', 16, 'Progger', 'АК-ОРДО-3 83')
person_joma.info_about_person()
person_joma.name = 'JOMA' #не изменит артрибут
person_joma.info_about_person()
person_joma.l_a = 'dklfjfdkgfn' #не изменит артребут
person_joma.info_about_person()
