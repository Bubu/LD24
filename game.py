import pygame, sys
from pygame.locals import *

# set up the colors
BLACK = (0, 0, 0)
BG_COLOR = (168, 165 , 160)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

def run():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            if event.type == KEYUP and event.key == K_ESCAPE:
                return

def init():
    # set up pygame
    pygame.init()
    
    # set up the window
    windowSurface = pygame.display.set_mode((800, 600), 0, 32)
    pygame.display.set_caption('Human Evolution!')

    # set up fonts
    basicFont = pygame.font.Font('EBGaramond08-Regular.ttf', 30)

    # draw the white background onto the surface
    windowSurface.fill(BLACK)

    # set up the text
    text = basicFont.render('Once upon a time on our blue planet...', True, WHITE)
    textRect = text.get_rect()
    textRect.centerx = windowSurface.get_rect().centerx
    textRect.centery = windowSurface.get_rect().centery
    # draw the text onto the surface
    windowSurface.blit(text, textRect)

    # draw the window onto the screen
    pygame.display.update()



# draw a green polygon onto the surface
#pygame.draw.polygon(windowSurface, GREEN, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))

# draw some blue lines onto the surface
#pygame.draw.line(windowSurface, BLUE, (60, 60), (120, 60), 4)
#pygame.draw.line(windowSurface, BLUE, (120, 60), (60, 120))
#pygame.draw.line(windowSurface, BLUE, (60, 120), (120, 120), 4)

# draw a blue circle onto the surface
#pygame.draw.circle(windowSurface, BLUE, (300, 50), 20, 0)

# draw a red ellipse onto the surface
#pygame.draw.ellipse(windowSurface, RED, (300, 250, 40, 80), 1)

# draw the text's background rectangle onto the surface
#pygame.draw.rect(windowSurface, RED, (textRect.left - 20, textRect.top - 20, textRect.width + 40, textRect.height + 40))

# get a pixel array of the surface
#pixArray = pygame.PixelArray(windowSurface)
#pixArray[480][380] = BLACK
#del pixArray



init()
run()
pygame.quit()
