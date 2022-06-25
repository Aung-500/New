from polygon import polygon
from shape import Shape 

class Triangle(polygon, Shape):
    def area(self):
        return self.get_width() * self.get_height() / 2