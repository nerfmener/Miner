from math import pi
 
class Figure:
    def __init__(self):
        pass
    def calc_area(self):
        pass
class Triangle(Figure):
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def calc_area(self):
        p = (self.a + self.b + self.c) / 2
        return (p*(p-self.a)*(p-self.b)*(p-self.c))**0.5
My_Triangle = Triangle(3,4,5)
print(My_Triangle.calc_area())
class Pryamougolnik(Figure):
    def __init__(self, d, e):
        self.d = d
        self.e = e
    def calc_area(self):
        t = (self.d * self.e)
        return (t)
My_Pryamougolnik = Pryamougolnik(4 ,8)
print(My_Pryamougolnik.calc_area())
class Cvadrat(Figure):
    def __init__(self, f):
        self.f = f
    def calc_area(self):
        r = (self.f) ** 2
        return (r)
My_Cvadrat = Cvadrat(4)
print(My_Cvadrat.calc_area())

class Krug(Figure):
    def __init__(self, x):
        self.x = x
    def calc_area(self):
        z = (self.x + pi) * 2
        return (z)
My_Krug = Krug(7)
print(My_Krug.calc_area())
