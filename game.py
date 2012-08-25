import pygame, sys, os
from pygame.locals import *
from constants import *
from util import number

class game:
    
    def __init__(self):
        # set up pygame
        pygame.init()
        
        # set up the window
        self.screen = pygame.display.set_mode((800, 600), 0, 32)
        pygame.display.set_caption('Human Evolution')
        self.intro = number(0)
        self.tutorial = number(-1)
        self.game = number(-1)
        self.scenes = [self.intro, self.tutorial, self.game]
        self.sceneText = {self.intro: T_intro, self.tutorial: T_tutorial}
        self.currentScene = 0

        # set up fonts
        self.logoText = pygame.font.Font('res' + os.sep + FONT_GARAMOND, 60)
        self.introText = pygame.font.Font('res' + os.sep + FONT_GARAMOND, 30)
        self.descriptionText = pygame.font.Font('res' + os.sep + FONT_GARAMOND, 22)
        
    def close(self):
         pygame.quit()

    def run(self):
        while True:
            if self.intro.number != -1:
                self.renderIntro()
            else:
                self.renderGame()
            if self.tutorial.number != -1:
                self.renderTurorial()
                
            pygame.display.update()
            event = pygame.event.wait()
            if event.type == QUIT:
                return
            if event.type == KEYUP and event.key == K_F4 and bool(event.mod & KMOD_ALT):
                return
            if self.game.number != 1:
                if event.type == MOUSEBUTTONDOWN and event.button == LEFT:
                    self.advanceScene()
                        
    def renderIntro(self):
        self.screen.fill(BLACK)

        if self.intro.number == 0:
            text = self.logoText.render(T_logo, True, WHITE)
        else:
            text = self.introText.render(T_intro[self.intro.number - 1], True, WHITE)
        textRect = text.get_rect()
        textRect.centerx = self.screen.get_rect().centerx
        textRect.centery = self.screen.get_rect().centery
        self.screen.blit(text, textRect)

    def advanceScene(self):
        if self.scenes[self.currentScene].number < len(self.sceneText[self.scenes[self.currentScene]]):
            self.scenes[self.currentScene].number +=1
        else:
            self.scenes[self.currentScene].number = -1
            self.currentScene += 1
            self.scenes[self.currentScene].number = 1
            
    def renderTurorial(self):
        text = self.introText.render(T_tutorial[self.tutorial.number - 1], True, WHITE)
        textRect = text.get_rect()
        textRect.midbottom = (self.screen.get_rect().midbottom[0], self.screen.get_rect().midbottom[1]-20)
        self.screen.blit(text, textRect)
        
    def renderGame(self):
        self.screen.fill(BG_COLOR)
        pygame.draw.circle(self.screen, BLUE, (300, 50), 20, 0)


aGame = game()
aGame.run()
aGame.close()
