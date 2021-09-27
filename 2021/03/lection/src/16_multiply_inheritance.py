import json

class Pet:
    def __init__(self, name):
        self.name = name

class Dog(Pet):
    def __init__(self, name, breed = None):
        super().__init__(name) #инициализация базового класса. 
        self.breed = breed

    def say(self):
        return "{0}: гав-гав!".format(self.name)

class ExportJSON:
    def to_json(self):
        return json.dumps({
            "name" : self.name,
            "breed" : self.breed
        })

class ExDog(Dog, ExportJSON):
    def __init__(self, name, breed=None):
        super().__init__(name, breed) #Вызов метода по MRO
        #super(ExDog, self).__init__(name)

class WooleanDog(Dog, ExportJSON):
    def __init__(self, name, breed=None):
        super(Dog, self).__init__(name, breed=breed) #явное указание конкретного класса
        self.breed = "Шерстянная собака породы {0}".format(breed)

dog = ExDog("Тузик", breed = "Пудель")
print(dog.to_json())

#method resolution order
print(ExDog.__mro__)