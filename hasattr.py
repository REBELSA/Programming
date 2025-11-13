class Book:
    def __init__(self,title):
        self.title = title
b = Book("Python Guide")
print(hasattr(b))