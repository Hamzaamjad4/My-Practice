import math
class QuadraticEquation:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def getDiscriminant(self):
        return ((self.b)**2) - (4 * self.a * self.c)
    def geta(self):
        return self.a
    def getb(self):
        return self.b
    def getc(self):
        return self.c

    def getRoot1(self):

         return ((-1*self.getb()) - math.sqrt(self.getDiscriminant())) / (2 * self.geta())
    def getRoot2(self):

        return ((-1*self.getb()) + math.sqrt(self.getDiscriminant())) / (2 * self.geta())

print('Enter values for a, b and c')
a, b, c= map(int, input().split())
qe = QuadraticEquation(a,b,c)
if(qe.getDiscriminant()<0):
    print('The equation has no roots')
elif(qe.getDiscriminant() == 0):
    print('One Common Root of equation='+str(qe.getRoot1()))
else: print('Roots of equation are:'+str(qe.getRoot1())+" and "+str(qe.getRoot2()))


