class Planet:
    def __init__(self, name): #переопределения магического метода инициализации класса; self - ссылка на экземпляр класса
        self.name = name #атрибуты экземпляра

    def __str__(self): #магический метод переопределения печати объекта
        return self.name

earth = Planet("Earth") #init вызывается автоматически
print(earth.name) #обращение к атрибуту с помощью точки
print(earth) 
