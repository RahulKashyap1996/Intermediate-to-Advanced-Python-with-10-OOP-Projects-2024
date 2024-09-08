import turtle
import random

# Create a turtle object for drawing
myTurtle = turtle.Turtle()


# Define the Point class
class Point:
    def __init__(self, x, y):
        """Initialize a point with x and y coordinates ok."""
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectanglex):
        """Check if the point falls within the given rectangle."""
        if rectanglex.point1.x < self.x < rectanglex.point2.x \
                and rectanglex.point1.y < self.y < rectanglex.point2.y:
            return True
        else:
            return False

    def falls_on_line(self, rectanglex, point):
        """Check if the point falls on any of the rectangle's sides."""
        if (((point.x == rectanglex.point1.x or point.x == rectanglex.point2.x) and (
                rectanglex.point1.y <= point.y <= rectanglex.point2.y)) or
                ((point.y == rectanglex.point1.y or point.y == rectanglex.point2.y) and (
                        rectanglex.point1.x <= point.x <= rectanglex.point2.x))):
            return True
        else:
            return False

    def distance_from_point(self, pointx):
        """Calculate the distance between two points."""
        dist = ((pointx.x - self.x) ** 2 + (pointx.y - self.y) ** 2) ** 0.5
        return dist

    def go_to_point(self):
        """Move the turtle to this point and mark it with a red dot."""
        myTurtle.pen(pendown=False)  # Lift the pen to move without drawing
        myTurtle.goto(self.x, self.y)  # Move to the point coordinates
        myTurtle.pen(pendown=True)  # Set the pen down to start drawing
        myTurtle.pencolor("red")  # Set the pen color to red
        myTurtle.dot(size=20)  # Mark the point with a dot


# Initialize two points to define the rectangle
point1 = Point(3, 4)
point2 = Point(10, 20)


# Define the Rectangle class
class Rectangle:
    def __init__(self, pointy, pointz):
        """Initialize a rectangle with two diagonal points."""
        self.point1 = pointy
        self.point2 = pointz

    def area_of_rectangle(self):
        """Calculate the area of the rectangle."""
        return (self.point2.y - self.point1.y) * (self.point2.x - self.point1.x)


# Define a subclass for a GUI rectangle that can be drawn
class GuiRectangle(Rectangle):
    def draw(self):
        """Draw the rectangle using the turtle graphics."""
        myTurtle.pen(pendown=False)  # Lift the pen to move without drawing
        myTurtle.pencolor("black")  # Set the pen color to black
        myTurtle.goto(self.point1.x, self.point1.y)  # Go to the first point
        myTurtle.tiltangle(180)  # Set the tilt angle for drawing

        myTurtle.pen(pendown=True)  # Put the pen down to start drawing
        myTurtle.left(90)
        myTurtle.forward(self.point2.x - self.point1.x)  # Draw the first side
        myTurtle.left(90)
        myTurtle.forward(self.point2.y - self.point1.y)  # Draw the second side
        myTurtle.left(90)
        myTurtle.forward(self.point2.x - self.point1.x)  # Draw the third side
        myTurtle.left(90)
        myTurtle.forward((self.point2.y - self.point1.y))  # Draw the fourth side


# Create a rectangle with two points
RectangleX = Rectangle(point1, point2)
print(f"falls in rectangle {point1.falls_in_rectangle(RectangleX)}")

# Create a random rectangle for GUI
rectangle = GuiRectangle(Point(random.randint(0, 500), random.randint(0, 500)),
                         Point(random.randint(500, 1000), random.randint(500, 1000)))

# Print the coordinates of the rectangle
print(f"The coordinates of the rectangle are Point 1 is {rectangle.point1.x}\
       and {rectangle.point1.y} \n  and Point 2 is {rectangle.point2.x}\
       and {rectangle.point2.y}")

# Get user input for a guess and validate input
try:
    user_guess = Point(float(input("Guess X: ")), float(input("Guess Y: ")))
except ValueError:
    print("Invalid input! Please enter a valid number.")

# Check if the guessed point falls inside the rectangle
print(f"The area you guessed falls inside the rectangle: {user_guess.falls_in_rectangle(rectangle)}")

# Get user input for the area and validate input
try:
    guessthearea = int(input("Please enter the area of the rectangle that you have guessed\n"))
    print(f"Your area was off by: {rectangle.area_of_rectangle() - guessthearea}")
except ValueError:
    print("Invalid input! Please enter a valid number.")

# Draw the rectangle and move to the guessed point
rectangle.draw()
user_guess.go_to_point()

# Check if the point lies on the rectangle's boundary
point3 = Point(rectangle.point1.x, rectangle.point1.y)
print(f"The point is lying on the line: {point3.falls_on_line(rectangle, point3)}")

# Set up turtle screen and exit on click
screen = turtle.Screen()
screen.screensize(2000, 2000)  # Set the screen size for better visibility
screen.exitonclick()  # Wait for user to click before closing
