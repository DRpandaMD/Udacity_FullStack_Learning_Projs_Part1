import turtle
def draw_square():
    bradly = turtle.Turtle()
    bradly.shape("turtle")
    bradly.color("white")
    bradly.speed(3)

    for i in xrange(0, 4):
        bradly.forward(200)
        bradly.right(90)
        pass
    pass

def draw_circle():
    mikey = turtle.Turtle()
    mikey.shape("turtle")
    mikey.color("red")
    mikey.speed(3)
    mikey.circle(100)
    pass

def draw_triangle():
    billy = turtle.Turtle()
    billy.shape("arrow")
    billy.color("blue")
    billy.speed(3)

    for i in range(0, 3):
        billy.backward(180)
        billy.left(120)
        pass
    pass

def draw_cirlce_from_squares():
    bobby = turtle.Turtle()
    bobby.shape("turtle")
    bobby.color("green")
    bobby.speed(3)

    for j in range(0,36):
        for i in xrange(0, 4):
            bobby.forward(150)
            bobby.right(90)
            
        bobby.right(10)
    pass


window = turtle.Screen()
window.bgcolor("black")

draw_square()
draw_circle()
draw_triangle()
draw_cirlce_from_squares()



window.exitonclick()
