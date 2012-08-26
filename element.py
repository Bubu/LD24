import pygame.sprite
from math import sqrt

class element(pygame.sprite.Sprite):
	def __init__(self, type):
		super().__init__()
		self.type = type