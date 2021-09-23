class Human: #CamelCase
    pass #Блок пространства имен(suite)

class Robot:
    """Данный класс позволяет создавать роботов""" #docstring - cтрока документирования

print(Robot) #__main__ - модуль + название класса

print(dir(Robot)) #много методов


class Planet: #Описание абстрактной планеты
    pass

planet = Planet() #экземпляр/объекта класса
print(planet) #object at 0x...

solar_system = []
for i in range(8):
    planet 