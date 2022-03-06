import pygame
from constants import *

class SpriteSheet(object):
    def __init__(self, file_path):
        self.sprite_sheet = pygame.image.load(file_path).convert_alpha()
    
    def get_image(self, x, y, width, height):
        image = pygame.Surface([width, height]).convert_alpha()
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        return image