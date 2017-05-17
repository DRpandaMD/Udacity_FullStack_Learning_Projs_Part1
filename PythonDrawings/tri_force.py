import turtle
# following an example from http://stackoverflow.com/questions/25772750/sierpinski-triangle-recursion-using-turtle-graphics
# I have never actually made a fractal and it has been a while since ive done any recursion
# And I have never done any type of recursion in python so lets give this a go and see what I can figure out.


# The idea here is that we take the lenght and depth of side and how many times we want this thing to run
# for each pass in the recurison the lenght with be divided by two and its level -1 
# we break out of the recursion when we have met the criteria for the 0th level
# then jump our way back through the stack

def draw_tri_force(length, depth):
    if depth == 0:  # from my coomputer science classes this is our BASE CASE
        link.begin_fill()
        for i in range(3):
            link.forward(length)
            link.left(120)
        link.end_fill()     
    else:
        draw_tri_force(length/2, depth - 1)
        link.forward(length/2)
        draw_tri_force(length/2, depth - 1)
        link.backward(length/2)
        link.left(60)
        link.forward(length/2)
        link.right(60)
        draw_tri_force(length/2, depth - 1)
        link.left(60)
        link.backward(length/2)  # this bit right here resets the start position
        link.right(60)
    return


# set up drawing canvas
window = turtle.Screen()
window.bgcolor("black")

# taking insperation from 4chan and Ledgend of Zelda 
# link will be our little artist 
link = turtle.Turtle()
link.shape("arrow")
link.color("gold")
link.speed(10)

# didn't like how the the drawing started in the middle of my canvas
# so i dicieded to move it
link.hideturtle()
link.penup()
link.goto(-200, -100)
link.pendown()

draw_tri_force(360, 3)


window.exitonclick()


