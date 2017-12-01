"""planets.py: A homework to roughly modify the movements of the planets.

__author__ = "胡奕潇"
__pkuid__  = "1700011716"
__email__  = "1700011716@pku.edu.cn"

I DON'T KNOW WHICH TYPES OF THE FILE IS REQUIRED, SO THERE IS TWO KIND OF ANSWERS.
"""

import math
import turtle

def start(name,q):
    name.up()
    name.speed("fast")
    name.goto(2/3*q,0)
    name.down()
    name.shape("circle")

    
def main():
    turtle.color("red")
    turtle.shape("circle")
    turtle.shapesize(2)
    turtle.up()
    
    sc=turtle.Screen()
    sc.bgcolor("darkblue")
    
    alice=turtle.Turtle()
    alice.color("aliceblue")
    bob=turtle.Turtle()
    bob.color("blanchedalmond")
    cindy=turtle.Turtle()
    cindy.color("yellow")
    dave=turtle.Turtle()
    dave.color("lightpink")
    eve=turtle.Turtle()
    eve.color("lawngreen")
    fiona=turtle.Turtle()
    fiona.color("orange")

    start(alice,120)  
    start(bob,67)
    start(cindy,270)
    start(dave,300)
    start(eve,405)
    start(fiona,286)
    
    for an in range(500):
        def move(name,e,p,sp):
            ang=an*(math.pi/180)
            t=e*p/(1-e*math.cos(ang*sp))
            x=t*math.cos(ang*sp)
            y=t*math.sin(ang*sp)
            name.goto(x,y)
        move(alice,0.4,120,6)
        move(bob,0.2,180,8)
        move(cindy,0.6,120,4)
        move(dave,0.4,300,3)
        move(eve,0.2,1080,2)
        move(fiona,0.5,190,3.5)
        
           

if __name__ == '__main__':
    main()

   