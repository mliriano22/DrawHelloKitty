import turtle as t

def head(r):

    t.forward(r)
    t.circle(r, 130)
    t.circle(r, -130)
    t.backward(r)
    t.circle(r, -130)
    t.left(90)
    t.circle(r/2,-90)
    t.right(45)
    t.circle(r, -45)
    t.right(140)
    t.forward(r)
    t.right(140)
    t.circle(r,-45)
    t.right(30)
    t.circle(r/2,-90)


def features(r,a):
    t.seth(a)
    for i in range(2):
        t.circle(r,90)
        t.circle(r//2,90)

def bow(r,bowcolor):
    t.fillcolor(bowcolor)
    t.begin_fill()

    t.right(120)
    t.circle(r*3, 90)
    t.right(-45)
    t.circle(r*5,60)
    t.right(-45)
    t.circle(r*3,90)
    t.right(130)
    t.circle(r * 3, 90)
    t.right(-35)
    t.circle(r * 5, 60)
    t.right(-50)
    t.circle(r * 3, 90)

    t.end_fill()

    t.right(40)
    t.circle(r,-120)
    t.right(20)
    t.circle(r, -120)
    t.right(140)
    t.forward(r)
    t.right(150)
    t.circle(r,-120)
    t.right(20)
    t.circle(r, -120)
    t.pu()
    t.setpos(r * 5, r * 7)
    t.pd()

    t.begin_fill()

    t.circle(r,360)

    t.end_fill()


def whiskers(a,r):
    t.right(a)
    t.forward(r)

def drawhk(r):

    bowcolor=str(input("Enter a bow color. For example, pink\n"))

    #speed
    t.speed(0)

    #bold outline
    t.pensize(r//10)
    t.pu()

    #head
    t.setpos(-r*2,-r*2)
    t.pd()
    head(r*5)
    t.pu()


    #nose
    t.fillcolor("yellow")
    t.begin_fill()

    t.setpos(0, 0)
    t.pd()
    features(r,-45)
    t.pu()

    t.end_fill()

    #right eye
    t.fillcolor("black")
    t.begin_fill()

    t.setpos(r*3+r,r)
    t.pd()
    features(r, 45)
    t.pu()

    t.end_fill()

    #left eye
    t.fillcolor("black")
    t.begin_fill()

    t.setpos(-r*2,r)
    t.pd()
    features(r, 45)
    t.pu()

    t.end_fill()



    #whiskers
    t.setpos(r*7,r*2)
    t.pd()
    whiskers(40,r*3)
    t.pu()

    t.setpos(-r * 6, r * 2)
    t.pd()
    whiskers(190, r * 3)
    t.pu()

    t.setpos(r*7,r)
    t.pd()
    whiskers(175,r*3)
    t.pu()

    t.setpos(-r * 6, r)
    t.pd()
    whiskers(180, r * 3)
    t.pu()

    t.setpos(r*7-r/4,r-r/2)
    t.pd()
    whiskers(190,r*3)
    t.pu()

    t.setpos(-r * 6 + r/3, r-r/2)
    t.pd()
    whiskers(160, r * 3)
    t.pu()

    #bow
    t.setpos(r*4,r*7)
    t.pd()
    bow(r*2-r,bowcolor)

    t.ht()

    t.done()

