import sys
import pygame
from constants import *
from player import Player

def run():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(TITLE)

    #Init
    plr = Player()

    getTicksLastFrame = 0
    deltaTime = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        #Clear to black
        screen.fill(pygame.color.Color(0, 0, 0))

        #Timing
        t = pygame.time.get_ticks()

        #Logic
        keys = pygame.key.get_pressed()
        if(keys[pygame.key.key_code("A")]):
            plr.move(deltaTime, LEFT)
        elif(keys[pygame.key.key_code("D")]):
            plr.move(deltaTime, RIGHT)
        elif(keys[pygame.key.key_code("W")]):
            plr.move(deltaTime, UP)
        elif(keys[pygame.key.key_code("S")]):
            plr.move(deltaTime, DOWN)
        else:
            if(plr.direction == LEFT or plr.direction == RIGHT):
                plr.animate(plr.sprite_idle_horizontal, plr.animationSpeed_idle)
            elif(plr.direction == UP):
                plr.animate(plr.sprite_idle_vertical_up, plr.animationSpeed_idle)
            else:
                plr.animate(plr.sprite_idle_vertical_down, plr.animationSpeed_idle)
        plr.draw(screen, deltaTime)

        pygame.display.flip()
        # deltaTime in seconds.
        deltaTime = (t - getTicksLastFrame) / 1000.0
        getTicksLastFrame = t


if __name__ == "__main__":
    sys.exit(run())