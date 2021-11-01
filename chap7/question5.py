import math
class regularPolygon:
    def __init__(self, n=1, side=3, x=0, y=0):
        self.n = int(n)
        self.side = side
        self.x = x
        self.y = y

    def getArea(self):
        area = self.n * self.side**2/4*math.tan(3.14/10)
        print(area)

    def getPerimeter(self):
        perimeter = 2 * self.height * math.pi
        print(perimeter)


p1 = regularPolygon()
p1.getArea()

