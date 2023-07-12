class Rectangle:
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        pass

    def __str__(self):
        line = str()
        if self.height <= 50 or self.width <= 50:
            line += (f'Rectangle(width={self.width}, height={self.height}) \n')
        return line

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
    
    def get_picture(self):
        i = 1
        line = str()
        if self.height <= 50 or self.width <= 50:
            for i in range(self.height):
                line += ('*'*self.width) + '\n'
            return line
        else: 
            return 'Too big for picture.'
        
    def get_amount_inside(self, shape):
        return self.get_area() // shape.get_area()
    


class Square(Rectangle):
    def __init__(self, width):
        super().__init__(width)
        self.height = width
        self.width = width
    
