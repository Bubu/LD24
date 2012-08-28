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

INTRO = True

# mouse buttons
LEFT = 1
MIDDLE = 2
RIGHT = 3

# Fonts
FONT_GARAMOND = 'EBGaramond08-Regular.ttf'
#MUSIC = ['wolfram.ambient1.mid','wolfram.guitar1.mid','wolfram.rampb1.mid']
MUSIC = ['viking.mp3']
SOUNDS = ['react.wav', 'new_element.wav']

appdir = os.path.dirname(sys.argv[0])
PATH = os.path.join(appdir, "res") + os.sep

ELEMENT_RADIUS = 27
VERT_OFFSET = 40

# Text lines
T_logo = 'Human Evolution'
T_intro = ['Once upon a time on our blue planet...',
 'Actually it wasn\'t even blue back then.',
 'More  like a bubbling red-hot mass.',
 'There was only lava, and carbon dioxyde...',
 'well and some other elements maybe',
 'Then something happened...']
 
T_tutorial = ['Combine multiple elements to form new ones.',
 'Can you create life? Sentient species? And then?']
 
ElementData = {
				'chlorophyll':('Chlorophyll',(0,0),0),
				'co':('CO',(0,0),0),
				'people':('People',(0,0),0),
				'h2':('H2',(0,0),0),
				'h2so4':('H2SO4',(0,0),0),
				'cynobacterium':('Cynobacterium',(0,0),0),
				'computer':('Computer',(0,0),0),
				'human':('Human',(0,0),0),
				'tools':('Tools',(0,0),0),
				'firearm':('Firearm',(0,0),0),
				'co2':('CO2',(0,0),1),
				'dna':('DNA',(0,0),0),
				'network':('Network',(0,0),0),
				'sun':('Sun',(0,0),1),
				'prokaryote':('Prokaryote',(0,0),0),
				'eukaryote':('Eukaryote',(0,0),0),
				'sand':('Sand',(0,0),0),
				'lava':('Lava',(0,0),1),
				'sugar':('Sugar',(0,0),0),
				'brimstone':('Brimstone',(0,0),0),
				'wood':('Wood',(0,0),0),
				'lipids':('Lipids',(0,0),0),
				'internet':('Internet',(0,0),0),
				'sulfur':('Sulfur',(0,0),0),
				'o2':('O2',(0,0),0),
				'charcoal':('Charcoal',(0,0),0),
				'diamond':('Diamond',(0,0),0),
				'explosion':('Explosion',(0,0),0),
				'fire':('Fire',(0,0),0),
				'rna':('Rna',(0,0),0),
				'water':('Water',(0,0),0),
				'glass':('Glass',(0,0),0),
				'so3':('SO3',(0,0),0),
				'so2':('SO2',(0,0),0),
				'lighting':('Lighting',(0,0),0),
				'salpetre':('Salpetre',(0,0),0),
				'carbon':('Carbon',(0,0),0),
				'gunpowder':('Gunpowder',(0,0),0),
				'steel':('Steel',(0,0),0),
				'stone':('Stone',(0,0),0),
				'bible':('Bible',(0,0),0),
				'cloth':('Cloth',(0,0),0),
				'proteins':('Proteins',(0,0),0),
				'h2o':('H2O',(0,0),0),
				'iron':('Iron',(0,0),1),
				'social':('Social',(0,0),0),
				'steam':('Steam',(0,0),1),
				'rust':('Rust',(0,0),0),
				'magnetic field':('mag. field',(0,0),0),
				 }
				 
Reactions = {frozenset(Counter(['water','sun']).items()):('steam',),
			 frozenset(Counter(['water','co2','sun']).items()):('o2','sugar'),
			 frozenset(Counter(['iron','lava']).items()):('magnetic field',),			 
			 frozenset(Counter(['magnetic field','steam']).items()):('water',),
			}

PositionMap = {1: [(0,0)], 2: [(-40,0),(40,0)],3:[(-40,-40),(40,-40),(0,40)],4:[(-40,-40),(40,-40),(-40,40),(40,40)]}