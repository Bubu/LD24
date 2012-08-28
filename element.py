import pygame, pygame.gfxdraw, TextProvider, copy
from pygame.locals import *
from constants import *

#UUUGLY global data structure
activeDict = {}

def initializeActive():
	for e in ElementLabels.keys():
		activeDict[e] = True
	activeDict['steam'] = False
	activeDict['rna'] = False

def activate(e):
	activeDict[e] = True

def isActive(e):
	return activeDict[e]
	
class Element(pygame.sprite.Sprite):
	def __init__(self, type,game):
		super().__init__()
		self.type = type
		self.label = ElementLabels[self.type]
		self.game = game
		self.active = True
		self.radius = ELEMENT_RADIUS
	
	def draw(self, pos):
		self.coords = (35 + pos*65,51)
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
		self.game.screen.blit(frame, frameRect)
		self.game.screen.blit(text, textRect)
		
	def handleClick(self):
		if self in self.game.reactants:
			self.game.reactants.remove(self)
			self.game.sprites.remove(self)
			self.game.react()
			self.game.pickup = self
		else:
			self.game.pickup = copy.copy(self)
			
	def isActive(self):
		return activeDict[self.type]