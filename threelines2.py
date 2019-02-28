# Sarah Murphy
#threelines2.py

import turtle as t


def draw_line(myturtle):
    myturtle.pd() #pendown
    myturtle.fd(200)
    myturtle.pu() #penup
    myturtle.fd(-200)



def draw_three_lines(myturtle):
    myturtle.left(90)

    draw_line(myturtle)

    myturtle.right(90)
    myturtle.fd(30)
    myturtle.left(90)

    draw_line(myturtle)

    myturtle.right(90)
    myturtle.fd(30)
    myturtle.left(90)

    draw_line(myturtle)

    myturtle.left(90)  # the last moves are to place larry back at start
    myturtle.fd(60)
    myturtle.right(180)

def main():

    wn = t.Screen()
    larry = t.Turtle()
    draw_three_lines(larry)

    wn.exitonclick()

main()