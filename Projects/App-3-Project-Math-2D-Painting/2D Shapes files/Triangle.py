
class Triangle:
    def __init__(self,a=0,b=0,c=0,ang1=0,ang2=0,ang3=0,type=""):

        self.a= a
        self.b = b
        self.c = c
        self.ang1=ang1
        self.ang2=ang2
        self.ang3=ang3
        self.type=type

    def ok(self):
        pass




class Equilateral_Triangle(Triangle):
    pass

class Isosceles_Triangle(Triangle):
    pass

class Scalene_Triangle(Triangle):
    pass


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
                                    From Fig One. 1.(a, b, angC) 
                                                  2.(b, c, angA)
                                                  3.(c, a, angB)
            
            3.ASA(Angle-Side-Angle): 1.(Two Angles and the included Side)
                
                #Any one of the below combination
                                     From Fig One. 1.(angA, b, angB) 
                                                   2.(angB, c, angC)
                                                   3.(angC, a, angA)
            
            4.AAS(Angle-Angle-Side): 1.(Two Angles and one side not in between them) 
                
                #Any one of the below combination
                                    From Fig One. 1.(angA, angB, a) 
                                                   2.(angA, angC, b)
                                                   3.(angC, a, angA)
                                                   4.(angB, angC, c)
                                                   5.(angC, angA, a)
                                                   6.(angC, angB, b)
                                                   

            5.For Equilateral Triangle:   1.(Any one Side) 
                #Any one of the below combination
                                    From Fig One. 1.a
                                                   2.b
                                                   3.c

            6.For Isosceles Triangle: 1.(One of the equal sides and the base) 
                                    2.(one of the equal sides and the included angle)
            
            7.For Right Angle Triangle: 1.(The two sides opposite of hypotenuse)
                                      2.(Hypotenuse and one other side any)
                                    
            
            
            
            
            
            """)

triangle=Triangle(a=4)
triangle.a=5
triangle.ok()
print(triangle.a)





