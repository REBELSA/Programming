class Box:
    def __init__(self,l,b):
        self.l = l
        self.b = b
    def area(self):
        return self.l * self.b
b = Box(10,15)
print("Area of box: ",b.area())