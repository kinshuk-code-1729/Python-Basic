#Rect.py
class Rectangle:
    def __init__(self):
        print("Rectangle")
    def Area(self, length, width):
        self.l=length
        self.w=width
        print("Area of Rectangle is : ", self.l*self.w)
#Sq.py
class Sq:
    def __init__(self):
        print("Square")
    def Area(self, side):
        self.a=side
        print("Area of square is : ", self.a*self.a)
#Tri.py
class Tri:
    def __init__(self):
        print("Triangle")
    def Area(self, base, height):
        self.b=base
        self.h=height
        ar= (1/2)*self.b*self.h
        print("Area of Triangle is : ", ar )
#main.py
import Rectangle
import Sq
import Tri
r=Rect.Rectangle( )
r.Area(10,20)
s=Sq.Square( )
s.Area(10)
t=Tri.Triangle( )
t.Area(6,8)
