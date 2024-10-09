from math import sin,cos,acos,asin,atan,degrees
import datetime
import time
import os
from PIL.ImageDraw import Draw,Image


class Triangle:
    def __init__(self,a=0,b=0,c=0,angA=0,angB=0,angC=0,type=""):

        self.a= a
        self.b = b
        self.c = c
        self.angA=angA
        self.angB=angB
        self.angC=angC
        self.type=type

    def perimeter(self):
        self.find_all_sides_and_angles()
        return float("{:.2f}".format(self.a+self.b+self.c))

    def area(self):
        s=self.perimeter()/2
        return float("{:.2f}".format((s*(s-self.a)*(s-self.b)*(s-self.c))**0.5))

    def altitudes(self):
        self.find_all_sides_and_angles()
        alt_at_a=2*self.area()/self.a
        alt_at_b=2*self.area()/self.b
        alt_at_c=2*self.area()/self.c
        return float("{:.2f}".format(alt_at_a)),float("{:.2f}".format(alt_at_b)),float("{:.2f}".format(alt_at_c))

    def circum_radius(self):
        self.find_all_sides_and_angles()
        return float("{:.2f}".format(self.a*self.b*self.c/(4 * self.area())))

    def in_radius(self):
        self.find_all_sides_and_angles()
        return float("{:.2f}".format(self.area()/(self.perimeter()/2)))

    def median(self):
        self.find_all_sides_and_angles()
        med_a=(1/2)*((2*self.b**2+2*self.c**2-self.a**2)**0.5)
        med_b=(1/2)*((2*self.a**2+2*self.c**2-self.b**2)**0.5)
        med_c=(1/2)*((2*self.a**2+2*self.b**2-self.c**2)**0.5)
        return float("{:.2f}".format(med_a)),float("{:.2f}".format(med_b)),float("{:.2f}".format(med_c))

    def angle_bisector(self):
        self.find_all_sides_and_angles()
        bis_a=(self.b*self.c*(1-(self.a**2)/(self.b+self.c)**2))**0.5
        bis_b=(self.a*self.c*(1-(self.b**2)/(self.a+self.c)**2))**0.5
        bis_c=(self.b*self.a*(1-(self.c**2)/(self.b+self.a)**2))**0.5
        return float("{:.2f}".format(bis_a)),float("{:.2f}".format(bis_b)),float("{:.2f}".format(bis_c))

    def cosine_rule_find_angA(self):
        #self.find_all_sides_and_angles()
        self.angA=degrees(acos((self.b**2+self.c**2-self.a**2)/(2*self.b*self.c)))
        return float("{:.2f}".format(self.angA))

    def cosine_rule_find_angB(self):
        #self.find_all_sides_and_angles()
        self.angB=degrees(acos((self.a**2+self.c**2-self.b**2)/(2*self.a*self.c)))
        return float("{:.2f}".format(self.angB))

    def cosine_rule_find_angC(self):
        #self.find_all_sides_and_angles()
        self.angC=degrees(acos((self.a**2+self.b**2-self.c**2)/(2*self.b*self.a)))
        return float("{:.2f}".format(self.angC))

    def print_all_sides_and_angles(self):
        self.find_all_sides_and_angles()
        if self.chk_for_inequality():
            print(f"""
                    The side a of the triangle is {self.a}
                    The side b of the triangle is {self.b}  
                    The side c of the triangle is {self.c}
                    The Angle A of the triangle is {float("{:.2f}".format(self.angA))}
                    The Angle B of the triangle is {float("{:.2f}".format(self.angB))}
                    The Angle C of the triangle is {float("{:.2f}".format(self.angC))}
            """
                  )
        else:
            print("""Please enter the Values for the sides correctly
                Triangle Inequality Theorem:
                
                The theorem states that for any triangle with sides:
                
                1.a+b>c
                2.a+c>b
                3.b+c>a

                """)

    def print_all_calculations(self):

        print(f"The type of the triangle based on sides is {self.find_type_of_triangle_on_sides()}")

        print(f"The type of the triangle based on sides is {self.find_type_of_triangle_on_angle()}")

        print(f"The perimeter of the triangle is {self.perimeter()}")

        print(f"The Area of the triangle is {self.area()}")

        print(f"The Circum Radius of the triangle is {self.circum_radius()}")

        print(f"The In Radius  of the triangle is {self.in_radius()}")


        alt_at_a, alt_at_b, alt_at_c=self.altitudes()
        print(f"The altitude at a will be {alt_at_a}")
        print(f"The altitude at b will be {alt_at_b}")
        print(f"The altitude at c will be {alt_at_c}")

        med_a, med_b, med_c=self.median()
        print(f"The median at a will be {med_a}")
        print(f"The median at b will be {med_b}")
        print(f"The median at c will be {med_c}")

        bis_a, bis_b, bis_c=self.angle_bisector()
        print(f"The angle bisector at a will be {bis_a}")
        print(f"The angle bisector at b will be {bis_b}")
        print(f"The angle bisector at c will be {bis_c}")

    def find_type_of_triangle_on_sides(self):
        self.find_all_sides_and_angles()
        if self.a==self.b==self.c or self.angA==self.angB==self.angC==60:
            return "Equilateral Triangle"

        if self.a==self.b and self.angA==self.angB or\
           self.b==self.c and self.angB==self.angC or\
           self.c==self.a and self.angA==self.angC:
            return "Isosceles Triangle"

        if self.a!=self.b and self.b!=self.c:
            return "Isosceles Triangle"

    def find_type_of_triangle_on_angle(self):
        self.find_all_sides_and_angles()
        if self.angA == 90 or self.angB == 90 or self.angC == 90:
            return "Right Angled Triangle"

        if self.angA <= 90 and self.angB <= 90 and self.angC <= 90:
            return  "Acute Angled Triangle"

        if self.angA >= 90 or self.angB >= 90 and self.angC >= 90:
            return  "Obtuse Angled Triangle"

        if self.angA == 60 and self.angB == 60 and self.angC == 60:
            return  "Equilateral Triangle"


    def check_the_input(self):
        if self.type== "e".lower() or self.type== "e".upper():
            if ((self.a!=0 and self.b==0 and self.c==0) or
                (self.a==0 and self.b!=0 and self.c==0) or
                (self.a==0 and self.b==0 and self.c!=0)):

                return "You have entered the values for an equilateral Triangle"
            else:
                print_func_one()
                input_requirements_to_draw_triangle()

        if self.type == "i".lower() or self.type == "i".upper():
            if((self.a!=0 and self.b!=0 and self.c==0 and self.angA==0 and self.angB==0 and self.angC==0) or
                (self.a==0 and self.b!=0 and self.c==0 and self.angA!=0 and self.angB==0 and self.angC==0)):
                return "You have entered the Correct values for an Isosceles Triangle"
            else:
                print_func_one()
                input_requirements_to_draw_triangle()

        if self.type == "r".lower() or self.type == "r".upper():
            if ((self.a != 0 and self.b != 0 and self.c == 0 and self.angA == 0 and self.angB == 0 and self.angC == 0) or
                (self.a == 0 and self.b != 0 and self.c != 0 and self.angA == 0 and self.angB == 0 and self.angC == 0) or
                (self.a == 0 and self.b != 0 and self.c != 0 and self.angA == 0 and self.angB == 0 and self.angC == 0)):
                return "You have entered the Correct values for an Right Angle Triangle"
            else:
                print_func_one()
                input_requirements_to_draw_triangle()

        if self.type== "":
                #for SSS
            if ((self.a != 0 and self.b != 0 and self.c != 0 and self.angA == 0 and self.angB == 0 and self.angC == 0) or
                #for SAS
                (self.a != 0 and self.b != 0 and self.c == 0 and self.angA == 0 and self.angB != 0 and self.angC == 0) or
                (self.a != 0 and self.b == 0 and self.c != 0 and self.angA == 0 and self.angB == 0 and self.angC != 0) or
                (self.a == 0 and self.b != 0 and self.c != 0 and self.angA != 0 and self.angB == 0 and self.angC == 0) or
                #for ASA
                (self.a == 0 and self.b != 0 and self.c == 0 and self.angA != 0 and self.angB != 0 and self.angC == 0) or
                (self.a != 0 and self.b == 0 and self.c != 0 and self.angA == 0 and self.angB != 0 and self.angC != 0) or
                (self.a == 0 and self.b == 0 and self.c != 0 and self.angA != 0 and self.angB == 0 and self.angC != 0) or
                #for AAS
                (self.a != 0 and self.b == 0 and self.c == 0 and self.angA != 0 and self.angB != 0 and self.angC == 0) or
                (self.a == 0 and self.b == 0 and self.c != 0 and self.angA != 0 and self.angB != 0 and self.angC == 0) or
                ( self.a == 0 and self.b != 0 and self.c == 0 and self.angA == 0 and self.angB != 0 and self.angC != 0) or
                (self.a == 0 and self.b == 0 and self.c != 0 and self.angA == 0 and self.angB != 0 and self.angC != 0) or
                (self.a != 0 and self.b == 0 and self.c == 0 and self.angA != 0 and self.angB == 0 and self.angC != 0) or
                (self.a == 0 and self.b != 0 and self.c == 0 and self.angA != 0 and self.angB == 0 and self.angC != 0)):
                return "You have entered the Correct values for the Triangle"

            else:
                print_func_one()
                input_requirements_to_draw_triangle()

    def chk_for_inequality(self):
        if self.a+self.b>self.c:
            if self.a + self.b > self.c:
                if self.a + self.b > self.c:
                    return True
        return False

    def draw_the_triangle(self):

        canvas_var=max(self.a,self.b,self.c)
        if canvas_var<10:
            canvas_multiplier=20
        elif canvas_var<50:
            canvas_multiplier = 10
        elif canvas_var<100:
            canvas_multiplier = 5
        else:
            canvas_multiplier=1

        canvas_round=canvas_var * canvas_multiplier

        p = Image.new(mode="RGB", size=[canvas_round*12, canvas_round*8], color="white")
        os.chdir("../Output Files/Triangle")
        filename = "MaxSide" + "-" + str(canvas_var) + "-" + str(datetime.date.today()) + str(
            "{:.4f}".format(time.time())) + ".jpg"

        draw = Draw(p)

        draw.text((canvas_round * 2, canvas_round * 5), "a : " + str(self.a), fill="Black",
                  font_size=canvas_round * 0.2)

        draw.text((canvas_round * 2, canvas_round * 5.2), "b : " + str(self.b), fill="Black",
                  font_size=canvas_round * 0.2)

        draw.text((canvas_round * 2, canvas_round * 5.4), "c : " + str(self.c), fill="Black",
                  font_size=canvas_round * 0.2)

        draw.text((canvas_round * 2, canvas_round * 5.6), "Ang A : " + str(self.angA), fill="Black",
                  font_size=canvas_round * 0.2)

        draw.text((canvas_round * 2, canvas_round * 5.8), "Ang B : " + str(self.angB), fill="Black",
                  font_size=canvas_round * 0.2)

        draw.text((canvas_round * 2, canvas_round * 6), "Ang C : " + str(self.angC), fill="Black",
                  font_size=canvas_round * 0.2)



        draw.text((canvas_round * 7, canvas_round * 5), "Triangle type(side) : " + str(self.find_type_of_triangle_on_sides()), fill="Black",
                  font_size=canvas_round * 0.2)

        draw.text((canvas_round * 7, canvas_round * 5.2), "Triangle type(angle) : " + str(self.find_type_of_triangle_on_angle()), fill="Black",
                  font_size=canvas_round * 0.2)

        draw.text((canvas_round * 7, canvas_round * 5.4), "Perimeter : " + str(self.perimeter()), fill="Black",
                  font_size=canvas_round * 0.2)

        draw.text((canvas_round * 7, canvas_round * 5.6), "Area : " + str(self.area()), fill="Black",
                  font_size=canvas_round * 0.2)

        draw.text((canvas_round * 7, canvas_round * 5.8), "Circum Radius : " + str(self.circum_radius()), fill="Black",
                  font_size=canvas_round * 0.2)

        draw.text((canvas_round * 7, canvas_round * 6), "InRadius : " + str(self.in_radius()), fill="Black",
                  font_size=canvas_round * 0.2)


        draw.text((canvas_round * 7, canvas_round * 6.2), "altitude at a : " + str(self.altitudes()[0]), fill="Black",
                  font_size=canvas_round * 0.2)

        draw.text((canvas_round * 7, canvas_round * 6.4), "altitude at b : " + str(self.altitudes()[1]), fill="Black",
                  font_size=canvas_round * 0.2)


        draw.text((canvas_round * 7, canvas_round * 6.6), "altitude at c : " + str(self.altitudes()[2]), fill="Black",
                  font_size=canvas_round * 0.2)

        draw.text((canvas_round * 7, canvas_round * 6.8), "median at a : " + str(self.median()[0]), fill="Black",
                  font_size=canvas_round * 0.2)

        draw.text((canvas_round * 7, canvas_round * 7), "median at b : " + str(self.median()[1]), fill="Black",
                  font_size=canvas_round * 0.2)

        draw.text((canvas_round * 7, canvas_round * 7.2), "median at c : " + str(self.median()[2]), fill="Black",
                  font_size=canvas_round * 0.2)

        draw.text((canvas_round * 2, canvas_round * 6.2), "angle bisector at a : " + str(self.angle_bisector()[0]), fill="Black",
                  font_size=canvas_round * 0.2)

        draw.text((canvas_round * 2, canvas_round * 6.4), "angle bisector at b : " + str(self.angle_bisector()[1]), fill="Black",
                  font_size=canvas_round * 0.2)

        draw.text((canvas_round * 2, canvas_round * 6.6), "angle bisector at c : " + str(self.angle_bisector()[2]), fill="Black",
                  font_size=canvas_round * 0.2)

        draw.polygon([(canvas_round * 7, canvas_round * 4),
                      (canvas_round * 7 + self.a * canvas_multiplier * 2, canvas_round * 4), (
                      (canvas_round * 7 + self.a * canvas_multiplier),
                      (canvas_round * 4 - 2 * canvas_multiplier * self.altitudes()[0]))], fill="pink", outline="black",
                     width=canvas_round // 50)

        draw.polygon([(canvas_round * 2 , canvas_round * 4), (canvas_round * 2+self.a*canvas_multiplier*2 , canvas_round * 4),((canvas_round * 2+self.a*canvas_multiplier) , (canvas_round * 4-2*canvas_multiplier*self.altitudes()[0]))],fill="pink",outline="black",width=canvas_round // 50)

        draw.text((canvas_round * 7 + self.a * canvas_multiplier , canvas_round * 4.2), " a ", fill="Black",
                  font_size=canvas_round * 0.2)

        draw.text((canvas_round * 7, canvas_round * 6.8), "median at a : " + str(self.median()[0]), fill="Black",
                  font_size=canvas_round * 0.2)

        draw.text((canvas_round * 7, canvas_round * 7), "median at b : " + str(self.median()[1]), fill="Black",
                  font_size=canvas_round * 0.2)

        draw.text((canvas_round * 7, canvas_round * 7.2), "median at c : " + str(self.median()[2]), fill="Black",
                  font_size=canvas_round * 0.2)

        draw.text((canvas_round * 2, canvas_round * 6.2), "angle bisector at a : " + str(self.angle_bisector()[0]),
                  fill="Black",
                  font_size=canvas_round * 0.2)

        draw.text((canvas_round * 2, canvas_round * 6.4), "angle bisector at b : " + str(self.angle_bisector()[1]),
                  fill="Black",
                  font_size=canvas_round * 0.2)

        draw.text((canvas_round * 2, canvas_round * 6.6), "angle bisector at c : " + str(self.angle_bisector()[2]),
                  fill="Black",
                  font_size=canvas_round * 0.2)
        p.save(filename)



    def find_all_sides_and_angles(self):
        if self.type == "e".lower() or self.type == "e".upper():
            self.angA=self.angB=self.angC=60
            if self.a != 0 and self.b == 0 and self.c == 0:
                self.b=self.c=self.a

            if self.a == 0 and self.b != 0 and self.c == 0:
                self.a=self.c=self.b

            if self.a == 0 and self.b == 0 and self.c != 0:
                self.a=self.b=self.c
                return self.a,self.b,self.c,self.angA,self.angB,self.angC


        if self.type == "i".lower() or self.type == "i".upper():
            if self.a != 0 and self.b != 0 and self.c == 0 and self.angA == 0 and self.angB == 0 and self.angC == 0:
                self.c=self.b
                self.cosine_rule_find_angA()
                self.cosine_rule_find_angB()
                self.cosine_rule_find_angC()
                return self.a,self.b,self.c,self.angA,self.angB,self.angC

            if self.a == 0 and self.b != 0 and self.c == 0 and self.angA != 0 and self.angB == 0 and self.angC == 0:
                self.c=self.b
                self.angB=(180-self.angC)/2
                self.angC=self.angB
                self.a=(self.b*degrees(sin(self.angA))/sin(self.angB))
                return self.a, self.b, self.c, self.angA, self.angB, self.angC


        if self.type == "r".lower() or self.type == "r".upper():
            self.angB=90

            if self.a != 0 and self.b != 0 and self.c == 0 and self.angA == 0  and self.angC == 0:
                self.angA = degrees(atan(self.a / self.b))
                self.angC=90-self.angA
                self.c=(self.b**2-self.a**2)**0.5
                return self.a, self.b, self.c, self.angA, self.angB, self.angC

            if self.a == 0 and self.b != 0 and self.c != 0 and self.angA == 0  and self.angC == 0:
                self.angA=degrees(asin(self.b/self.c))
                self.angC=90-self.angA
                self.a = (self.b ** 2 - self.c ** 2) ** 0.5
                return self.a, self.b, self.c, self.angA, self.angB, self.angC

            if self.a != 0 and self.b == 0 and self.c != 0 and self.angA == 0 and self.angC == 0:
                self.angA=degrees(asin(self.a/self.c))
                self.angC=90-self.angA
                self.b = (self.c ** 2 + self.a ** 2) ** 0.5
                return self.a, self.b, self.c, self.angA, self.angB, self.angC


        if self.type == "sss".lower() or self.type=="sss".upper():
            # for SSS
            if self.a != 0 and self.b != 0 and self.c != 0 and self.angA == 0 and self.angB == 0 and self.angC == 0:
                self.cosine_rule_find_angB()
                self.cosine_rule_find_angA()
                self.cosine_rule_find_angC()
                return self.a, self.b, self.c, self.angA, self.angB, self.angC

        if self.type == "sas".lower() or self.type == "sas".upper():
                # for SAS
            if self.a != 0 and self.b != 0 and self.c == 0 and self.angA == 0 and self.angB != 0 and self.angC == 0:
                self.angA=degrees(self.a*sin(self.angB)/self.b)
                self.angC=180-(self.angA+self.angB)
                self.c=(self.b * (sin(self.angC) / sin(self.angB)))
                return self.a, self.b, self.c, self.angA, self.angB, self.angC

            if self.a != 0 and self.b == 0 and self.c != 0 and self.angA == 0 and self.angB == 0 and self.angC != 0:
                self.angA = (self.a * degrees(sin(self.angC) / self.c))
                self.angB = 180 - (self.angA + self.angC)
                self.b = (self.c * (sin(self.angB) / sin(self.angC)))
                return self.a, self.b, self.c, self.angA, self.angB, self.angC


            if self.a == 0 and self.b != 0 and self.c != 0 and self.angA != 0 and self.angB == 0 and self.angC == 0:
                self.angB = (self.b * degrees(sin(self.angA) / self.a))
                self.angC = 180 - (self.angA + self.angB)
                self.a = (self.b * sin(self.angA) / sin(self.angB))
                return self.a, self.b, self.c, self.angA, self.angB, self.angC

        if self.type == "asa".lower() or self.type == "asa".upper():
                # for ASA
            if self.a == 0 and self.b != 0 and self.c == 0 and self.angA != 0 and self.angB != 0 and self.angC == 0:
                self.angC=180-(self.angA+self.angB)
                self.a=(self.b * sin(self.angA) / sin(self.angB))
                self.c=(self.b * sin(self.angC) / sin(self.angB))
                return self.a, self.b, self.c, self.angA, self.angB, self.angC

            if self.a != 0 and self.b == 0 and self.c != 0 and self.angA == 0 and self.angB != 0 and self.angC != 0:
                self.angA = 180 - (self.angC + self.angB)
                self.b = (self.a * sin(self.angB) / sin(self.angA))
                self.c = (self.b * sin(self.angC) / sin(self.angB))
                return self.a, self.b, self.c, self.angA, self.angB, self.angC

            if self.a == 0 and self.b == 0 and self.c != 0 and self.angA != 0 and self.angB == 0 and self.angC != 0:
                self.angB = 180 - (self.angA + self.angC)
                self.a = (self.c * sin(self.angA) / sin(self.angC))
                self.b = (self.c * sin(self.angB) / sin(self.angC))
                return self.a, self.b, self.c, self.angA, self.angB, self.angC

                # for AAS
        if self.type == "aas".lower() or self.type == "aas".upper():
            if self.a != 0 and self.b == 0 and self.c == 0 and self.angA != 0 and self.angB != 0 and self.angC == 0:
                self.angC = 180 - (self.angA + self.angB)
                self.b = (self.c * sin(self.angB) / sin(self.angC))
                self.c = (self.b * sin(self.angC) / sin(self.angB))
                return self.a, self.b, self.c, self.angA, self.angB, self.angC

            if self.a == 0 and self.b == 0 and self.c != 0 and self.angA != 0 and self.angB != 0 and self.angC == 0:
                self.angC = 180 - (self.angA + self.angB)
                self.a = (self.c * sin(self.angA) / sin(self.angC))
                self.b = (self.c * sin(self.angB) / sin(self.angC))
                return self.a, self.b, self.c, self.angA, self.angB, self.angC

            if self.a == 0 and self.b != 0 and self.c == 0 and self.angA == 0 and self.angB != 0 and self.angC != 0:
                self.angA = 180 - (self.angC + self.angB)
                self.a = (self.c * sin(self.angA) / sin(self.angC))
                self.c = (self.b * sin(self.angC) / sin(self.angB))
                return self.a, self.b, self.c, self.angA, self.angB, self.angC

            if self.a == 0 and self.b == 0 and self.c != 0 and self.angA == 0 and self.angB != 0 and self.angC != 0:
                self.angA = 180 - (self.angC + self.angB)
                self.a = (self.c * sin(self.angA) / sin(self.angC))
                self.b = (self.c * sin(self.angB) / sin(self.angC))
                return self.a, self.b, self.c, self.angA, self.angB, self.angC

            if self.a != 0 and self.b == 0 and self.c == 0 and self.angA != 0 and self.angB == 0 and self.angC != 0:
                self.angB = 180 - (self.angA + self.angC)
                self.a = (self.c * sin(self.angA) / sin(self.angC))
                self.b = (self.c * sin(self.angB) / sin(self.angC))
                return self.a, self.b, self.c, self.angA, self.angB, self.angC

            if self.a == 0 and self.b != 0 and self.c == 0 and self.angA != 0 and self.angB == 0 and self.angC != 0:
                self.angB = 180 - (self.angA + self.angC)
                self.a = (self.c * sin(self.angA) / sin(self.angC))
                self.c = (self.b * sin(self.angC) / sin(self.angB))
                return self.a, self.b, self.c, self.angA, self.angB, self.angC


def print_func_one():
    print("Please Go through the instructions given and enter the correct values:")

def input_requirements_to_draw_triangle():
    print("""
            We need the following Minimum requirements Drawing the triangles any one of them
            
                                         A
                                        / \\.
                                      b/   \\.c               Fig One
                                      /     \\.
                                     *-------*  
                                    B    a     C
                Where:
                
            - A = Vertex opposite side a
            - B = Vertex opposite side b
            - C = Vertex opposite side c
            - angA = Angle at vertex A
            - angB = Angle at vertex B
            - angC = Angle at vertex C
            
                                        
            
            1.SSS(side-side-side): 1.(All sides of the triangle must be provided.)
            
                                    From Fig One. 1.(a, b, c)
            
            2.SAS(Side-Angle_Side): 1.(Two Sides and the included Angle)
                
                #Any one of the below combination
                                    From Fig One. 1.(a, b, angB) 
                                                  2.(b, c, angA)
                                                  3.(c, a, angC)
            
            3.ASA(Angle-Side-Angle): 1.(Two Angles and the included Side)
                
                #Any one of the below combination
                                     From Fig One. 1.(angA, b, angB) 
                                                   2.(angB, a, angC)
                                                   3.(angC, c, angA)
            
            4.AAS(Angle-Angle-Side): 1.(Two Angles and one side not in between them) 
                
                #Any one of the below combination
                                    From Fig One. 1.(angA, angB, a) 
                                                   2.(angA, angC, b)
                                                   3.(angA,angB,  c)
                                                   4.(angB, angC, c)
                                                   5.(angC, angA, a)
                                                   6.(angC, angB, b)
                                                   
                                    Equilateral Triangle (All sides equal)
                                          A
                                         / \\.
                                      a /   \\. a     Fig Two 
                                       /     \\.
                                      B-------C
                                          a
                                     
                         




            5.For Equilateral Triangle:   1.(Any one Side) 
                #Any one of the below combination
                                    From Fig Two. 1.1. (a) - Any one side since all sides are equal (a = b = c)
                                             
                                    Combinations:
                                             1. (a) 
                                             
                                                   
                                     Isosceles Triangle (Two equal sides)
                                          A
                                         /|\\.
                                        / | \\.
                                      b/  |  \\.b Fig Three
                                      /   |   \\.
                                     B----*----C
                                         a
                                     
                                     
                     
            6.For Isosceles Triangle: 1.(One of the equal sides and the base) 
                                    2.(one of the equal sides and the included angle)
            
                                    Combinations From Fig Three:
                                     1. (b, a) 
                                     2. (b, angA) 
                                     

                                         Right-Angle Triangle (One 90° angle)
                                             C
                                            /|
                                          b/ | a
                                          /  |
                                         A---*B
                                            c (Hypotenuse)
 

            7.For Right Angle Triangle: 1.(The two sides opposite of hypotenuse)
                                      2.(Hypotenuse and one other side any)
                                
                                 Combinations:
                                         1. (a, c) 
                                         2. (b, a)
                                         3. (b, c)
            
            Rules:
            if you want to enter the type you can:
            
            1.Enter I for Isosceles
            2.Enter E for Equilateral
            3.Enter R for Right angle 
            
            
            
            \n\n""")

def take_input_triangle():
        while True:
            try:
                input_requirements_to_draw_triangle()

                triangle=Triangle()

                print("""Please enter the type of triangle :\n
                
                1.Enter I for Isosceles
                2.Enter E for Equilateral
                3.Enter R for Right angle
                4.SSS(side-side-side) Enter SSS
                5.SAS(Side-Angle_Side) Enter SAS
                6.ASA(Angle-Side-Angle) Enter ASA
                7.AAS(Angle-Angle-Side) Enter AAS
                \n
                """)

                var_chk = input()
                triangle.type=var_chk

                if var_chk.lower() == "e" or var_chk == 'e':
                    print("Please enter the value for Side:\n")
                    triangle.a = int(input())

                elif var_chk.lower() == "i" or var_chk == 'i':
                    print("""Please enter combination you want to input Values for :\n
                        1. (b, a) 
                        2. (b, angA) 

                        """)

                    comb = int(input())
                    if comb == 1:
                        print("please Enter the Value for Side a :")
                        triangle.a = int(input())

                        print("please Enter the Value for Side b :")
                        triangle.b = int(input())

                        triangle.c=triangle.b

                        if triangle.chk_for_inequality():
                            pass
                        else:
                            print("""Please enter the Values for the sides correctly
                                        Triangle Inequality Theorem:
    
                                        The theorem states that for any triangle with sides:
    
                                        1.a+b>c
                                        2.a+c>b
                                        3.b+c>a
    
                                        """)
                            return True

                    elif comb == 2:
                        print("please Enter the Value for Side b :")
                        triangle.b = int(input())

                        print("please Enter the Value for ang A :")
                        triangle.angA = int(input())


                elif var_chk.lower() == "r" or var_chk == 'r':
                    print("""Please enter combination you want to input Values for :\n
                        1. (a, c) 
                        2. (b, a)
                        3. (b, c) 

                        """)

                    comb = int(input())
                    if comb == 1:
                        print("please Enter the Value for Side a :")
                        triangle.a = int(input())

                        print("please Enter the Value for Side c :")
                        triangle.c = int(input())

                    elif comb == 2:
                        print("please Enter the Value for Side b :")
                        triangle.b = int(input())

                        print("please Enter the Value for side a :")
                        triangle.a = int(input())

                    elif comb == 3:
                        print("please Enter the Value for Side b :")
                        triangle.b = int(input())

                        print("please Enter the Value for side c :")
                        triangle.c = int(input())

                elif var_chk.lower() == "sss" or var_chk == 'sss':
                    print("Please enter the value for Side a:\n")
                    triangle.a = int(input())

                    print("Please enter the value for Side b:\n")
                    triangle.b = int(input())

                    print("Please enter the value for Side c:\n")
                    triangle.c = int(input())



                elif var_chk.lower() == "sas" or var_chk == 'sas':
                    print("""Please enter combination you want to input Values for :\n
                        1.(a, b, angB) 
                        2.(b, c, angA)
                        3.(c, a, angC) 

                        """)

                    comb = int(input())
                    if comb == 1:
                        print("please Enter the Value for Side a :")
                        triangle.a = int(input())

                        print("please Enter the Value for Side b :")
                        triangle.b = int(input())

                        print("please Enter the Value for ang B :")
                        triangle.angB = int(input())

                    elif comb == 2:
                        print("please Enter the Value for Side b :")
                        triangle.b = int(input())

                        print("please Enter the Value for side c :")
                        triangle.c = int(input())

                        print("please Enter the Value for ang A :")
                        triangle.angA = int(input())

                    elif comb == 3:
                        print("please Enter the Value for Side c :")
                        triangle.b = int(input())

                        print("please Enter the Value for side a :")
                        triangle.c = int(input())

                        print("please Enter the Value for ang C :")
                        triangle.angC = int(input())

                elif var_chk.lower() == "asa" or var_chk == 'asa':
                    print("""Please enter combination you want to input Values for :\n
                        1.(angA, b, angB) 
                        2.(angB, a, angC)
                        3.(angC, c, angA)

                        """)

                    comb = int(input())
                    if comb == 1:
                        print("please Enter the Value for angle B :")
                        triangle.angB = int(input())

                        print("please Enter the Value for Side a :")
                        triangle.b = int(input())

                        print("please Enter the Value for ang A :")
                        triangle.angA = int(input())

                    elif comb == 2:
                        print("please Enter the Value for ang B :")
                        triangle.angB = int(input())

                        print("please Enter the Value for side a :")
                        triangle.a = int(input())

                        print("please Enter the Value for ang C :")
                        triangle.angC = int(input())

                    elif comb == 3:
                        print("please Enter the Value for ang A :")
                        triangle.angA = int(input())

                        print("please Enter the Value for side c :")
                        triangle.c = int(input())

                        print("please Enter the Value for ang C :")
                        triangle.angC = int(input())

                elif var_chk.lower() == "aas" or var_chk == 'aas':
                    print("""Please enter combination you want to input Values for :\n
                        1.(angA, angB, a) 
                        2.(angA, angC, b)
                        3.(angA,angB,  c)
                        4.(angB, angC, c)
                        5.(angC, angA, a)
                        6.(angC, angB, b)

                        """)

                    comb = int(input())
                    if comb == 1:
                        print("please Enter the Value for angle B :")
                        triangle.angB = int(input())

                        print("please Enter the Value for Side a :")
                        triangle.b = int(input())

                        print("please Enter the Value for ang A :")
                        triangle.angA = int(input())

                    elif comb == 2:
                        print("please Enter the Value for ang A :")
                        triangle.angA = int(input())

                        print("please Enter the Value for side b :")
                        triangle.b = int(input())

                        print("please Enter the Value for ang C :")
                        triangle.angC = int(input())

                    elif comb == 3:
                        print("please Enter the Value for ang A :")
                        triangle.angA = int(input())

                        print("please Enter the Value for side c :")
                        triangle.c = int(input())

                        print("please Enter the Value for ang B :")
                        triangle.angB = int(input())
                    elif comb == 4:
                        print("please Enter the Value for angle B :")
                        triangle.angB = int(input())

                        print("please Enter the Value for Side c :")
                        triangle.c = int(input())

                        print("please Enter the Value for ang C :")
                        triangle.angC = int(input())

                    elif comb == 5:
                        print("please Enter the Value for ang A :")
                        triangle.angA = int(input())

                        print("please Enter the Value for side a :")
                        triangle.a = int(input())

                        print("please Enter the Value for ang C :")
                        triangle.angC = int(input())

                    elif comb == 6:
                        print("please Enter the Value for ang B :")
                        triangle.angB = int(input())

                        print("please Enter the Value for side b :")
                        triangle.b = int(input())

                        print("please Enter the Value for ang C :")
                        triangle.angC = int(input())

                    triangle.check_the_input()

                else:
                    print("""You did not provide the Correct Values out of :
                        
                        1.Enter I for Isosceles
                        2.Enter E for Equilateral
                        3.Enter R for Right angle
                        4.SSS(side-side-side) Enter SSS
                        5.SAS(Side-Angle_Side) Enter SAS
                        6.ASA(Angle-Side-Angle) Enter ASA
                        7.AAS(Angle-Angle-Side) Enter AAS
                    
                        """)
                    return True


                print("\n Do you want to find all sides and angles print 'y' for Yes and 'n' for No :\n")
                var_chk = input()
                if var_chk.lower() == "y" or var_chk == 'y':
                    triangle.print_all_sides_and_angles()

                print("\n Do you want to find all the calculations 'y' for Yes and 'n' for No :\n")
                var_chk = input()
                if var_chk.lower() == "y" or var_chk == 'y':
                    triangle.print_all_calculations()

                print("\n Do you want to create an image for the triangle 'y' for Yes and 'n' for No :\n")
                var_chk = input()
                if var_chk.lower() == "y" or var_chk == 'y':
                    triangle.draw_the_triangle()
                    return False


            except ValueError as e:
                print(e)
                print("Please Enter the Correct Values for the Parameters int for comb and string for type :\n")


take_input_triangle()

