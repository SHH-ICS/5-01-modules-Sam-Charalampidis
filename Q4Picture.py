import pygame

from pygame import Color, Rect
from pygame import draw
from pygame import display

SCREEN_SIZE = (500, 500)
pygame.init()
gameDisplay = display.set_mode(SCREEN_SIZE)
gameDisplay.fill(Color('white'))
draw.rect(gameDisplay, Color('black'), Rect(100, 200, 300, 50))
draw.polygon(gameDisplay, Color('black'), [(100, 200), (400, 200), (250, 175)])
draw.circle(gameDisplay, Color('red'), (100, 100), 50)
draw.circle(gameDisplay, Color('red'), (400, 100), 50)
display.flip()
input("Press enter to exit")
