import random
import turtle as t

t.speed("fastest")

t.penup()
# go to bottom of image
t.goto((0, -300))

# turning the turtle to face upwards
t.right(-90)
t.pendown()

# function to plot a Y
def tree(sz, level, angle):
    if level > 0:
        # drawing the base
        t.width(level)
        t.forward(sz)

        t.right(angle)

        # recursive call for
        # the right subtree
        tree(0.8 * sz, level - 1, angle + random.randint(-10, 10))

        t.left(2 * angle)

        # recursive call for
        # the left subtree
        tree(0.8 * sz, level - 1, angle + random.randint(-10, 10))

        t.right(angle)
        t.forward(-sz)


# tree of size 80 and level 7
tree(150, 8, 30)
input()
