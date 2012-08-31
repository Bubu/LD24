import pygame, TextProvider
from constants import *

class Sprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surface = None
    
    def draw(self, screen):
        pass
        
    def isClicked(self, pos):
        pass        
    def handleMouseDown(self):
        pass
    def handleMouseUp(self):
        pass
        
class ElementSprite(Sprite):
    def __init__(self, type, caption):
        super().__init__()
        self.type = type
        self.radius = ELEMENT_RADIUS
        self.surface = self.createSurface(caption)        
    
    def createSurface(self,caption)
        frame = pygame.image.load(PATH + 'empty.png')
        try:
            ele = pygame.image.load(PATH + self.type + '.png')
        except:
            ele = pygame.image.load(PATH + 'noimg.png')
        eleRect = ele.get_rect()
        eleRect.center = frame.get_rect().center
        frame.blit(ele,eleRect)
        frameRect = frame.get_rect()
        frameRect.center = self.coords
        text = TextProvider.captionText.render(self.label, True, BLACK)
        textRect = text.get_rect()
        textRect.center = (self.coords[0],self.coords[1]+35)
        self.game.screen.blit(frame, frameRect)        
        self.game.screen.blit(text, textRect)
        return surface
        
    def isClicked(self, pos): #TODO: needs radius
        posSprite = pygame.sprite.Sprite()
        posSprite.rect = pygame.Rect(pos[0],pos[1],0,0)
        if pygame.sprite.collide_circle(self,posSprite):
            return True
        else:
            return False            
    def handleMouseDown(self):
        pass
    def handleMouseUp(self):
        pass
        
        
class PageSprite(Sprite):
    def __init__(self, number):
        super().__init__()
        self.number = number
        
    def isClicked(self, pos): #TODO: needs radius
        return self.rect.collidepoint(pos)
        
    def handleMouseDown(self):
        pass
    def handleMouseUp(self):
        pass