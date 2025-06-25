class NamePrint():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def printname(self):
        return f"my name is {self.name} and {self.age}"
obj1 = NamePrint("ram",15)
print(obj1.printname())

class Lamp():
    def __init__(self,a):
        self.is_on = a
    def printout(self):
        return self.is_on
obj2 = Lamp(False)
print(obj2.is_on)
obj2.is_on=True
print(obj2.is_on)