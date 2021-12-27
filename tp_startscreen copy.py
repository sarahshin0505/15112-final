from tp_sword import *
import pygame
import sys
from pygame.locals import *
from tp_fruits import *
from tp_sword import *
import random
pygame.init()

#defines the icons for the start screen

class StartScreen(pygame.sprite.Sprite):
    def __init__(self):        
        pygame.sprite.Sprite.__init__(self)
        self.x = x
    
    def cut(self, swordX, swordY, x):
        if (abs((swordX) - (x + 80)) <= 80) and (abs((swordY) - (400 + 80)) <= 80):
            return True
        return False
 
class TimedMode(StartScreen):
    
    def __init__(self):        
        pygame.sprite.Sprite.__init__(self)
        self.x = 200
        self.chosen = False

    def draw(self, screen): 
        timed = pygame.image.load('fruitninja_timed.png')
        screen.blit(pygame.transform.scale(timed, (80,80)), (200,400))
        
class InfiniteMode(StartScreen):
    
    def __init__(self):        
        pygame.sprite.Sprite.__init__(self)
        self.x = 350
        self.chosen = False
    
    def draw(self, screen):
        infinite = pygame.image.load('fruitninja_infinite.jpeg')
        screen.blit(pygame.transform.scale(infinite, (80,80)), (350,400))
            
    
class TrainingMode(StartScreen):
    
    def __init__(self):        
        pygame.sprite.Sprite.__init__(self)
        self.x = 500
        self.chosen = False
    
    def draw(self, screen):
        training = pygame.image.load('fruitninja_training.jpg')
        screen.blit(pygame.transform.scale(training, (80,80)), (500,400))
            
class playAgain(StartScreen):
    
    def __init__(self):        
        pygame.sprite.Sprite.__init__(self)
        self.x = 300
        self.chosen = False
        
    def cut(self, swordX, swordY, x):
        if (abs((swordX) - (x + 200)) <= 200) and (abs((swordY) - (300 + 100)) <= 100):
            return True
        return False
    
    def draw(self, screen):
        training = pygame.image.load('fruitninja_playagain.png')
        screen.blit(pygame.transform.scale(training, (200,100)), (300,300))
        
class sparkle(StartScreen):
    
    def __init__(self):        
        pygame.sprite.Sprite.__init__(self)
        self.x = 500
        self.chosen = False
    
    def draw(self, screen, xpos, ypos):
        sparkle = pygame.image.load('fruitninja_sparkle.jpg')
        screen.blit(pygame.transform.scale(sparkle, (50,50)), (xpos, ypos))
        
class combo(StartScreen):
    def __init__(self):        
        pygame.sprite.Sprite.__init__(self)
        self.x = 500
        self.chosen = False
    
    
    def draw(self, screen, xpos, ypos):
        pygame.time.delay(100)
        sparkle = pygame.image.load('fruitninja_sparkle.jpg')
        screen.blit(pygame.transform.scale(sparkle, (50,50)), (xpos, ypos))
        
class back(StartScreen):
    
    def __init__(self):        
        pygame.sprite.Sprite.__init__(self)
        self.x = 600
        self.chosen = False
        
    def cut(self, swordX, swordY, x):
        if (abs((swordX) - (x + 80)) <= 80) and (abs((swordY) - (230)) <= 80):
            return True
        return False
    
    def draw(self, screen):
        training = pygame.image.load('fruitninja_back.png')
        screen.blit(pygame.transform.scale(training, (80,80)), (600,150))
        if self.chosen == True: 
            pass