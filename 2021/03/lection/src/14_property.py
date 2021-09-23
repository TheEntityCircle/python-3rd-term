#вычисляемые свойства. Позволяют изменять поведение и выполнять какую-то вычислительную работы при обращении к атрибуту/изменении/удалении

class Robot:

    def __init__(self, power):
        self.power = power

wall_e = Robot(100)
wall_e.power = 200
print(wall_e.power)
wall_e.power = -20 #not valid

#example 1. Программисту придется менять свой код, если он уже используется
class Robot_With_Set:

    def __init__(self, power):
        self.power = power
    
    def set_power(self, power):
        if power < 0:
            self.power = 0
        else:
            self.power = power

wall_e = Robot_With_Set(100)
wall_e.set_power(-20)
print(wall_e.power)


#example 2. Properties
class Robot_Property:
 
    def __init__(self, power):
        self._power = power

    power = property() #объект property
    
    #переопределение метода модифицирования
    @power.setter
    def power(self, value):
        if value < 0:
            self._power = 0
        else:
            self._power = value

    #переопределение метода обращения/чтения
    @power.getter
    def power(self):
        return self._power
    
    #переопределение метода удаления
    @power.deleter
    def power(self):
        print("make robot useless")
        del self._power

wall_e = Robot_Property(-20)
wall_e.power = -20
print(wall_e.power)
del wall_e.power


#example 3. Property
class Robot_Property_1:
 
    #модифицирование уникального свойства при чтении
    @property
    def power(self):
        # здесь могут быть любые полезные вычисления
        return self._power

wall_e = Robot(200)
wall_e.power