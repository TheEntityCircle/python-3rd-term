class Human:
    def __new__(cls, *args, **kwargs): #переопределение действий с экземпляром до его инциализации
        print("__new__ called")
        obj = super().__new__(cls) #создание нового экземпляра класса. super() - родитель Object
        return obj

    def __init__(self, name):
        print("__init__ called")
        self.name = name

    def __del__(self): #переопределение специального метода деструктора. Лучше не определять - нет гарантий, что он будет вызван. 
        #Лучше определить методы экземпляра закрытия
        print(f"Goodbye, {self.name}!")

human = Human("Petya")
#del human

#что на самом деле происходит
human_manual = Human.__new__(Human, "Ivan") #на вход класс, аргумент экземпляра
if isinstance(human_manual, Human): #если все ок
    Human.__init__(human_manual, "Ivan") #инициализируем

