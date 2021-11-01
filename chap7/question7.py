class account:
    def __init__(self, a=2, b=3, c=6,d=4,e=9,f=7):
        self.a = (a)
        self.b = (b)
        self.c = (c)
        self.d = (d)
        self.e = (e)
        self.f = (f)



    def isSloved(self):
       isSolved=((self.e()* self.d()) - (self.b()* self.f())) /(self.a()* self.d())-(self.b()* self.gc())
       print(isSolved)


p1 = account()
print(p1.isSloved())
