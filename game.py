import pygame, sys, os
from pygame.locals import *

# set up the colors
BLACK = (0, 0, 0)
BG_COLOR = (168, 165 , 160)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# mouse buttons
LEFT = 1
MIDDLE = 2
RIGHT = 3

class game:
    
    def __init__(self):
        # set up pygame
        pygame.init()
        
        # set up the window
        self.screen = pygame.display.set_mode((800, 600), 0, 32)
        pygame.display.set_caption('Human Evolution!')

        # set up fonts
        basicFont = pygame.font.Font('res' + os.sep + 'EBGaramond08-Regular.ttf', 30)

        # draw the white background onto the surface
        self.screen.fill(BLACK)

        # set up the text
        text = basicFont.render('Once upon a time on our blue planet...', True, WHITE)
        textRect = text.get_rect()
        textRect.centerx = self.screen.get_rect().centerx
        textRect.centery = self.screen.get_rect().centery
        # draw the text onto the surface
        self.screen.blit(text, textRect)

    def run(self):
        while True:
            event = pygame.event.wait()
            if event.type == QUIT:
                return
            if event.type == KEYUP and event.key == K_ESCAPE:
                return
            if event.type == MOUSEBUTTONUP and event.button == LEFT:
                self.screen.fill(BLACK)
            pygame.display.update()

    def close(self):
        pygame.quit()


# draw a blue circle onto the surface
#pygame.draw.circle(windowSurface, BLUE, (300, 50), 20, 0)

# draw a red ellipse onto the surface
#pygame.draw.ellipse(windowSurface, RED, (300, 250, 40, 80), 1)



aGame = game()
aGame.run()
aGame.close()
