class Planet:
    def __init__(self, name): #переопределения магического метода инициализации класса; self - ссылка на экземпляр класса
        self.name = name #атрибуты экземпляра класса

    def __str__(self): #магический метод переопределения печати объекта
        return self.name

    def __repr__(self): #магический метод переопределения для интерпретатора Python (внутренее представление объекта)
        return f'Planet {self.name}'

mars = Planet("Mars")
print(mars.name)

mars.name = "Second Earth?"
print(mars.name)

print(mars.mass) #AttributeError

del mars.name
print(mars.name) #AttributeError