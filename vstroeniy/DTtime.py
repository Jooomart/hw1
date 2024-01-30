from datetime import datetime


def dr(birthday):
    today = datetime.now()
    birthday = datetime(today.year, birthday.month, birthday.day)
    if today > birthday:
        birthday = datetime(today.year + 1, birthday.month, birthday.day)
    day = (birthday - today).days
    return day


while True:
    try:
        birthday_str = input("Введите дату своего дня рождения(****-**-**): ")
        birthday = datetime.strptime(birthday_str, "%Y-%m-%d")
        days_left = dr(birthday)
        print(f"До вашего дня рождения осталось {days_left} дней.")
    except Exception:
        print("Некорректный формат даты.")
    else:
        break
