import turtle as t

tim=t.Turtle()

def draw_shapes(num_sides):
    angle=360/num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for shap_side in range(3,10):
    draw_shapes(shap_side)











screen=t.Screen()
screen.exitonclick()