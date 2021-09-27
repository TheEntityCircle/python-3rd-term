class Planet:
    def __init__(self, name): #переопределения магического метода инициализации класса; self - ссылка на экземпляр класса
        self.name = name #атрибуты экземпляра

    def __str__(self): #магический метод переопределения печати объекта
        return self.name

    def __repr__(self): #магический метод переопределения для интерпретатора Python (внутренее представление объекта)
        return f'Planet {self.name}'

planet_names = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")

solar_system = []
for name in planet_names:
    planet = Planet(name)
    solar_system.append(planet)

print(solar_system)

