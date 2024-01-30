class Ticher:
    def __init__(self, name):
        self.n = name
        self.les = []
        self.rosp = {
            'Понедельник': [],
            'Вторник': [],
            'Среда': [],
            'Четверг': [],
            'Пятница': [],
            'Суббота': [],
            'Воскресенье': [],
        }

    def append_lesson(self, *args):
        for lesson in args:
            if lesson in self.les:
                print(f'Урок {lesson} уже находится в списке!\n')
                continue
            else:
                self.les.append(lesson)
                print(f'Предмет {lesson} был добавлен в список!\n')

    def del_lesson(self, lesson):
        if lesson in self.les:
            self.les.remove(lesson)
            print(f'Предмет {lesson} был убран!\n')
        else:
            print('Данный предмет не находится в списке предметов данного учителя!\n')

    def app_rosp(self, day, *args):
        for lesson in args:
            if day not in self.rosp:
                print('Такой день недели не существует!\n')
                break
            elif lesson not in self.les:
                print(f'Предмет {lesson} не находится в списке предметов этого учителя!\n')
                continue
            elif day in self.rosp and lesson in self.rosp[day]:
                print(f'Предмет {lesson} уже в расписании этого дня!\n')
                continue
            else:
                self.rosp[day].append(lesson)
                print(f'Предмет {lesson} был добавлен в расписание дня {day}!\n')

    def del_rosp(self, day, lesson):
        if day not in self.rosp:
            print('Такой день недели не существует!\n')
        elif lesson not in self.rosp[day]:
            print(f'Предмет {lesson} не находится в расписании этого дня!\n')
        else:
            self.rosp[day].remove(lesson)
            print(f'Предмет {lesson} был убран из расписания дня {day}!\n')


ticher = Ticher('Жоомарт')
ticher.append_lesson('Биология', 'Физика', 'Литература')
ticher.app_rosp('Вторник', 'Биология', 'Физика', 'Физика', 'Литература', 'Мировая история')
