from tp_sword import *
import pygame
import sys
from pygame.locals import *
from tp_fruits import *
from tp_sword import *
import random
pygame.init()

#this file defines and lists all the properties of the fruits

class Fruits(pygame.sprite.Sprite):
    def __init__(self, width, height, whole, img, speed, y):
        self.size = size
        self.whole = True
        self.width = width
        self.height = height
        self.speed = 10
        self.y = 600
        self.x = random.randint(0,720)
        self.command = True
    
    def cut(self, swordX, swordY, fruitX, fruitY):
        if (abs((swordX) - (fruitX + 80)) <= 80) and (abs((swordY) - (fruitY + 80)) <= 80):
            return True
        return False
            

class Apples(Fruits):
    
    def __init__(self):        
        self.y = 600
        self.x = random.randint(0,360)
        self.speed = random.randint(5,10)
        self.endX = random.randint(360,720)
        self.endY = random.randint(200,500)
        pygame.sprite.Sprite.__init__(self)
        self.xdirect = random.choice([1,-1])
        self.xOpposite = (-1)*self.xdirect
        self.picture = pygame.image.load('fruitninja_apple.png')
        self.command = True
        self.sliced = False
        self.angle = 45
        
    def draw(self, screen):
        if self.sliced == False:
            picture = pygame.image.load('fruitninja_apple.png')
            screen.blit(pygame.transform.scale(picture, (80, 80)), (self.x,self.y))
        elif self.sliced == True: 
            slicedpicture1 = pygame.image.load('fruitninja_leftapple.png')
            slicedpicture1rotate = pygame.transform.rotate(slicedpicture1, self.angle)
            screen.blit(pygame.transform.scale(slicedpicture1rotate,(80,80)), (self.x, self.y))
            slicedpicture2 = pygame.image.load('fruitninja_rightapple.png')
            slicedpicture2scale = pygame.transform.scale(slicedpicture2, (80,80))
            slicedpicture2rotate =  pygame.transform.rotate(slicedpicture2scale, -self.angle)
            screen.blit(pygame.transform.scale(slicedpicture2rotate, (80,80)), (self.x + 80, self.y))
        
    def update(self, time, x, y, speed):
        a = random.randint(1,3)
        b = random.randint(1,3)
        self.x += 4*self.xdirect
        self.angle += 5
        if self.command == True:
            y -= speed
        elif self.command == False:
            self.y += speed
        if self.x == self.endX:
            self.y = 610
            
class Bananas(Fruits):
    def __init__(self):
        self.y = 600
        self.x = random.randint(0,360)
        self.speed = random.randint(5,10)
        self.endX = random.randint(360,720)
        self.endY = random.randint(200,500)
        pygame.sprite.Sprite.__init__(self)
        self.xdirect = random.choice([1,-1])
        self.xOpposite = (-1)*self.xdirect
        self.picture = pygame.image.load('fruitninja_banana.png')
        self.command = True
        self.sliced = False
        self.angle = 45
        
    def draw(self, screen):
        if self.sliced == False:
            picture = pygame.image.load('fruitninja_banana.png')
            screen.blit(pygame.transform.scale(picture, (80, 80)), (self.x,self.y))
        elif self.sliced == True: 
            slicedpicture1 = pygame.image.load('fruitninja_leftbanana.png')
            slicedpicture1rotate = pygame.transform.rotate(slicedpicture1, self.angle)
            screen.blit(pygame.transform.scale(slicedpicture1rotate, (80,80)), (self.x, self.y))
            slicedpicture2 = pygame.image.load('fruitninja_rightbanana.png')
            slicedpicture2rotate = pygame.transform.rotate(slicedpicture2, -self.angle)
            screen.blit(pygame.transform.scale(slicedpicture2, (80,80)), (self.x + 80, self.y))
        
    def update(self, time, x, y, speed):
        a = random.randint(1,3)
        b = random.randint(1,3)
        self.angle += 5
        self.x += 4*self.xdirect
        if self.command == True:
            self.y -= speed
        elif self.command == False:
            self.y += speed
        if self.x == self.endX:
            self.y = 610
            
