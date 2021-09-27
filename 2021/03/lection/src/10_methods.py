#Методы - это функции, которые действуют в контектсе экземпляра класса

class Human:

    def __init__(self, name, age=0):
        self.name = name
        self.age = age


class Planet:

    def __init__(self, name, population=None):
        self.name = name
        self.population = population or []
 
    def add_human(self, human): #функция/метод который принимает ссылку на экземпляр и переменную human. Можно использовать return
        print(f"Welcome to {self.name}, {human.name}!")
        self.population.append(human)

mars = Planet("Mars")

bob = Human("Bob")

mars.add_human(bob)
print(mars.population)