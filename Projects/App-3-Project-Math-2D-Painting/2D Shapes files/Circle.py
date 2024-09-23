from math import pi,sin,cos
from PIL import Image
import time
import os

from PIL.ImageDraw import ImageDraw,Draw,Image


class Circle:
    def __init__(self,radius,angle=0,color="yellow"):
        self.radius=radius
        self.angle=angle
        self.color=color

    def diameter(self):
        return self.radius*2

    def circumference(self):
        return 2*pi*self.radius

    def area(self):
        return pi*self.radius**2

    def chord_length(self):
        return 2*self.radius*sin(self.angle/2)

    def arc_length(self):
        return self.radius*self.angle

    def area_of_sector(self):
        return 0.5*self.radius**2*self.angle

    def circle_print_all_calculations(self):
        if self.angle==0:
            print(f"The Diameter is {self.diameter()}")
            print(f"The Circumference is {self.circumference()}")
            print(f"The Area is {self.area()}")
        else:
            print(f"The Diameter is {self.diameter()}")
            print(f"The Circumference is {self.circumference()}")
            print(f"The Area is {self.area()}")
            print(f"The Chord Length is {self.chord_length()}")
            print(f"The Arc Length is {self.arc_length()}")
            print(f"The Area Of Sector is {self.area_of_sector()}")

    def draw_circle_and_all_properties(self):
        p = Image.new(mode="RGB", size=[self.radius*4, self.radius*4], color="white")
        os.chdir("../Output Files/")
        filename = str(time.time()) + ".jpg"

        draw=Draw(p)

        draw.circle(xy=[self.radius*2,self.radius*2],radius=self.radius,fill=self.color,outline="black",width=self.radius // 50)

        draw.line([(self.radius*2,self.radius*3),(self.radius*2,self.radius*1)],width=self.radius//50,fill="red")

        draw.line([(self.radius * 2, self.radius * 2), (self.radius * 3, self.radius * 2)], width=self.radius // 50,
                  fill="Green")
        draw.arc()


        p.save(filename)


circle=Circle(radius=500,angle=30)
circle1=Circle(radius=500,angle=40)
circle.circle_print_all_calculations()
circle1.circle_print_all_calculations()
circle.draw_circle_and_all_properties()