import pygame
from pygame.locals import *
from constants import *

def init():
	global logoText, introText, descriptionText, captionText, pageText
	logoText = pygame.font.Font(PATH + FONT_GARAMOND, 60)
	introText = pygame.font.Font(PATH + FONT_GARAMOND, 30)
	descriptionText = pygame.font.Font(PATH + FONT_GARAMOND, 22)
	captionText = pygame.font.Font(PATH + FONT_GARAMOND, 14)
	pageText = pygame.font.SysFont('Arial', 16)
	pageText.set_bold(True)