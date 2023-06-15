class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)


# Create an instance of the Rectangle class
my_rectangle = Rectangle(5, 3)

# Calculate and print the area and perimeter
print("Area:", my_rectangle.area())
print("Perimeter:", my_rectangle.perimeter())
