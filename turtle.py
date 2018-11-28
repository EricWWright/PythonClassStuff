import turtle
x = turtle.Pen()

x.speed(6)
for i in range(250):
    x.circle(i*1.5)
    x.left(20)
    if i % 5 == 0:
        x.color("red")
    elif i % 5 == 1:
        x.color("purple")
    elif i % 5 == 2:
        x.color("orange")
    elif i % 5 == 3:
        x.color("pink")
    elif i % 5 == 4:
        x.color("yellow")