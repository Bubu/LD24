import pygame, pygame.gfxdraw, TextProvider
from pygame.locals import *
from constants import *

class Element(pygame.sprite.Sprite):
	def __init__(self, screen, type):
		super().__init__()
		self.type = type
		self.label = ElementLabels[self.type]
		self.screen = screen
		self.active = True
		self.radius = ELEMENT_RADIUS
	
	def draw(self, pos):
		self.coords = (35 + pos*65,35)
		self.drawfree()
		
	def isClicked(self,pos):
		posSprite = pygame.sprite.Sprite()
		posSprite.rect = pygame.Rect(pos[0],pos[1],0,0)
		if pygame.sprite.collide_circle(self,posSprite):
			return True
		else:
			return False
	
	def drawfree(self):
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
		self.rect = frameRect
		text = TextProvider.captionText.render(self.label, True, BLACK)
		textRect = text.get_rect()
		textRect.center = (self.coords[0],self.coords[1]+35)
		self.screen.blit(frame, frameRect)
		self.screen.blit(text, textRect)