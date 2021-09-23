class Human:
 
    def __init__(self, name, age=0):
        self.name = name
        self.age = age

    @staticmethod #этот метод не связан с классом. Статический метод - вопрос организации кода. Можно обращаться относительно имени класса
    def is_age_valid(age):
        return 0 < age < 150

# можно обращаться от имени класса
print(Human.is_age_valid(35))

# или от экземпляра:
human = Human("Old Bobby")
print(human.is_age_valid(234))