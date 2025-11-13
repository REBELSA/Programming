class person:
    def __init__(self,name):
        self.name = name
    def display(self):
        print("Person: ",self.name)

class teacher(person):
    def display(self):
        print("Teacher ",self.name)
    def teach(self):
        print(self.name, "is teaching")
#p1 = person("Devaj")
#p1.display()

t1 = teacher("Ashwin")
t1.display()
        