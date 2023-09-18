from pico2d import *

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
    while (x >= 40):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x = x - 2
    while (y >= 80):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y = y - 2
    while (x <=400):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x = x + 2
        
open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

while (1):
    square()

close_canvas()
