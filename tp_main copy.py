import pygame
import math
import sys
from pygame.locals import *
from tp_fruits import *
from tp_sword import *
from Sample import *
from tp_startscreen import *
import random
import Leap, sys, thread, time
sys.path.insert(0, "../lib/x86")
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture
import pygame
import pygame.display
import time

#created by Lukas Peraza
#for 15-112 F15 Pygame Optional Lecture, 11/11/15

# WORKS CITED: Got the structure of this from the link to framework from 112 schedule page (from Lukas Peraza's framework): 
# https://qwewy.gitbooks.io/pygame-module-manual/

#this file is the main file that compiles all the functionalities of the other files

pygame.init()

class PygameGame(object):

    def init(self):
        self.time = 0
        self.score = 0
        self.gameOver = False
        self.fruitList= []
        self.all_sprites = pygame.sprite.Group()
        controller = Leap.Controller()
        listener = SampleListener() 
        self.y = 600
        self.combo = []
        self.x = random.randint(0,720)
        self.font = None
        self.text = None
        self.scoreboard = None
        self.textCircle = None
        self.scoreCircle = None
        self.fruitTime = 0
        self.time = 0
        self.lives = 3
        self.livesBoard = None
        self.livesBoardCircle = None
        self.mode = 'start'
        self.directions = None
        self.directionsCircle = None
        self.title = pygame.image.load("fruitninja_title.jpg")
        self.count = 1
        self.number = random.randint(1,6) 
        
        pass

    def timerFired(self):
        if self.mode == 'timed':
            self.timedTimerFired()
        elif self.mode == 'infinite':
            self.infiniteTimerFired()
        elif self.mode == 'training':
            self.trainingTimerFired()
        elif self.mode == 'start':
            self.startTimerFired()
        elif self.mode == 'end':
            self.endTimerFired()
        
        
    def redrawAll(self, screen):
        if self.mode == 'timed':
            self.timedReDrawAll(screen)
        elif self.mode == 'infinite':
            self.infiniteReDrawAll(screen)
        elif self.mode == 'training':
            self.trainingReDrawAll(screen)
        elif self.mode == 'start':
            self.startRedrawAll(screen)
        elif self.mode == 'end':
            self.endRedrawAll(screen)
        
    def playGame(self, screen, x, y):
        if self.mode == 'timed':
            self.timedGame(screen, x, y)
        elif self.mode == 'infinite':
            self.infiniteGame(screen, x, y)
        elif self.mode == 'training':
            self.trainingGame(screen, x, y)
        elif self.mode == 'start':
            self.startPlayGame(screen, x, y)
        elif self.mode == 'end':
            self.endGame(screen, x, y)

