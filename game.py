import pygame, pygame.gfxdraw, sys, element, operator
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
        if INTRO == True:
            self.intro = number(0)
            self.tutorial = number(-1)
            self.game = number(-1)
        else:
            self.intro = number(-1)
            self.tutorial = number(-1)
            self.game = number(1)
        self.scenes = [self.intro, self.tutorial, self.game]
        self.sceneText = {self.intro: T_intro, self.tutorial: T_tutorial}
        self.currentScene = 0

        # set up fonts
        self.logoText = pygame.font.Font(PATH + FONT_GARAMOND, 60)
        self.introText = pygame.font.Font(PATH + FONT_GARAMOND, 30)
        self.descriptionText = pygame.font.Font(PATH + FONT_GARAMOND, 22)
        self.captionText = pygame.font.Font(PATH + FONT_GARAMOND, 14)
        
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
        pygame.gfxdraw.hline(self.screen, 0, 800, 120, DGRAY)
        pygame.gfxdraw.aacircle(self.screen, 200, 300, 120, DGRAY)
        pygame.gfxdraw.aacircle(self.screen, 800-200, 300, 120, DGRAY)
        self.drawArray()
        self.drawElements()
        
    def drawArray(self):
        pygame.gfxdraw.line(self.screen, 350, 280, 420, 280, DGRAY)
        pygame.gfxdraw.line(self.screen, 350, 600-280, 420, 600-280, DGRAY)

        a = tuple(map(operator.add,(450, 300) ,tuple(1.7 * i for i in(-30, -20))))
        b = (a[0],600-a[1])
        pygame.draw.aaline(self.screen, DGRAY, a, (450, 300))
        pygame.draw.aaline(self.screen, DGRAY, b, (450, 300))

    def drawElements(self):
        pygame.gfxdraw.aacircle(self.screen, 30, 30, 20, WHITE)
        ele = pygame.image.load(PATH + 'CO2.png')
        eleRect = ele.get_rect()
        eleRect.center = (30,30)
        text = self.captionText.render('Carbon dioxide', True, BLACK)
        textRect = text.get_rect()
        textRect.center = (30, 45)
        self.screen.blit(ele, eleRect)
        self.screen.blit(text, textRect)

    #def DrawTarget(self):
    
    # outside antialiased circle
    #pygame.gfxdraw.aacircle(self.image, self.rect.width/2, self.rect.height/2, self.rect.width/2 - 1, self.color)

    # outside filled circle
    #pygame.gfxdraw.filled_ellipse(self.image, self.rect.width/2, self.rect.height/2, self.rect.width/2 - 1, self.rect.width/2 - 1, self.color)
    
    
    #temp = pygame.Surface((TARGET_SIZE,TARGET_SIZE), SRCALPHA) # the SRCALPHA flag denotes pixel-level alpha
    
    #self.image.blit(temp, (0,0), None, BLEND_ADD)


aGame = game()
aGame.run()
aGame.close()
