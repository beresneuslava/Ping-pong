from pygame import *
from random import randint


WIDTH = 600
HEIGHT = 500
FPS = 60
WIN_SCORE = 10
RESTART_TIME = 3000

GREEN = (0, 150, 0)
RED = (150, 0, 0)
wHITE = (255, 255, 255)

def generate_color():
    return (randint(0, 255), randint(0,255), randint(0,255))

background = generate_color()
window = display.set_mode((WIDTH,HEIGHT))
display.set_caption("PING-PONG")
clock = time.Clock()

run = True
finish = False

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    if not finish:
        window.fill(background)

    display.update()
    clock.tick(FPS)