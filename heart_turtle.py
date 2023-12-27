from turtle import *

# draw a heart
def draw_heart():
    shape("turtle")
    color("red")
    begin_fill()
    pensize(3)
    left(50)
    forward(133)
    circle(50,200)
    right(140)
    circle(50,200)
    forward(133)
    end_fill()
    hideturtle()
    done()

# draw an orange
def draw_orange():
    shape("turtle")
    speed(1.5)  
    
    color("orange")
    begin_fill()
    circle(100)
    end_fill()
    
    up()
    goto(50, 130)
    down()
    color("green")
    begin_fill()
    circle(20, 120)
    left(120)
    circle(20, 120)
    left(120)
    circle(20, 120)
    end_fill()
    hideturtle()
    done()

print("1 - draw a heart")
print("2- draw an orange")
choice=int(input("choose what you want to draw : "))
if choice==1:

    draw_heart()
elif choice==2:
    draw_orange()

