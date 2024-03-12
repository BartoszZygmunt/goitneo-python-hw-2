from datetime import datetime

input_data = [
    {'name': 'John Nowak', 'birthday': datetime(1995, 10, 28)},
    {'name': 'Alice Smith', 'birthday': datetime(1987, 3, 13)},
    {'name': 'David Johnson', 'birthday': datetime(1990, 3, 8)},
    {'name': 'Emily Davis', 'birthday': datetime(1998, 7, 16)},
    {'name': 'Michael Brown', 'birthday': datetime(1985, 9, 4)},
    {'name': 'Olivia Wilson', 'birthday': datetime(1992, 12, 20)},
    {'name': 'James Taylor', 'birthday': datetime(1996, 2, 2)},
    {'name': 'Sophia Anderson', 'birthday': datetime(1989, 6, 10)},
    {'name': 'Daniel Martinez', 'birthday': datetime(1993, 11, 14)},
    {'name': 'Isabella Thomas', 'birthday': datetime(1997, 3, 15)},
    {'name': 'Joseph Lee', 'birthday': datetime(1991, 8, 18)},
    {'name': 'Mia Harris', 'birthday': datetime(1988, 3, 15)},
    {'name': 'Alexander Clark', 'birthday': datetime(1994, 10, 9)},
    {'name': 'Abigail Lewis', 'birthday': datetime(1986, 5, 22)},
    {'name': 'William Young', 'birthday': datetime(1989, 3, 14)},
    {'name': 'Charlotte Walker', 'birthday': datetime(1999, 7, 12)},
    {'name': 'Ethan Hall', 'birthday': datetime(1984, 9, 26)},
    {'name': 'Ava Allen', 'birthday': datetime(1992, 12, 8)},
    {'name': 'Benjamin King', 'birthday': datetime(1996, 1, 18)},
    {'name': 'Sofia Scott', 'birthday': datetime(1987, 3, 19)}
]

weekdays_en = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
weekdays_pl = ['Poniedziałek', 'Wtorek', 'Środa', 'Czwartek', 'Piątek', 'Sobota', 'Niedziela']
weekdays_de = ['Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag', 'Samstag', 'Sonntag'] 
weekdays_fr = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']

choice_lang = 'en' # 'pl', 'de', 'fr', 'en'

if choice_lang == 'en':
    weekdays = weekdays_en
elif choice_lang == 'pl':
    weekdays = weekdays_pl
elif choice_lang == 'de':
    weekdays = weekdays_de
elif choice_lang == 'fr':
    weekdays = weekdays_fr
else:
    weekdays = weekdays_en


def get_birthdays_per_week(users):
    result = {}
    today = datetime.today().date()
    
    for user in users:
        name = user['name']
        birthday = user['birthday'].date()

        birthday_this_year = datetime(today.year, birthday.month, birthday.day).date()

        if birthday_this_year < today:
            pass
        else:
            delta_days = (birthday_this_year - today).days
            if delta_days < 7:
                weekday = weekdays[birthday_this_year.weekday()]
                if weekday in result:
                    result[weekday] += (', ' + name)
                else:
                    result[weekday] = name

    for k, v in result.items():
        print(k, v)


get_birthdays_per_week(input_data)


    

    