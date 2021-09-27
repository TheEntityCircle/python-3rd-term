import json

class PetExport:
    def export(self, dog):
        raise NotImplementedError

class ExportJSON(PetExport):
    def export(self, dog):
        return json.dumps({
            "name" : dog.name,
            "breed" : dog.breed
        })

class ExportXML(PetExport):
    def export(self, dog):
        return """<?xml version ="1.0" encoding="utf-8"?>
        <dog>
            <name>
            {0}
            </name>
            <breed>
            {1}
            </breed>
        </dog> 
        """.format(dog.name, dog.breed)


class Pet:
    def __init__(self, name):
        self.name = name

class Dog(Pet):
    def __init__(self, name, breed = None):
        super().__init__(name) 
        self.breed = breed

    def say(self):
        return "{0}: гав-гав!".format(self.name)  

class ExDog(Dog):
    def __init__(self, name, breed=None, exporter = None):
        super().__init__(name, breed=breed)
        self._exporter = exporter or ExportJSON()
    
    def export(self):
        self._exporter.export(self)

dog = ExDog("Шарик", "Дворняга", exporter=ExportXML())
print(dog.export())
