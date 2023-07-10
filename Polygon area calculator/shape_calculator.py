class Rectangle:
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        pass
    
    def set_width(self, width):
        self.width += width
    
    def set_height(self, height):
        self.height += height
    
    def get_area(self):
        area = self.height * self.width
        return area
    
    def get_perimeter(self):
        perimeter = (2 *self.width) + (2*self.height)
        return perimeter
    
    def get_diagonal(self):
        diagonal = ((self.width**2)+(self.height**2))**.5
        return diagonal



class Square:
