from pico2d import *
import math

def square():
    y = 80
    x = 400
    while (x < 700):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x = x + 2
    while (y < 500):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y = y + 2
    while (x >= 100):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x = x - 2
    while (y >= 80):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y = y - 2
    while (x <= 400):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x = x + 2

def circle():
    y = 300
    x = 400
    temp = 0
    while (temp <= 2 * math.pi):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x + 200*math.sin(temp),y + 200*math.cos(temp))
        temp = temp + 0.1
        delay(0.05)
        
open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

while (1):
    square()
    circle()

close_canvas()
#Done
