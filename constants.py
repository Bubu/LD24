import os,sys, collections
from collections import Counter
# colors
BLACK = (0, 0, 0)
BG_COLOR = (196, 195, 192)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
DGRAY = (99, 98, 96)

INTRO = False

# mouse buttons
LEFT = 1
MIDDLE = 2
RIGHT = 3

# Fonts
FONT_GARAMOND = 'EBGaramond08-Regular.ttf'

appdir = os.path.dirname(sys.argv[0])
PATH = os.path.join(appdir, "res") + os.sep

ELEMENT_RADIUS = 27

# Text lines
T_logo = 'Human Evolution'
T_intro = ['Once upon a time on our blue planet...',
 'Actually it wasn\'t even blue back then.',
 'More  like a bubbling red-hot mass.',
 'There was only lava, and carbon dioxyde...',
 'well and some other elements maybe',
 'Then something happened...']
 
T_tutorial = ['(Combine multiple elements to form new ones.)',
 'Can you create life? Sentient species? And then?']
 
ElementLabels = collections.OrderedDict([('co2', 'CO2'),
				 ('steam', 'H2O (gas.)'),
				 ('sun', 'Sun'),
				 ('lava', 'Lava'),
				 ('sand', 'Sand'),
				 ('bolt', 'Electricity'),
				 ('dna', 'DNA'),
				 ('rna', 'RNA'),
				 ('water', 'Water'),
				 ('stone', 'Stone'),
				 ('photosynthesis', 'Photosynth.'),
				 ('sugar', 'Sugar'),
				 ('o2', 'Oxygen'),
				 ])
				 
Reactions = {frozenset(Counter(['water','sun']).items()):('steam',),
			 frozenset(Counter(['water','co2','sun']).items()):('o2','sugar'),
			}

PositionMap = {1: [(0,0)], 2: [(-40,0),(40,0)],3:[(-40,-40),(40,-40),(0,40)],4:[(-40,-40),(40,-40),(-40,40),(40,40)]}