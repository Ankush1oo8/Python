import turtle as t
import random

tim=t.Turtle()
colors = ['black', 'white', 'red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink', 'brown', 'gray', 'cyan', 'magenta', 'turquoise', 'coral', 'crimson', 'gold', 'lime', 'maroon', 'navy', 'olive', 'orchid', 'peru', 'plum', 'salmon', 'sienna', 'teal', 'violet', 'wheat']
def draw_shapes(num_sides):
    angle=360/num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for shap_side in range(3,10):
    tim.color(random.choice(colors))
    draw_shapes(shap_side)











screen=t.Screen()
screen.exitonclick()