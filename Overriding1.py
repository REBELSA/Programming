class Circle:
    def draw(self):
        print("Drawing a circle ")

class Square:
    def draw(self):
        print("Drawing a square ")

def render_shape(shape):
    shape.draw()
    
circle = Circle()
square = Square()

render_shape(circle)
render_shape(square)