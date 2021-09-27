class Human:
    def __init__(self, name, age=0):
        self._name = name
        self._age = age
 
    def _say(self, text): #нижнее подчеркивание - это соглашение в котором данным атрибутом нельзя пользоваться на прямую
        #могут данный метод модифицировать либо отказаться
        print(text)
 
    def say_name(self):
        self._say(f"Hello, I am {self._name}")
 
    def say_how_old(self):
        self._say(f"I am {self._age} years old")


bob = Human("Bob", age=29)
bob.say_name()
bob.say_how_old()

print(bob._name) #не рекомендуется !
print(bob._say("Bla-bla-bla")) #не рекомендуется !