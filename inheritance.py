class Math():
    def __init__(self):
        print(" I am from the parent")
    def sum(self):
        return self.a + self.b
class Num(Math):
    def __init__(self):
        self.a =5
        self.b =6
        print("I am from the child.")
        super().__init__()
obj1 = Num()
print(obj1.sum())

        