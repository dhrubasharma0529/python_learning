class Area():
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        ar = self.length * self.width
        return ar
    def perimeter(self):
        br = 2 * (self.length + self.width)
        return br
rect = Area(6,5)
print(f"the area is {rect.area()}")
print(f"the perimeter is {rect.perimeter()}")
