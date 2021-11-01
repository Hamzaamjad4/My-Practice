import math
class Circle:
    def __init__(self, height = 1, width=2):
     self.height = height
     self.width=width
     print(self.width)
     print(self.height)

    def getArea(self):
       area=self.height * self.width / 2
       print(area)

    def getPerimeter(self):
     perimeter = 2 * self.height * math.pi
     print(perimeter)
p1 = Circle(4, 40)
p1.getArea()

p2 = Circle(3.5,35.7)
p2.getPerimeter()





