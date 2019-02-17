import turtle
import math
import random
score =0
f=0
wn=turtle.Screen()
wn.bgcolor("black")
pen=turtle.Turtle()
pen.color("white")
pen.speed(0)
pen.penup()
pen.setposition(-300,-300)
pen.pendown()
pen.pensize(3)
for i in range(4):
    pen.fd(600)
    pen.lt(90)
pen.hideturtle()
pen.penup()
pennn=turtle.Turtle()
pennn.color("white")
pennn.speed(0)
pennn.penup()
pennn.pensize(3)
pennn.hideturtle()
pennn.setposition(-250,250)
pennn.write("Score={}".format(score),font=("Arial",14,"normal"))
#gamers
tri=turtle.Turtle()
tri.shape("triangle")
tri.color("blue")
tri.speed(0)
tri.penup()
tri.goto(0,-250)
tri.setheading(90)
#enemy
enemysize=5
enimies=[]
for i in range(enemysize):

    en=turtle.Turtle()
    enimies.append(en)
for en in enimies:
    en.shape("circle")
    en.color("red")
    en.speed(0)
    en.penup()
    x=random.randint(-200,250)
    y=random.randint(100,250)
    en.setposition(x,y)
espeed=2

#weapon
we=turtle.Turtle()
we.shape("triangle")
we.shapesize(0.5,0.5)
we.color("yellow")
we.speed(0)
we.setheading(90)
we.penup()
we.hideturtle()
bulletspeed=20
bulletstate="ready"




def move_left():
    x=tri.xcor()
    tri.setx(x-10)
    if(tri.xcor()<-280):
        tri.setx(-280)

def mov_right():
    tri.setx(tri.xcor()+10)
    if (tri.xcor()>280):
        tri.setx(280)
def fire_bullet():
    global bulletstate
    if bulletstate=="ready":
        bulletstate="fire"
        y=tri.ycor()+10
        x=tri.xcor()
        we.setposition(x,y)
        we.showturtle()
def iscollision(t1,t2):
    x1=t1.xcor()
    x2=t2.xcor()
    y1=t1.ycor()
    y2=t2.ycor()
    distance=math.sqrt(math.pow(x1-x2,2)+math.pow(y1-y2,2))
    if(distance<15):
        return True
    else:
        return False



wn.listen()
wn.onkeypress(mov_right,"d")
wn.onkeypress(move_left,"a")
wn.onkeypress(fire_bullet,"space")

while True:
    for en in enimies:

        x=en.xcor()
        en.setx(x + espeed)
        if(en.xcor()>280):
            for e in enimies:

                y=e.ycor()
                y-=40
                e.sety(y)
            espeed *= -1
        elif(en.xcor()<-280):

            for e in enimies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            espeed *= -1
        if (iscollision(en, we) == True):
            we.setposition(0, -400)
            we.hideturtle()
            bulletstate = "ready"
            x=random.randint(-200,250)
            y=random.randint(100,250)
            en.setposition(x, y)
            score=score+10
            pennn.clear()
            pennn.write("Score={}".format(score), font=("Arial", 14, "normal"))

        if (iscollision(tri, en) == True or en.ycor()<=tri.ycor()):
            penn = turtle.Turtle()
            penn.shape("square")
            penn.color("red")
            penn.hideturtle()
            for e in enimies:
                e.hideturtle()
            penn.write("Game Over", align="center", font=("Arial", 24, "normal"))
            penn.hideturtle()
            f=1
            break
    if(f==1):
        break
    #move the bullet
    if(bulletstate=="fire"):

        y=we.ycor()
        we.sety(y+bulletspeed)
        if(we.ycor()>280):
            bulletstate="ready"
            we.hideturtle()




    wn.update()









wn.mainloop()

