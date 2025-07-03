#Create a class Car that stores the brand, model, and year. Add a method to display details.

class Car():
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
    def display(self):
        print(f'the model of the car is {self.model}, {self.brand}, {self.year} ')
car1 = Car("audi","bmw","1998-5-12")
car1.display()