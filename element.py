import pygame, pygame.gfxdraw, TextProvider
from pygame.locals import *
from math import sqrt
from constants import *

class Element(pygame.sprite.Sprite):
	def __init__(self, screen, type):
		super().__init__()
		self.type = type
		self.label = ElementLabels[self.type]
		self.screen = screen
		self.active = True
	
	def draw(self, pos):
		#pygame.gfxdraw.aacircle(self.screen, 30, 30, 25, WHITE)
		frame = pygame.image.load(PATH + 'empty.png')
		try:
			ele = pygame.image.load(PATH + self.type + '.png')
		except:
			ele = pygame.image.load(PATH + 'noimg.png')
		eleRect = ele.get_rect()
		eleRect.center = frame.get_rect().center
		frame.blit(ele,eleRect)
		frameRect = frame.get_rect()
		frameRect.center = (35 + pos*65,35)
		text = TextProvider.captionText.render(self.label, True, BLACK)
		textRect = text.get_rect()
		textRect.center = (35 + pos*65, 70)
		self.screen.blit(frame, frameRect)
		self.screen.blit(text, textRect)