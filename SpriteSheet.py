import pygame
from constants import *
from Vector import *

class SpriteSheet(object):
    def __init__(self, file_path):
        self.sprite_sheet = pygame.image.load(file_path).convert_alpha()

    def make_animation(self, frame_data, scale):
        frames = []
        for frame in frame_data:
            frames.append(self.get_image(frame, scale))
        return frames
    
    def get_image(self, frame, scale):
        image = pygame.Surface([frame.w, frame.h]).convert_alpha()
        image.blit(self.sprite_sheet, (0, 0), (frame.x, frame.y, frame.w, frame.h))
        image = pygame.transform.scale(image, (frame.w*scale, frame.h*scale))
        return image