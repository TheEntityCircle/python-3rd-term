class Planet:
    """Класс планеты"""
    count = 0 #переменная класса или атрибут класса

    def __init__(self, name, population = None):
        self.name = name
        self.population = population or []
        Planet.count += 1

earth = Planet("Earth")
marss = Planet("Mars")
print(Planet.count) #через класс
print(earth.count) #через экземпляр. Ищет атрибут экземпляра, далее атрибут класса

#Атрибут класса != Атрибуту экземпляра

print(earth.__dict__) #свойство dict, словарь атрибуты экземпляра класса(Python ищет тут атрибуты)
earth.mass = 5.97e24 #так делать можно, но не нужно
print(earth.__dict__)

print(Planet.__dict__) #словарь атрибутов класса. Есть count
print(Planet.__doc__) #обращение к атрибуту класса
print(earth.__doc__) #поиск атрибута класса через экземпляр

print(dir(earth)) #все методы экземпляра
print(earth.__class__) #название класса, к которому он принадлежит