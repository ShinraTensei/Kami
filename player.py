import pygame
from constants import *
from SpriteSheet import SpriteSheet
from Vector import *

class Player(object):
    def __init__(self):
        frame_data = [Vector(0, 0, 40, 40), Vector(40, 0, 40, 40)]

        self.sprite_sheet = SpriteSheet("sprites/characters/player.png", frame_data)

        #self.framePosX = 0
        #self.framePosY = 0
        #self.frame = self.sprite_sheet.get_image(self.framePosX, self.framePosY, 40, 40)
        self.animationSpeed = 0.13
        self.timePassed = 0
        self.direction_horizontal = False # False Right, True Left
        
        self.posX = 32
        self.posY = 32
        self.walkSpeed = 250

        #self.sizeX, self.sizeY = self.frame.get_size()

        self.scale = 5
        self.alpha = 255
        #self.frame.set_alpha(self.alpha)


    def draw(self, screen, deltaTime):
        self.deltaTime = deltaTime

        #self.frame = self.sprite_sheet.get_image(self.framePosX, self.framePosY, 40, 40)
        #self.frame = pygame.transform.scale(self.frame, (self.sizeX*self.scale, self.sizeY*self.scale))
        #screen.blit(pygame.transform.flip(self.frame, self.direction_horizontal, False), (self.posX, self.posY))

        self.timePassed += deltaTime

    def idle_anim(self):
        self.framePosY = 0
        if(self.timePassed > self.animationSpeed):
            if(self.framePosX < 200):
                self.framePosX += 40
            else:
                self.framePosX = 0
            self.timePassed = 0
    
    def walk_anim(self):
        self.framePosY = 40
        if(self.direction_horizontal):
            if(self.timePassed > self.animationSpeed):
                if(self.framePosX < 200):
                    self.framePosX += 40
                else:
                    self.framePosX = 0
                self.timePassed = 0
        elif(not self.direction_horizontal): # False is left
            if(self.timePassed > self.animationSpeed):
                if(self.framePosX < 200):
                    self.framePosX += 40
                else:
                    self.framePosX = 0
                self.timePassed = 0

    def move_left(self, deltaTime):
        self.direction_horizontal = True
        self.walk_anim()
        self.posX -= self.walkSpeed * deltaTime
    def move_right(self, deltaTime):
        self.direction_horizontal = False
        self.walk_anim()
        self.posX += self.walkSpeed * deltaTime
