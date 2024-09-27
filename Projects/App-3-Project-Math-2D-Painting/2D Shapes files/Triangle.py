from math import sin,cos,acos,asin,atan





class Triangle:
    def __init__(self,a=0,b=0,c=0,angA=0,angB=0,angC=0,type=""):

        self.a= a
        self.b = b
        self.c = c
        self.angA=angA
        self.angB=angB
        self.angC=angC
        self.type=type

    def cosine_rule_find_angA(self):
        self.angA=acos((self.b**2+self.c**2-self.a**2)/2*self.b*self.c)
        return self.angA

    def cosine_rule_find_angB(self):
        self.angB=acos((self.a**2+self.c**2-self.b**2)/2*self.a*self.c)
        return self.angB

    def cosine_rule_find_angC(self):
        self.angC=acos((self.a**2+self.b**2-self.a**2)/2*self.b*self.c)
        return self.angC

    def print_all_sides_and_angles(self):
        print(f"""
                The side a of the triangle is {self.a}
                The side b of the triangle is {self.b}  
                The side c of the triangle is {self.c}
                The Angle A of the triangle is {self.angA}
                The Angle B of the triangle is {self.angB}
                The Angle C of the triangle is {self.angC}
        """)

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
                self.a=(self.b*sin(self.angA))/sin(self.angB)
                return self.a, self.b, self.c, self.angA, self.angB, self.angC


        if self.type == "r".lower() or self.type == "r".upper():
            self.angB=90

            if self.a != 0 and self.b != 0 and self.c == 0 and self.angA == 0 and self.angB == 0 and self.angC == 0:
                self.angA = atan(self.a / self.b)
                self.angC=90-self.angA
                self.c=(self.b**2-self.a**2)**0.5
                return self.a, self.b, self.c, self.angA, self.angB, self.angC

            if self.a == 0 and self.b != 0 and self.c != 0 and self.angA == 0 and self.angB == 0 and self.angC == 0:
                self.angA=atan(self.c/self.a)
                self.angC=90-self.angA
                self.a = (self.b ** 2 - self.c ** 2) ** 0.5
                return self.a, self.b, self.c, self.angA, self.angB, self.angC


        if self.type == "":
            # for SSS
            if self.a != 0 and self.b != 0 and self.c != 0 and self.angA == 0 and self.angB == 0 and self.angC == 0:
                self.cosine_rule_find_angB()
                self.cosine_rule_find_angA()
                self.cosine_rule_find_angC()
                return self.a, self.b, self.c, self.angA, self.angB, self.angC

                # for SAS
            if self.a != 0 and self.b != 0 and self.c == 0 and self.angA == 0 and self.angB != 0 and self.angC == 0:
                self.angA=(self.a*sin(self.angB)/self.b)
                self.angC=180-(self.angA+self.angB)
                self.c=(self.b * sin(self.angC) / sin(self.angB))
                return self.a, self.b, self.c, self.angA, self.angB, self.angC

            if self.a != 0 and self.b == 0 and self.c != 0 and self.angA == 0 and self.angB == 0 and self.angC != 0:
                self.angA = (self.a * sin(self.angC) / self.c)
                self.angB = 180 - (self.angA + self.angC)
                self.b = (self.c * sin(self.angB) / sin(self.angC))
                return self.a, self.b, self.c, self.angA, self.angB, self.angC


            if self.a == 0 and self.b != 0 and self.c != 0 and self.angA != 0 and self.angB == 0 and self.angC == 0:
                self.angB = (self.b * sin(self.angA) / self.a)
                self.angC = 180 - (self.angA + self.angB)
                self.a = (self.b * sin(self.ang) / sin(self.angB))
                return self.a, self.b, self.c, self.angA, self.angB, self.angC

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





class Equilateral_Triangle(Triangle):
    pass

class Isosceles_Triangle(Triangle):
    pass

class Scalene_Triangle(Triangle):
    pass

def print_func_one():
    print("Please Go through the instructions given and enter the correct values:")

def input_requirements_to_draw_triangle():
    print("""
            We need the following Minimum requirements Drawing the triangles any one of them
            
                                         A
                                        / \.
                                      b/   \c               Fig One
                                      /     \.
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
                                         / \.
                                      a /   \ a     Fig Two 
                                       /     \.
                                      B-------C
                                          a
                                     
                         




            5.For Equilateral Triangle:   1.(Any one Side) 
                #Any one of the below combination
                                    From Fig Two. 1.1. (a) - Any one side since all sides are equal (a = b = c)
                                             
                                    Combinations:
                                             1. (a) 
                                             
                                                   
                                     Isosceles Triangle (Two equal sides)
                                          A
                                         /|\.
                                        / | \.
                                      b/  |  \.b Fig Three
                                      /   |   \.
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
            
            """)



triangle=Triangle(a=4)
triangle.a=5
triangle.ok()
print(triangle.a)