class Watermelon(Fruits):
    def __init__(self):
        self.y = 600
        self.x = random.randint(0,360)
        self.speed = random.randint(5,10)
        self.endX = random.randint(360,720)
        self.endY = random.randint(200,500)
        pygame.sprite.Sprite.__init__(self)
        self.xdirect = random.choice([1,-1])
        self.xOpposite = (-1)*self.xdirect
        self.picture = pygame.image.load('fruitninja_watermelon.png')
        self.command = True
        self.sliced = False
        self.angle = 45
        
    def draw(self, screen):
        if self.sliced == False:
            picture = pygame.image.load('fruitninja_watermelon.png')
            screen.blit(pygame.transform.scale(picture, (80, 80)), (self.x,self.y))
        elif self.sliced == True: 
            slicedpicture1 = pygame.image.load('fruitninja_leftwatermelon.png')
            slicedpicture1rotate = pygame.transform.rotate(slicedpicture1, self.angle)
            screen.blit(pygame.transform.scale(slicedpicture1rotate, (80,80)), (self.x, self.y))
            slicedpicture2 = pygame.image.load('fruitninja_rightwatermelon.png')
            slicedpicture2rotate = pygame.transform.rotate(slicedpicture2, -self.angle)
            screen.blit(pygame.transform.scale(slicedpicture2rotate, (80,80)), (self.x + 80, self.y))
    
    def update(self, time, x, y, speed):
        a = random.randint(1,3)
        b = random.randint(1,3)
        self.angle += 5
        self.x += 4*self.xdirect
        if self.command == True:
            self.y -= speed
        elif self.command == False:
            self.y += speed
        if self.x == self.endX:
            self.y = 610

     
class Coconut(Fruits):
    def __init__(self):
        self.y = 600
        self.x = random.randint(0,360)
        self.speed = random.randint(5,10)
        self.endX = random.randint(360,720)
        self.endY = random.randint(200,500)
        pygame.sprite.Sprite.__init__(self)
        self.xdirect = random.choice([1,-1])
        self.xOpposite = (-1)*self.xdirect
        self.picture = pygame.image.load('fruitninja_coconut.png')
        self.command = True
        self.sliced = False
        self.angle = 45
        
    def draw(self, screen):
        if self.sliced == False:
            picture = pygame.image.load('fruitninja_coconut.png')
            screen.blit(pygame.transform.scale(picture, (80, 80)), (self.x,self.y))
        elif self.sliced == True: 
            slicedpicture1 = pygame.image.load('fruitninja_leftcoconut.png')
            slicedpicture1rotate = pygame.transform.rotate(slicedpicture1, self.angle)
            screen.blit(pygame.transform.scale(slicedpicture1rotate, (80,80)), (self.x, self.y))
            slicedpicture2 = pygame.image.load('fruitninja_rightcoconut.png')
            slicedpicture2rotate = pygame.transform.rotate(slicedpicture2, -self.angle)
            screen.blit(pygame.transform.scale(slicedpicture2rotate, (80,80)), (self.x + 80, self.y))
        
    def update(self, time, x, y, speed):
        a = random.randint(1,3)
        b = random.randint(1,3)
        self.angle += 5
        self.x += 4*self.xdirect
        if self.command == True:
            self.y -= speed
        elif self.command == False:
            self.y += speed
        if self.x == self.endX:
            self.y = 610
        
class Mango(Fruits):
    def __init__(self):
        self.y = 600
        self.x = random.randint(0,360)
        self.speed = random.randint(5,10)
        self.endX = random.randint(360,720)
        self.endY = random.randint(200,500)
        pygame.sprite.Sprite.__init__(self)
        self.xdirect = random.choice([1,-1])
        self.xOpposite = (-1)*self.xdirect
        self.picture = (pygame.image.load('fruitninja_mango.png'))
        self.command = True
        self.sliced = False
        self.angle = 45
        
    def draw(self, screen):
        if self.sliced == False:
            picture = pygame.image.load('fruitninja_mango.png')
            screen.blit(pygame.transform.scale(picture, (80, 80)), (self.x,self.y))
        elif self.sliced == True: 
            slicedpicture1 = pygame.image.load('fruitninja_leftmango.png')
            slicedpicture1rotate = pygame.transform.rotate(slicedpicture1, self.angle)
            screen.blit(pygame.transform.scale(slicedpicture1rotate, (80,80)), (self.x, self.y))
            slicedpicture2 = pygame.image.load('fruitninja_rightmango.png')
            slicedpicture2rotate = pygame.transform.rotate(slicedpicture2, -self.angle)
            screen.blit(pygame.transform.scale(slicedpicture2rotate, (80,80)), (self.x + 80, self.y))
        
    def update(self, time, x, y, speed):
        a = random.randint(1,3)
        b = random.randint(1,3)
        self.angle += 5
        self.x += 4*self.xdirect
        if self.command == True:
            self.y -= speed
        elif self.command == False:
            self.y += speed
        if self.x == self.endX:
            self.y = 610


