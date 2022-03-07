import pygame
from constants import *
from SpriteSheet import SpriteSheet
from Vector import *

class Player(object):
    def __init__(self):
        self.scale = 2

        frame_data_idle_horizontal = [Vector(0, 288, 48, 48),
                                      Vector(48, 288, 48, 48),
                                      Vector(96, 288, 48, 48)]

        frame_data_idle_vertical_up = [Vector(0, 336, 48, 48),
                                       Vector(48, 336, 48, 48),
                                       Vector(96, 336, 48, 48)]

        frame_data_idle_vertical_down = [Vector(0, 192, 48, 48),
                                         Vector(48, 192, 48, 48),
                                         Vector(96, 192, 48, 48)]
        
        frame_data_walk_horizontal = [Vector(0, 96, 48, 48),
                                      Vector(48, 96, 48, 48),
                                      Vector(96, 96, 48, 48)]

        frame_data_walk_vertical_up = [Vector(0, 142, 48, 48),
                                       Vector(48, 142, 48, 48),
                                       Vector(96, 142, 48, 48)]
        frame_data_walk_vertical_down = [Vector(0, 0, 48, 48),
                                         Vector(48, 0, 48, 48),
                                         Vector(96, 0, 48, 48)]


        self.sprite_sheet = SpriteSheet("sprites/characters/player.png")
        
        self.sprite_idle_horizontal = self.sprite_sheet.make_animation(frame_data_idle_horizontal, self.scale)
        self.sprite_idle_vertical_up = self.sprite_sheet.make_animation(frame_data_idle_vertical_up, self.scale)
        self.sprite_idle_vertical_down = self.sprite_sheet.make_animation(frame_data_idle_vertical_down, self.scale)
        
        self.sprite_walk_vertical_up = self.sprite_sheet.make_animation(frame_data_walk_vertical_up, self.scale)
        self.sprite_walk_vertical_down = self.sprite_sheet.make_animation(frame_data_walk_vertical_down, self.scale)
        self.sprite_walk = self.sprite_sheet.make_animation(frame_data_walk_horizontal, self.scale)

        self.current_frame = 0
        self.current_animation = self.sprite_idle_horizontal

        self.animationSpeed_idle = 0.80
        self.animationSpeed_walk = 0.13
        self.timePassed = 0
        self.direction_horizontal = False # False Right, True Left
        self.direction_vertical = False # False Down, True Up
        
        # Start position
        self.posX = 200
        self.posY = 200
        self.walkSpeed = 250

        #Start direction
        self.direction = DOWN

    def draw(self, screen, deltaTime):
        self.deltaTime = deltaTime
        #screen.blit(pygame.transform.flip(self.current_animation[self.current_frame], self.direction_horizontal, False), (self.posX, self.posY))
        if(self.direction == LEFT):
            screen.blit(pygame.transform.flip(self.current_animation[self.current_frame], True, False), (self.posX, self.posY))
        else:
            screen.blit(pygame.transform.flip(self.current_animation[self.current_frame], False, False), (self.posX, self.posY))
        self.timePassed += deltaTime

    def animate(self, animation, speed):
        self.current_animation = animation
        if(self.timePassed > speed):
            if(self.timePassed > speed):
                if(self.current_frame < len(animation)-1):
                    self.current_frame += 1
                else:
                    self.current_frame = 0
                self.timePassed = 0   

    def move(self, deltaTime, direction):
        self.direction = direction
        if(self.direction == UP):
            self.animate(self.sprite_walk_vertical_up, self.animationSpeed_walk)
            self.posY -= self.walkSpeed * deltaTime
        elif(self.direction == DOWN):
            self.animate(self.sprite_walk_vertical_down, self.animationSpeed_walk)
            self.posY += self.walkSpeed * deltaTime
        elif(self.direction == LEFT):
            self.animate(self.sprite_walk, self.animationSpeed_walk)
            self.posX -= self.walkSpeed * deltaTime
        elif(self.direction == RIGHT):
            self.animate(self.sprite_walk, self.animationSpeed_walk)
            self.posX += self.walkSpeed * deltaTime