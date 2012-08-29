import pygame, TextProvider
from constants import *

class Page(pygame.sprite.Sprite): #should become just the object, seperate the sprite
    def __init__(self, number, elements,game):
        self.number = number
        self.elements = elements
        self.center = (self.number * 38 -19, 9)
        self.text = TextProvider.pageText.render(str(self.number), True, BLACK)
        frame = pygame.image.load(PATH + 'page_inactive.png')
        self.rect = frame.get_rect()
        self.rect.center = self.center
        self.textRect = self.text.get_rect()
        self.game = game

    def draw(self, screen, activePage):
        activePage
        if self is activePage:
            frame = pygame.image.load(PATH + 'page_active.png')
        else:
            frame = pygame.image.load(PATH + 'page_inactive.png')
        self.textRect.center = frame.get_rect().center
        frame.blit(self.text, self.textRect)
        frameRect = frame.get_rect()
        frameRect.center = self.center
        screen.blit(frame, frameRect)
        
    def isClicked(self,pos):
        return self.rect.collidepoint(pos)

    def handleClick(self):
        self.game.activePage = self