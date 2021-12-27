import pygame
import sys
from pygame.locals import *
from tp_fruits import *
from tp_main import *
from tp_sword import *
import random
from Sample import *
pygame.init()

#this file defines the properties of the sword

class Sword(pygame.sprite.Sprite):
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen, x, y):
        swordImg = pygame.image.load('fruitninja_sword.png')
        screen.blit(pygame.transform.scale(swordImg, (80, 80)), (self.x,self.y))