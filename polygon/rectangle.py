from polygon import polygon
from shape import Shape 

class Rectangle(polygon, Shape):
    def area(self):
        return self.get_width() * self.get_height()
