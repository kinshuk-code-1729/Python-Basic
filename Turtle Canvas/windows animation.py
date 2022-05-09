import turtle
t = turtle
t.speed(1)
t.bgcolor('black')
t.penup()
t.goto(-50,60)
t.pendown()
t.color('green')
turtle.begin_fill()
turtle.goto(100,100)
turtle.goto(100,-100)
#Draw Windows
turtle.goto(-50,-60)
turtle.goto(-50,60)
turtle.end_fill()
turtle.color('black')
turtle.goto(15,100)
#Cut into two equal parts
turtle.color('black')
turtle.width(10)
turtle.goto(15,-100)
turtle.penup()
