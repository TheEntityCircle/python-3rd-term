class Event:
 
    def __init__(self, description, event_date):
        self.description = description #описание
        self.date = event_date #дата

    def __str__(self):
        return f"Event \"{self.description}\" at {self.date}"

from datetime import date

event_description = "Рассказать, что такое @classmethod"
event_date = date.today()

event = Event(event_description, event_date)
print(event)



def extract_description(user_string):
    return "открытие чемпионата мира по футболу"


def extract_date(user_string):
    return date(2018, 6, 14)


class Event_Modified:
 
    def __init__(self, description, event_date):
        self.description = description
        self.date = event_date
    
    def __str__(self):
        return f"Event \"{self.description}\" at {self.date}"

    @classmethod #метод класса принимает сам класс
    def from_string(cls, user_input):
        description = extract_description(user_input) #Функция выделения события
        date = extract_date(user_input) #Функция выделение времени
        return cls(description, date) #инициализируем класс и возвращаем экземпляр Event

event = Event_Modified.from_string("добавить в мой календарь открытие чемпионата мира по футболу на 14 июня 2018 года")
print(event)

print(dict.fromkeys("12345")) #пример класс-метода у словаря. Принимает итерабельный объект, возвращает словарь