#############
#start screen
#############

    def startRedrawAll(self, screen):
        pink = (255,182,193)
        screen.fill(pink)
        title = pygame.image.load("fruitninja_title.jpg")
        screen.blit(title, (self.width//2 - 250, self.height//2 - 275))
        timedModeIcon = TimedMode()
        infiniteModeIcon = InfiniteMode()
        trainingModeIcon = TrainingMode()
        timedModeIcon.draw(screen)
        infiniteModeIcon.draw(screen)
        trainingModeIcon.draw(screen)
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.instruction = self.font.render("Select Your Mode: Timed, Infinite, Training", True, (255,0,0), (255,255,0))
        self.instructionCircle = self.instruction.get_rect()
        self.instructionCircle.center = (400,320)
        screen.blit(self.instruction, self.instructionCircle)
        self.font2 = pygame.font.Font('freesansbold.ttf', 20)
        self.directions = self.font2.render("Directions: Move your hand up and down and side to side to control the sword.", True, (0,0,0), (255,255,255))
        self.directionsCircle = self.directions.get_rect()
        self.directionsCircle.center = (400,550)
        screen.blit(self.directions, self.directionsCircle)
        
    def startTimerFired(self):
        pass
    
    def startPlayGame(self, screen, x, y):
        sword = Sword(abs(int(x)*10), abs(int(y)))
        timedModeIcon = TimedMode()
        infiniteModeIcon = InfiniteMode()
        trainingModeIcon = TrainingMode()
        if timedModeIcon.cut(abs(int(x)*10), int(y), timedModeIcon.x):
            self.mode = "timed"
            timedModeIcon.chosen = True
        elif infiniteModeIcon.cut(abs(int(x)*10), int(y), infiniteModeIcon.x):
            self.mode = "infinite"
            infiniteModeIcon.chosen = True
        elif trainingModeIcon.cut(abs(int(x)*10), int(y), trainingModeIcon.x):
            self.mode = "training"
            trainingModeIcon.chosen = True
    
    #############
    #timed mode
    #############
    
    def timedReDrawAll(self, screen):
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.text = self.font.render(str(self.time//100), True, (255,0,0), (255,255,0))
        self.textCircle = self.text.get_rect()
        self.textCircle.center = (40, 40)
        self.scoreboard = self.font.render("score: " + str(self.score), True, (0,0,0), (255,255,0)) 
        self.scoreboardCircle = self.scoreboard.get_rect()
        self.scoreboardCircle.center = (650,40)
        self.directions = self.font.render("Timed Mode: You have 30 seconds!", True, (255,0,0), (255,255,0))
        self.speed = random.randint(5,10)
        self.directionsCircle = self.directions.get_rect()
        self.directionsCircle.center = (400,300)
        screen.blit(self.bg, (0,0))
        screen.blit(self.directions, self.directionsCircle)
    
    def timedTimerFired(self):
        if (self.time)//100 >= 30: self.gameOver = True
        self.fruitTime += 1 #remember to do it every something or so seconds
        self.time += 1
        #randomly decides how many fruits to throw in the air
        if self.fruitTime % 100 == 0:
            self.combo = []
            for fruit in range(self.number):
                fn = random.randint(1,28) #to decide what fruit
                randomfruit = None
                if fn == 1 or fn == 2 or fn == 3:
                    randomfruit = Apples()
                elif fn == 4 or fn == 5 or fn == 6:
                    randomfruit = Bananas()
                elif fn == 7 or fn == 8 or fn == 9:
                    randomfruit = Watermelon()
                elif fn == 10 or fn == 11 or fn == 12:
                    randomfruit = Coconut()
                elif fn == 13 or fn == 14 or fn == 15: 
                    randomfruit = Mango()
                elif fn == 16 or fn == 17 or fn == 18: 
                    randomfruit = Strawberry()
                elif fn == 19 or fn == 20 or fn == 21: 
                    randomfruit = Pineapple()
                elif fn == 22 or fn == 23 or fn == 24: 
                    randomfruit = Pear()
                elif fn == 25 or fn == 26: #for differing probabilities
                    randomfruit = Bomb()
                elif fn == 27: 
                    randomfruit = SpecialFruit()
                self.combo.append(randomfruit)
                self.fruitList.append(randomfruit)
        
    def timedGame(self, screen, x, y):
        sword = Sword(abs(int(x)*10), abs(int(y)))
        if (self.time)//100 >= 30: self.gameOver = True
        if self.lives <= 0: self.gameOver = True
        for fruit in self.fruitList: 
            if fruit != None: 
                fruit.draw(screen) 
                fruit.update(self.time, fruit.x, fruit.y, fruit.speed)
                if fruit.y <= random.randint(100,200):
                    fruit.command = False
                if fruit.cut(abs(int(x)*10), abs(int(y)), fruit.x, fruit.y) == True:
                    if isinstance(fruit, Bomb): 
                        pass
                    else: 
                        if fruit in self.combo:
                            self.combo.remove(fruit)
                        self.score += 1
                        fruit.sliced = True
                        fruit.command = False
                        pygame.mixer.music.load('slicesound.mp3')
                        pygame.mixer.music.play()
                        if (len(self.combo)) == 0:
                            self.score += 2
                            pygame.mixer.music.load('combo_sound.mp3')
                            pygame.mixer.music.play()
                if (fruit.y + 80) < 0 or fruit.y > 600:
                    self.fruitList.remove(fruit)
                elif (fruit.x + 80) < 0 or fruit.x > 800: 
                    self.fruitList.remove(fruit)
                if isinstance(fruit, Bomb):
                    if fruit.cut(abs(int(x)*10), abs(int(y)), fruit.x, fruit.y) == True:
                        pygame.mixer.music.load('bomb.mp3')
                        pygame.mixer.music.play()
                        fruit.explosion(screen)
                        pygame.time.delay(100)
                        screen.fill((0,0,0))
                        fruit.sliced = True
                        if fruit.sliced == True: 
                            self.gameOver = True
                        if self.lives == 0:
                            black = [0,0,0]
                            screen.fill(black)
                elif isinstance(fruit, SpecialFruit):
                    pygame.mixer.music.load('fruitninja_sparklesound.mp3')
                    pygame.mixer.music.play()
                    if fruit.cut(sword.y, sword.x, fruit.x, fruit.y) == True:
                        fruit.sliced = True
                        for fruit in range(20):
                            list = [Apples(), Bananas(), Pineapple(), Strawberry(), Coconut(), Mango(), Pear(), Watermelon()]
                            self.fruitList.append(random.choice(list))
        screen.blit(self.text, self.textCircle)
        screen.blit(self.scoreboard, self.scoreboardCircle)
    
    #############
    #infinite mode
    #############
    
    def infiniteReDrawAll(self, screen):
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.text = self.font.render(str(self.time//100), True, (255,0,0), (255,255,0))
        self.textCircle = self.text.get_rect()
        self.textCircle.center = (40, 40)
        self.scoreboard = self.font.render("score: " + str(self.score), True, (0,0,0), (255,255,0)) 
        self.scoreboardCircle = self.scoreboard.get_rect()
        self.scoreboardCircle.center = (650,40)
        self.directions = self.font.render("Infinite Mode", True, (255,0,0), (255,255,0))
        self.directionsCircle = self.directions.get_rect()
        self.directionsCircle.center = (400,300)
        screen.blit(self.bg, (0,0))
        screen.blit(self.directions, self.directionsCircle)
        pass
    
    def infiniteTimerFired(self):
        self.fruitTime += 1 #remember to do it every something or so seconds
        self.time += 1
        number = random.randint(1,6) 
        #randomly decides how many fruits to throw in the air
        self.command = []
        if self.fruitTime % 100 == 0:
            for fruit in range(number):
                fn = random.randint(1,28) #to decide what fruit
                randomfruit = None
                if fn == 1 or fn == 2 or fn == 3:
                    randomfruit = Apples()
                elif fn == 4 or fn == 5 or fn == 6:
                    randomfruit = Bananas()
                elif fn == 7 or fn == 8 or fn == 9:
                    randomfruit = Watermelon()
                elif fn == 10 or fn == 11 or fn == 12:
                    randomfruit = Coconut()
                elif fn == 13 or fn == 14 or fn == 15: 
                    randomfruit = Mango()
                elif fn == 16 or fn == 17 or fn == 18: 
                    randomfruit = Strawberry()
                elif fn == 19 or fn == 20 or fn == 21: 
                    randomfruit = Pineapple()
                elif fn == 22 or fn == 23 or fn == 24: 
                    randomfruit = Pear()
                elif fn == 25 or fn == 26:
                    randomfruit = Bomb()
                elif fn == 7: 
                    randomfruit = SpecialFruit()
                self.command.append(True)
                self.fruitList.append(randomfruit)
        
    def infiniteGame(self, screen, x, y):
        if self.lives <= 0: self.gameOver = True
        sword = Sword(abs(int(x)*10), abs(int(y)))
        for fruit in self.fruitList: 
            if fruit != None: 
                fruit.draw(screen) 
                fruit.update(self.time, fruit.x, fruit.y, fruit.speed)
                if fruit.y <= random.randint(100,200):
                    fruit.command = False
                if fruit.cut(abs(int(x)*10), abs(int(y)), fruit.x, fruit.y) == True:
                    if isinstance(fruit, Bomb): 
                        pass
                    else: 
                        if fruit in self.combo:
                            self.count += 1 
                            self.combo.remove(fruit)
                        if (len(self.combo)) == 0:
                            pygame.mixer.music.load('combo_sound.mp3')
                            pygame.mixer.music.play()
                            self.score += 2
                        self.score += 1
                        fruit.sliced = True
                        fruit.command = False
                        pygame.mixer.music.load('slicesound.mp3')
                        pygame.mixer.music.play()
                if (fruit.y + 80) < 0 or fruit.y > 600:
                    self.fruitList.remove(fruit)
                elif (fruit.x + 80) < 0 or fruit.x > 800: 
                    self.fruitList.remove(fruit)
                if isinstance(fruit, Bomb):
                    if fruit.cut(abs(int(x)*10), abs(int(y)), fruit.x, fruit.y) == True:
                        pygame.mixer.music.load('bomb.mp3')
                        pygame.mixer.music.play()
                        fruit.sliced = True
                        fruit.explosion(screen)
                        pygame.time.delay(2)
                        screen.fill((0,0,0))
                        if fruit.sliced == True: 
                            self.gameOver=True
                elif isinstance(fruit, SpecialFruit):
                    pygame.mixer.music.load('fruitninja_sparklesound.mp3')
                    pygame.mixer.music.play()
                    if fruit.cut(sword.y, sword.x, fruit.x, fruit.y) == True:
                        for fruit in range(20):
                            list = [Apples(), Bananas(), Pineapple(), Strawberry(), Coconut(), Mango(), Pear(), Watermelon()]
                            self.fruitList.append(random.choice(list))
        screen.blit(self.text, self.textCircle)
        screen.blit(self.scoreboard, self.scoreboardCircle)
        
    #############
    #training mode
    #############
    
    def trainingReDrawAll(self, screen):
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.text = self.font.render(str(self.time//100), True, (255,0,0), (255,255,0))
        self.textCircle = self.text.get_rect()
        self.textCircle.center = (40, 40)
        self.scoreboard = self.font.render("score: " + str(self.score), True, (0,0,0), (255,255,0)) 
        self.scoreboardCircle = self.scoreboard.get_rect()
        self.scoreboardCircle.center = (650,40)
        self.livesBoard = self.font.render('Lives: ' + str(self.lives), True, (0,0,0), (255,255,0))
        self.livesBoardCircle= self.livesBoard.get_rect()
        self.livesBoardCircle.center = (650, 100)
        self.directions = self.font.render("Training Mode: Slice the fruit with your hand!", True, (255,0,0), (255,255,0))
        self.directionsCircle = self.directions.get_rect()
        self.directionsCircle.center = (400,300)
        screen.blit(self.bg, (0,0))
        screen.blit(self.directions, self.directionsCircle)
        pass
    
    def trainingTimerFired(self):
        self.fruitTime += 0.5 #remember to do it every something or so seconds
        self.time += 1
        self.number = random.randint(1,6) 
        #randomly decides how many fruits to throw in the air
        self.command = []
        if self.fruitTime % 100 == 0:
            for fruit in range(self.number):
                fn = random.randint(1,25) #to decide what fruit
                randomfruit = None
                if fn == 1 or fn == 2 or fn == 3:
                    randomfruit = Apples()
                elif fn == 4 or fn == 5 or fn == 6:
                    randomfruit = Bananas()
                elif fn == 7 or fn == 8 or fn == 9:
                    randomfruit = Watermelon()
                elif fn == 10 or fn == 11 or fn == 12:
                    randomfruit = Coconut()
                elif fn == 13 or fn == 14 or fn == 15: 
                    randomfruit = Mango()
                elif fn == 16 or fn == 17 or fn == 18: 
                    randomfruit = Strawberry()
                elif fn == 19 or fn == 20 or fn == 21: 
                    randomfruit = Pineapple()
                elif fn == 22 or fn == 23 or fn == 24: 
                    randomfruit = Pear()
                self.fruitList.append(randomfruit)
        
    def trainingGame(self, screen, x, y):
        sword = Sword(abs(int(x)*10), abs(int(y)))
        backbutton = back()
        backbutton.draw(screen)
        if backbutton.cut(abs(int(x)*10), int(y), backbutton.x) == True:
            self.mode = 'start'
        for fruit in self.fruitList: 
            if fruit != None: 
                fruit.draw(screen) 
                fruit.update(self.time, fruit.x, fruit.y, fruit.speed)
                fruit.speed = random.randint(5,10)
                if fruit.y <= random.randint(100,200):
                    fruit.command = False
                if fruit.cut(abs(int(x)*10), abs(int(y)), fruit.x, fruit.y) == True:
                    self.score += 1
                    fruit.sliced = True
                    fruit.command = False
                    pygame.mixer.music.load('slicesound.mp3')
                    pygame.mixer.music.play()
                if (fruit.y + 80) < 0 or fruit.y > 600:
                    self.fruitList.remove(fruit)
                elif (fruit.x + 80) < 0 or fruit.x > 800: 
                    self.fruitList.remove(fruit)
        screen.blit(self.text, self.textCircle)
        screen.blit(self.scoreboard, self.scoreboardCircle)

#############
#end screen
#############

    def endRedrawAll(self, screen):
        black = (0,0,0)
        screen.fill(black)
        endScreen = pygame.image.load('fruitninja_gameover.jpg')
        screen.blit(endScreen, (self.width//2 - 250, self.height//2 - 200))
        screen.blit(self.scoreboard, (325,500))
        playagain = playAgain()
        playagain.draw(screen)
        
    def endTimerFired(self):
        pass
        
    def endGame(self, screen, x, y):
        playagain = playAgain()
        sword = Sword(abs(int(x)*10), abs(int(y)))
        if playagain.cut(abs(int(x)*10), int(y), playagain.x) == True:
       
            self.gameOver = False
            self.mode = 'start'


#############

    def __init__(self, width=800, height=600, fps=50, title="Fruit Ninja"):
        self.pictureList = []
        self.width = width
        self.height = height
        self.fps = fps
        self.title = title
        self.bg = pygame.image.load('fruitninja_bg.jpg')
        self.score = 0
        self.gameOver = False
        self.training = False
        self.timed = True
        self.infinite = False
        self.end = False
        self.start = False
        pygame.init()

    def run(self):
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((self.width, self.height))
        # set the title of the window
        pygame.display.set_caption(self.title)
        listener = SampleListener()
        # stores all the keys currently being held down
        self._keys = dict()
        self._keys = dict()
        controller = Leap.Controller()
        # call game-specific initialization
        self.init()
        
        playing = True
        # Initialize the mixer
        pygame.mixer.init()
        pygame.mixer.init()
        
        while playing:
            time = clock.tick()
            self.timerFired()
            frame = controller.frame()
            self.redrawAll(screen)
            for event in pygame.event.get():
                frame = controller.frame()
                (x,y) = (0,0)
            for hand in frame.hands:
                handType = "Left hand" if hand.is_left else "Right hand"
                x = (hand.palm_position)[0]
                y = (hand.palm_position)[1]
            sword = Sword(abs(int(x)*10), abs(int(y)))
            sword = Sword(abs(int(x)*10), abs(int(y)))
            sword.draw(screen, (int(x)), abs(int(y)))
            self.playGame(screen, x, y)
            if self.gameOver == True:
                self.mode = 'end'
                self.score = 0
                self.time = 0
            if self.mode == 'start': 
                self.gameOver = False
                self.score = 0
                self.time = 0
                self.lives = 3
                self.fruitList = []
            pygame.display.flip()
        try:
            sys.stdin.readline() 
        except KeyboardInterrupt:
            pass
        finally:
            # Remove the sample listener when done
            controller.remove_listener(listener)


        pygame.quit()


def main():
    game = PygameGame()
    game.run()

if __name__ == '__main__':
    main()