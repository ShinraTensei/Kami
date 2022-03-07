import pygame
from constants import *

class SpriteSheet(object):
    def __init__(self, file_path, frame_data):
        self.sprite_sheet = pygame.image.load(file_path).convert_alpha()

        for i in frame_data:
            self.get_image(frame_data, i)

    
    def get_image(self, img_vec, index):

        #Testing shit
        width = img_vec[index].getW()
        height = img_vec[index].getH()

        image = pygame.Surface([40, 40]).convert_alpha()

        image.blit(self.sprite_sheet, (0, 0), img_vec[index])
        return image