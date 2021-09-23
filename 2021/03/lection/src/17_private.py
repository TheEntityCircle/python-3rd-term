
import json

class Pet:
    def __init__(self, name):
        self.name = name

class Dog(Pet):
    def __init__(self, name, breed = None):
        super().__init__(name) #инициализация базового класса
        self.__breed = breed

    def say(self):
        return "{0}: гав-гав!".format(self.name)

    def get_breed(self):
        return self.__breed

class ExportJSON:
    def to_json(self):
        return json.dumps({
            "name" : self.name,
            "breed" : self.breed
        })

class ExDog(Dog, ExportJSON):
    def get_breed(self):
        return "порода: {0} - {1}".format(self.name, self._Dog__breed)

dog = ExDog("Фокс", "Мопс")
print(dog.get_breed()) #AttributeError
print(dog.__dict__)