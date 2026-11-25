import pgzrun
from random import randint
from time import time

WIDTH = 800
HEIGHT = 600

TITLE = "Connecting Stars"

start_time=0 
total_time = 0
end_time = 0

next_stars = 0
gameover=False

number_of_stars = 8
lines=[]
stars = []

def create_stars():
    global start_time
    for count in range (0,number_of_stars):
        star= Actor("star-removebg-preview.png")
        star.pos = (randint(40, WIDTH - 40),randint(40, HEIGHT -40))
        stars.append(star)
    start_time = time()    

def draw():
    global total_time
    screen.blit("background1",(0,0))
    number=1
    for star in stars:
        screen.draw.text(str(number),(star.pos[0],star.pos[1]+ 20))   
        star.draw()
        number += 1
    for line in lines:
        screen.draw.line(line[0],line[1],(255,255,255))
    if next_stars<number_of_stars:
        total_time=time()-start_time
        screen.draw.text(str (round(total_time, 1)),(10,10), fontsize = 30 )
    else:
        screen.draw.text(str(round(total_time, 1)),(10,10), fontsize = 30 )

def update():
    pass
def on_mouse_down(pos):
     global next_stars, lines
     if next_stars<number_of_stars:
         if stars[next_stars].collidepoint(pos):
             if next_stars:
                 lines.append((stars[next_stars - 1].pos, stars[next_stars].pos))
             next_stars += 1    
         else:
             lines = []     
             next_stars = 0 

         

create_stars()
pgzrun.go()