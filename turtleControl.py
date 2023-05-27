import turtle
from os import system


"""
movimentos:
    w: forward(speed)
    a: left(30°)
    s: backward
    d: right(30°)
    q: + 5º
    e: - 5°

    z: -speed
    x: +speed
    c: clear
    u: undo
    h: hide/showturtle
    p: penup/down
    i: show/hide turtle info
    r: -shape wid
    t: +shape wid
    f: -pensize
    g: +pensize
    v: stamp
    b: start/end fill
    y: change colors

shapes:
    1: classic
    2: arrow
    3: turtle
    4: circle
    5: square
    6: triangle
"""

def more_slow():
    global speed
    speed = max(speed - 1, 1)
    
def more_fast():
    global speed
    speed += 1

def more_shape_size():
    shape_size[0], shape_size[1] = shape_size[0]+1, shape_size[1]+1
    t.shapesize(*shape_size)
    
def less_shape_size():
    shape_size[0], shape_size[1] = max(shape_size[0]-1, 1), max(shape_size[1]-1, 1)
    t.shapesize(*shape_size)
    
def more_pen_size():
    global pen_size
    pen_size += 1
    t.pensize(pen_size)
    
def less_pen_size():
    global pen_size
    pen_size = max(pen_size-1, 1)
    t.pensize(pen_size)
    
def toggle_turtle():
    if t.isvisible():
        t.hideturtle()
    else:
        t.showturtle()

def toggle_pen():
    if t.isdown():
        t.penup()
    else:
        t.pendown()

def toggle_info():
    global show_info
    show_info = not show_info
    info()

def toggle_fill():
    global fill
    fill = not fill

    if fill:
        t.begin_fill()
    else:
        t.end_fill()

def change_color():
    color_input = turtle.textinput(
        "Color menu",
        "1 shape  2 pen  3 fill  4 background\n\nex: 1 blue 2 #FF0000\n(blue shape and red pen)"
        ).split(' ')

    try:
        for i in range(0, len(color_input), 2):
            target, color = color_input[i], color_input[i+1]
            match target:
                case '1':
                    t.color(color)
                case '2':
                    t.pencolor(color)
                case '3':
                    t.fillcolor(color)
                case '4':
                    s.bgcolor(color)
    except Exception as e:
        pass
    main()
    
def info():

    if show_info:
        system("cls || clear")
        print(f"""
position: {t.position()}
angle: {t.heading()}
pendown: {t.isdown()}
speed: {speed}
shap size {shape_size[0]}, {shape_size[1]}
pen size: {pen_size}
fill: {'opened' if fill else 'closed'}""")
        turtle.ontimer(info, 300)
    
    
def main():

    #movimentos
    s.onkeypress(lambda: t.left(30), 'a')
    s.onkeypress(lambda: t.right(30), 'd')
    s.onkeypress(lambda: t.backward(speed), 's')
    s.onkeypress(lambda: t.forward(speed), 'w')
    s.onkeypress(lambda: t.left(5), 'q')
    s.onkeypress(lambda: t.right(5), 'e')
    
    #comandos
    s.onkeypress(toggle_turtle, 'h')
    s.onkeypress(toggle_pen, 'p')
    s.onkeypress(more_fast, 'x')
    s.onkeypress(more_slow, 'z')
    s.onkeypress(t.undo, 'u')
    s.onkeypress(t.clear, 'c')
    s.onkeypress(toggle_info, 'i')
    s.onkeypress(more_shape_size, 't')
    s.onkeypress(less_shape_size, 'r')
    s.onkeypress(more_pen_size, 'g')
    s.onkeypress(less_pen_size, 'f')
    s.onkeypress(t.stamp, 'v')
    s.onkeypress(toggle_fill, 'b')
    s.onkeypress(change_color, 'y')
    
    #shapes
    s.onkeypress(lambda: t.shape('classic'), '1')
    s.onkeypress(lambda: t.shape('arrow'), '2')
    s.onkeypress(lambda: t.shape('turtle'), '3')
    s.onkeypress(lambda: t.shape('circle'), '4')
    s.onkeypress(lambda: t.shape('square'), '5')
    s.onkeypress(lambda: t.shape('triangle'), '6')
    
    s.listen()
    s.mainloop()

if __name__ == '__main__':
    t = turtle.Turtle()
    s = turtle.Screen()
    t.speed(0)

    show_info = False
    fill = False
    speed = 1
    shape_size = [1, 1]
    pen_size = 1
    
    main()

