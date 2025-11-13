class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print("name: ", self.name,"\nAge: ",self.age) 

a = Animal("fast",20)
b = Animal("bakk",19)

a.display()
b.display()

    