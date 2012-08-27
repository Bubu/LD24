import pygame, pygame.gfxdraw, sys, element, operator, TextProvider, copy
from pygame.locals import *
from constants import *
from util import number
from math import sqrt
MUSIC_END = pygame.USEREVENT + 1

class game:
    
    def __init__(self):
        pygame.mixer.pre_init(22050, -16, 2, 256)
        pygame.init()
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
        self.middleAreas = [MiddleArea(200,300+VERT_OFFSET,120),MiddleArea(800-200, 300+VERT_OFFSET, 120)]
        self.reactants = []
        self.products = []
        TextProvider.init()

        self.generateElements()
        self.sprites = copy.copy(self.elements)
        
        self.pages = [Page(1, self.elements),]
        self.activePage = self.pages[0]
        self.song = 0
        pygame.mixer.music.load(PATH + MUSIC[self.song])
        pygame.mixer.music.set_endevent(MUSIC_END)
        self.init = True
        self.sounds = {}
        for s in SOUNDS:
            self.sounds[s]= pygame.mixer.Sound(PATH + s)
        
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
                                self.sprites.remove(s)
                                self.react()
                                self.pickup = s
                            else:
                                self.pickup = copy.copy(s)
                            break
                        
                if event.type == MOUSEBUTTONUP and event.button == LEFT:
                    if self.pickup is not None:
                        if self.middleAreas[0].isinDrop(event.pos):
                            self.reactants.append(self.pickup)
                            self.sprites.append(self.pickup)
                            self.react()
                        self.pickup = None
                if event.type == MOUSEMOTION:
                    pygame.time.wait(5)
                    if self.pickup is not None:
                        self.pickup.coords = event.pos
            if event.type == MUSIC_END:
                self.handleMusic()
                        
    def renderIntro(self):
        self.screen.fill(BLACK)

        if self.intro.number == 0:
            text = pygame.image.load(PATH + 'title.png')
            #it's not text... too lazy
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
        if self.init:
            pygame.mixer.music.play()
            self.init = False
            
        self.screen.fill(BG_COLOR)
        self.drawPages()
        self.drawMute()
        pygame.gfxdraw.hline(self.screen, 0, 800, 180, DGRAY)
        for a in self.middleAreas:
            a.draw(self.screen)
        self.drawArrow()
        self.drawElements()
        if self.pickup is not None:
            self.pickup.drawfree()
        self.drawReactants()
        self.drawProducts()
        
    def drawArrow(self):
        pygame.gfxdraw.line(self.screen, 350, 280+VERT_OFFSET, 420, 280+VERT_OFFSET, DGRAY)
        pygame.gfxdraw.line(self.screen, 350, 600-280+VERT_OFFSET, 420, 600-280+VERT_OFFSET, DGRAY)

        a = tuple(map(operator.add,(450, 300+VERT_OFFSET) ,tuple(1.7 * i for i in(-30, -20))))
        b = (a[0],600-a[1]+VERT_OFFSET*2)
        pygame.draw.aaline(self.screen, DGRAY, a, (450, 300+VERT_OFFSET))
        pygame.draw.aaline(self.screen, DGRAY, b, (450, 300+VERT_OFFSET))

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
            
    def drawProducts(self):
        for p in self.products:
            p.drawfree()

    def react(self):
        self.products = []
        tmp_reactants = []
        for r in self.reactants:
            tmp_reactants.append(r.type)
        tmp_reactants = frozenset(Counter(tmp_reactants).items())
        if tmp_reactants in Reactions:
            self.sounds['react.wav'].play()
            tmp_products = Reactions[tmp_reactants]
            i = 0
            for p in tmp_products:
                e = element.Element(self.screen, p)
                e.coords = tuple(map(operator.add,(600,300+VERT_OFFSET),PositionMap[len(tmp_products)][i]))
                self.products.append(e)
                i +=1

    def drawPages(self):
        i = 1
        for p in self.pages:
            if p == self.activePage:
                frame = pygame.image.load(PATH + 'page_active.png')
                text = TextProvider.pageText.render(str(p.number), True, BLACK)
            else:
                frame = pygame.image.load(PATH + 'page_inactive.png')
                text = TextProvider.pageText.render(str(p.number), True, BLACK)

            
            pos = (p.number * 38 -19, 9)
            textRect = text.get_rect()
            textRect.center = frame.get_rect().center
            frame.blit(text, textRect)
            frameRect = frame.get_rect()
            frameRect.center = pos
            self.screen.blit(frame, frameRect)
            i+=1

        frame = pygame.image.load(PATH + 'page_inactive.png')
        text = TextProvider.pageText.render(str(p.number), True, BLACK)
        pos = (i * 38 -19, 9)
        frameRect = frame.get_rect()
        frameRect.center = pos
        self.screen.blit(frame, frameRect)

    def handleMusic(self):
        if self.song < len(MUSIC)-1:
            self.song +=1
        pygame.mixer.music.load(PATH + MUSIC[self.song])
        pygame.mixer.music.play()

    def drawMute(self):
        #need that... but later
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
    
class Page:
    def __init__(self, number, elements):
        self.number = number
        self.elements = elements

aGame = game()
aGame.run()
aGame.close()