class Strawberry(Fruits):
    def __init__(self):
        self.y = 600
        self.x = random.randint(0,360)
        self.speed = random.randint(5,10)
        self.endX = random.randint(360,720)
        self.endY = random.randint(200,500)
        pygame.sprite.Sprite.__init__(self)
        self.xdirect = random.choice([1,-1])
        self.xOpposite = (-1)*self.xdirect
        self.picture = (pygame.image.load('fruitninja_strawberry.png'))
        self.command = True
        self.sliced = False
        self.angle = 45
        
    def draw(self, screen):
        if self.sliced == False:
            picture = pygame.image.load('fruitninja_strawberry.png')
            screen.blit(pygame.transform.scale(picture, (80, 80)), (self.x,self.y))
        elif self.sliced == True: 
            slicedpicture1 = pygame.image.load('fruitninja_leftstrawberry.png')
            slicedpicture1rotate = pygame.transform.rotate(slicedpicture1, self.angle)
            screen.blit(pygame.transform.scale(slicedpicture1rotate, (80,80)), (self.x, self.y))
            slicedpicture2 = pygame.image.load('fruitninja_rightstrawberry.png')
            slicedpicture2rotate = pygame.transform.rotate(slicedpicture2, -self.angle)
            screen.blit(pygame.transform.scale(slicedpicture2rotate, (80,80)), (self.x + 80, self.y))
        
    def update(self, time, x, y, speed):
        a = random.randint(1,3)
        b = random.randint(1,3)
        self.angle += 5
        self.x += 4*self.xdirect
        if self.command == True:
            self.y -= speed
        elif self.command == False:
            self.y += speed
        if self.x == self.endX:
            self.y = 610
            
class Pineapple(Fruits):
    def __init__(self):
        self.y = 600
        self.x = random.randint(0,360)
        self.speed = random.randint(5,10)
        self.endX = random.randint(360,720)
        self.endY = random.randint(200,500)
        pygame.sprite.Sprite.__init__(self)
        self.xdirect = random.choice([1,-1])
        self.xOpposite = (-1)*self.xdirect
        self.picture = (pygame.image.load('fruitninja_pineapple.png'))
        self.command = True
        self.sliced = False
        self.angle = 45
        
    def draw(self, screen):
        if self.sliced == False:
            picture = pygame.image.load('fruitninja_pineapple.png')
            screen.blit(pygame.transform.scale(picture, (80, 80)), (self.x,self.y))
        elif self.sliced == True: 
            slicedpicture1 = pygame.image.load('fruitninja_leftpineapple.png')
            slicedpicture1rotate = pygame.transform.rotate(slicedpicture1, self.angle)
            screen.blit(pygame.transform.scale(slicedpicture1rotate, (80,80)), (self.x, self.y))
            slicedpicture2 = pygame.image.load('fruitninja_rightpineapple.png')
            slicedpicture2rotate = pygame.transform.rotate(slicedpicture2, -self.angle)
            screen.blit(pygame.transform.scale(slicedpicture2rotate, (80,80)), (self.x + 80, self.y))
        
    def update(self, time, x, y, speed):
        a = random.randint(1,3)
        b = random.randint(1,3)
        self.angle += 5
        self.x += 4*self.xdirect
        if self.command == True:
            self.y -= speed
        elif self.command == False:
            self.y += speed
        if self.x == self.endX:
            self.y = 610
            
