import pygame, pygame.gfxdraw, sys, element, operator, TextProvider, copy
from pygame.locals import *
from constants import *
from util import number
from math import sqrt

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
        self.pickup = None
        self.middleAreas = [MiddleArea(200,300,120),MiddleArea(800-200, 300, 120)]
        self.reactants = []

        # set up fonts
        TextProvider.init()

        self.generateElements()
        self.sprites = copy.copy(self.elements)
        
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
            else:
                if event.type == MOUSEBUTTONDOWN and event.button == LEFT:
                    for s in self.sprites:
                        if s.isClicked(event.pos):
                            if s in self.reactants:
                                self.reactants.remove(s)
                                self.pickup = s
                            else:
                                self.pickup = copy.copy(s)
                if event.type == MOUSEBUTTONUP and event.button == LEFT:
                    if self.pickup is not None:
                        if self.middleAreas[0].isinDrop(event.pos ):
                            self.reactants.append(self.pickup)
                            self.sprites.append(self.pickup)
                            self.react()
                        self.pickup = None
                if event.type == MOUSEMOTION:
                    if self.pickup is not None:
                        self.pickup.coords = event.pos
                        
    def renderIntro(self):
        self.screen.fill(BLACK)

        if self.intro.number == 0:
            text = TextProvider.logoText.render(T_logo, True, WHITE)
        else:
            text = TextProvider.introText.render(T_intro[self.intro.number - 1], True, WHITE)
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
        text = TextProvider.introText.render(T_tutorial[self.tutorial.number - 1], True, WHITE)
        textRect = text.get_rect()
        textRect.midbottom = (self.screen.get_rect().midbottom[0], self.screen.get_rect().midbottom[1]-20)
        self.screen.blit(text, textRect)
        
    def renderGame(self):
        self.screen.fill(BG_COLOR)
        pygame.gfxdraw.hline(self.screen, 0, 800, 120, DGRAY)
        for a in self.middleAreas:
            a.draw(self.screen)
        self.drawArrow()
        self.drawElements()
        if self.pickup is not None:
            self.pickup.drawfree()
        self.drawReactants()
        
    def drawArrow(self):
        pygame.gfxdraw.line(self.screen, 350, 280, 420, 280, DGRAY)
        pygame.gfxdraw.line(self.screen, 350, 600-280, 420, 600-280, DGRAY)

        a = tuple(map(operator.add,(450, 300) ,tuple(1.7 * i for i in(-30, -20))))
        b = (a[0],600-a[1])
        pygame.draw.aaline(self.screen, DGRAY, a, (450, 300))
        pygame.draw.aaline(self.screen, DGRAY, b, (450, 300))

    def drawElements(self):
        pos = 0
        for e in self.elements:
            if e.active == True:
                e.draw(pos)
                pos += 1

    def generateElements(self):
        self.elements = []
        for e in ElementLabels.keys():
            self.elements.append(element.Element(self.screen, e))
            
    def drawReactants(self):
        for r in self.reactants:
            r.drawfree()

    def react(self):
        pass
        
class MiddleArea:
    def __init__(self,x,y,r):
        self.centerx = x
        self.centery = y
        self.radius = r
	
    def draw(self, screen):
        pygame.gfxdraw.aacircle(screen, self.centerx, self.centery, self.radius, DGRAY)

    def isinDrop(self, pos):
        return sqrt((self.centerx - pos[0])**2 + (self.centery - pos[1])**2) <= self.radius - (ELEMENT_RADIUS-2)

aGame = game()
aGame.run()
aGame.close()
