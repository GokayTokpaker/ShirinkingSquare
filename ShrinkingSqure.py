import turtle

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("light green")
turtle_screen.title("ShrinkingSqure")

turtle_instance = turtle.Turtle()
turtle_instance.color("blue")

def ShirinkingSquare(size):
    for i in range(4):
        turtle_instance.forward(size)
        turtle_instance.left(90)
        size=size-5

ShirinkingSquare(110)
ShirinkingSquare(90)
ShirinkingSquare(70)
ShirinkingSquare(50)
ShirinkingSquare(30)
turtle.done()