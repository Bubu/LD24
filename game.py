import pygame, sys, os
from pygame.locals import *
from constants import *



class game:
    
    def __init__(self):
        # set up pygame
        pygame.init()
        
        # set up the window
        self.screen = pygame.display.set_mode((800, 600), 0, 32)
        pygame.display.set_caption('Human Evolution')
        self.introStage = 0
        self.tutorial = -1

        # set up fonts
        self.logoText = pygame.font.Font('res' + os.sep + FONT_GARAMOND, 60)
        self.introText = pygame.font.Font('res' + os.sep + FONT_GARAMOND, 30)
        self.descriptionText = pygame.font.Font('res' + os.sep + FONT_GARAMOND, 22)
        
    def close(self):
         pygame.quit()

    def run(self):
        while True:
            if self.introStage != -1:
                self.renderIntro()
            else:
                self.renderGame()
            if self.turorial != -1:
                self.renderTurorial()
                
            pygame.display.update()
            event = pygame.event.wait()
            if event.type == QUIT:
                return
            if event.type == KEYUP and event.key == K_F4 and bool(event.mod & KMOD_ALT):
                return
            if event.type == MOUSEBUTTONDOWN and event.button == LEFT:
                self.advanceIntro()
                        
    def renderIntro(self):
        self.screen.fill(BLACK)

        if self.introStage == 0:
            text = self.logoText.render(T_logo, True, WHITE)
        else:
            text = self.introText.render(T_intro[self.introStage - 1], True, WHITE)
        textRect = text.get_rect()
        textRect.centerx = self.screen.get_rect().centerx
        textRect.centery = self.screen.get_rect().centery
        self.screen.blit(text, textRect)

    def advanceIntro(self):
        if self.introStage < len(T_intro):
            self.introStage +=1
        else:
            self.introStage = -1
            self.tutorial = 1
        
    def renderGame(self):
        self.screen.fill(BG_COLOR)
        
class TextHandler():
    def __init__(self):
        pass

# draw a blue circle onto the surface
#pygame.draw.circle(windowSurface, BLUE, (300, 50), 20, 0)



aGame = game()
aGame.run()
aGame.close()
