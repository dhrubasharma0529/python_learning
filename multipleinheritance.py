class A():
    def __init__(self):
        self.value = "A"
class B():
    def __init__(self):
        self.value = "B"
class C(B,A):
    def __init__(self):
        super().__init__()
    def display(self):
        a = self.value
        return a

Ca = C()
print(Ca.display())