class Pear(Fruits):
    def __init__(self):
        self.y = 600
        self.x = random.randint(0,360)
        self.speed = random.randint(5,10)
        self.endX = random.randint(360,720)
        self.endY = random.randint(200,500)
        pygame.sprite.Sprite.__init__(self)
        self.xdirect = random.choice([1,-1])
        self.xOpposite = (-1)*self.xdirect
        self.picture = (pygame.image.load('fruitninja_pear.png'))
        self.command = True
        self.sliced = False
        self.angle = 45
        
    def draw(self, screen):
        if self.sliced == False:
            picture = pygame.image.load('fruitninja_pear.png')
            screen.blit(pygame.transform.scale(picture, (80, 80)), (self.x,self.y))
        elif self.sliced == True: 
            slicedpicture1 = pygame.image.load('fruitninja_leftpear.png')
            slicedpicture1rotate = pygame.transform.rotate(slicedpicture1, self.angle)
            screen.blit(pygame.transform.scale(slicedpicture1rotate, (80,80)), (self.x, self.y))
            slicedpicture2 = pygame.image.load('fruitninja_rightpear.png')
            slicedpicture2rotate = pygame.transform.rotate(slicedpicture2, -self.angle)
            screen.blit(pygame.transform.scale(slicedpicture2rotate, (80,80)), (self.x + 80, self.y))
        
    def update(self, time, x, y, speed):
        a = random.randint(1,3)
        b = random.randint(1,3)
        self.angle += 5
        self.x += 4*self.xdirect
        if self.command == True:
            self.y -= speed
        elif self.command == False:
            self.y += speed
        if self.x == self.endX:
            self.y = 610

class Bomb(Fruits):
    
    def __init__(self):
        self.y = 600
        self.x = random.randint(0,360)
        self.speed = random.randint(5,10)
        self.endX = random.randint(360,720)
        self.endY = random.randint(200,500)
        pygame.sprite.Sprite.__init__(self)
        self.xdirect = random.choice([1,-1])
        self.xOpposite = (-1)*self.xdirect
        self.command = True
        self.sliced = True
        
    def draw(self, screen):
        picture = pygame.image.load('tp_bomb.png')
        screen.blit(pygame.transform.scale(picture, (80, 80)), (self.x,self.y))
        
    def update(self, time, x, y, speed):
        a = random.randint(1,3)
        b = random.randint(1,3)
        
        self.x += 4*self.xdirect
        if self.command == True:
            self.y -= speed
        elif self.command == False:
            self.y += speed
        if self.x == self.endX:
            self.y = 610
            
    def explosion(self, screen):    
        explosion = pygame.image.load('fruitninja_explosion.jpg')
        screen.blit(explosion, (0,0))
            
class SpecialFruit(Fruits):
    
    def __init__(self):
        self.y = 0
        self.x = random.randint(0,360)
        self.speed = random.randint(15,20)
        self.endX = random.randint(360,720)
        self.endY = random.randint(200,500)
        pygame.sprite.Sprite.__init__(self)
        self.xdirect = random.choice([1,-1])
        self.xOpposite = (-1)*self.xdirect
        self.command = True
        self.sliced = False
        self.angle = 45
        
    def draw(self, screen):
        if self.sliced == False:
            picture = pygame.image.load('fruitninja_specialfruit1.png')
            screen.blit(pygame.transform.scale(picture, (80, 80)), (self.x,self.y))
        elif self.sliced == True: 
            slicedpicture1 = pygame.image.load('fruitninja_rightspecialfruit1.png')
            slicedpicture1rotate = pygame.transform.rotate(slicedpicture1, self.angle)
            screen.blit(pygame.transform.scale(slicedpicture1rotate, (80,80)), (self.x, self.y))
            slicedpicture2 = pygame.image.load('fruitninja_leftspecialfruit1.png')
            slicedpicture2rotate = pygame.transform.rotate(slicedpicture2, -self.angle)
            screen.blit(pygame.transform.scale(slicedpicture2rotate, (80,80)), (self.x + 80, self.y))
        
    def update(self, time, x, y, speed):
        a = random.randint(1,3)
        b = random.randint(1,3)
        self.angle += 5
        self.x += 4*self.xdirect
        if self.command == True:
            self.y -= speed
        elif self.command == False:
            self.y += speed
        if self.x == self.endX:
            self.y = 610
            
            
    
