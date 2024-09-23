import datetime
from math import pi,sin
import time
import os

from PIL.ImageDraw import Draw,Image


class Circle:
    def __init__(self,radius,angle=0,color="pink"):
        self.radius=radius
        self.angle=angle
        self.color=color

    def diameter(self):
        return "{:.2f}".format(self.radius*2)

    def circumference(self):
        return "{:.2f}".format(2*pi*self.radius)

    def area(self):
        return "{:.2f}".format(pi*self.radius**2)

    def chord_length(self):
        return "{:.2f}".format(2*self.radius*sin(self.angle/2))

    def arc_length(self):
        return "{:.2f}".format(self.radius*self.angle)

    def area_of_sector(self):
        return "{:.2f}".format(0.5*self.radius**2*self.angle)

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
        p = Image.new(mode="RGB", size=[self.radius*8, self.radius*5], color="white")
        os.chdir("../Output Files/")
        filename = "Rad"+"-"+str(self.radius)+"-"+str(datetime.date.today())+str("{:.4f}".format(time.time()))+ ".jpg"

        draw=Draw(p)

        draw.text((self.radius * 5, self.radius * 3.5), "Circumference : " + str(self.circumference()), fill="Black",
                  font_size=self.radius * 0.2)

        draw.text((self.radius * 5, self.radius * 3.7), "Area : " + str(self.area()), fill=self.color,
                  font_size=self.radius * 0.2)

        draw.text((self.radius * 1.5, self.radius * 3.5), "Radius : " + str(self.radius), fill="Green",
                  font_size=self.radius * 0.2)

        draw.text((self.radius * 1.5, self.radius * 3.7), "Diameter : " + str(self.diameter()), fill="Red",
                  font_size=self.radius * 0.2)

        draw.circle(xy=[self.radius * 6, self.radius * 2], radius=self.radius, fill=self.color, outline="black",
                    width=self.radius // 50)

        draw.circle(xy=[self.radius*2,self.radius*2],radius=self.radius,fill=self.color,outline="black",width=self.radius // 50)

        draw.line([(self.radius*2,self.radius*3),(self.radius*2,self.radius*1)],width=self.radius//50,fill="red")

        draw.line([(self.radius * 2, self.radius * 2), (self.radius * 3, self.radius * 2)], width=self.radius // 50,
                  fill="Green")

        if self.angle!=0:

            draw.arc(xy=[(self.radius * 1,self.radius * 1),(self.radius * 3,self.radius * 3)],start=0,end=self.angle,fill="Orange",width=self.radius // 50)

            draw.chord(xy=[(self.radius * 1, self.radius * 1), (self.radius * 3, self.radius * 3)], start=90, end=90+self.angle,
                      fill="blue",width=self.radius // 40,outline="Brown")

            draw.pieslice(xy=[(self.radius * 1, self.radius * 1), (self.radius * 3, self.radius * 3)], start=180, end=180+self.angle,
                      fill="indigo",width=self.radius // 50)

            draw.text((self.radius * 3, self.radius * 0.5),"Fig: Circle",fill="Red",font_size=self.radius*0.3)

            draw.text((self.radius * 1.5, self.radius * 4.1), "Chord Length : "+str(self.chord_length()), fill="brown", font_size=self.radius * 0.2)

            draw.text((self.radius * 1.5, self.radius * 4.3), "Arc Length : "+str(self.arc_length()), fill="Orange", font_size=self.radius * 0.2)

            draw.text((self.radius * 1.5, self.radius * 3.9), "Area of Sector : "+str(self.area_of_sector()), fill="brown", font_size=self.radius * 0.2)



            draw.text((self.radius * 1.5, self.radius * 4.5), "Angle : " + str(self.angle), fill="brown",
                      font_size=self.radius * 0.2)


        p.save(filename)


circle=Circle(radius=1000,angle=1)
circle1=Circle(radius=500,angle=40)
circle.circle_print_all_calculations()
circle1.circle_print_all_calculations()
circle.draw_circle_and_all_properties()