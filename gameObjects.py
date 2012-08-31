import gameSprites
from constants import *

class TypeBar:
    def __init__(self):
        self.types = []
        self.pages = [Page(1,True)]
        self.activePage = self.pages[0]
        
        f = open(PATH + 'elements.txt', mode = 'r')
        page = 1
        for line in f:
            if line == '':
                page += 1
                self.pages.append(Page(page))
            else:
                ls = line.split(',')
                self.types.append(Type(ls[0],ls[1], page, ls[0] in StartElements))

    def activateType(self,type):
        pass
    
    def renderTypes(self,screen):
        pass
    
    def renderPages(self,screen):
        for p in self.pages:
            p.draw(screen)
    
class Type:
    def __init__(self,type,caption,page,unlocked):
        self.type = type
        self.page = page
        self.unlocked = unlocked
        self.sprite = gameSprites.ElementSprite(type, caption)

class Page:
    def __init__(self, number, activated = False):
        self.sprite = gameSprites.PageSprite(number)
        self.number = number
        self.activated = activated
        self.types = []