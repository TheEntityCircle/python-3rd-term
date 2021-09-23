class Pet:
    def __init__(self, name):
        self.name = name

class Dog(Pet):
    def __init__(self, name, breed = None):
        super().__init__(name) #инициализация базового класса
        self.breed = breed

    def say(self):
        return "{0}: гав-гав!".format(self.name)

dog = Dog("Тузик", "Пудель")
print(dog.say())

print(issubclass(int, object))
print(issubclass(Dog, object))
print(issubclass(Dog, Pet))
print(issubclass(Dog, int))

print(isinstance(dog, Dog))
print(isinstance(dog, Pet))
print(isinstance(dog, object))