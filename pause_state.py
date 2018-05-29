import pygame
from pause_sprites import Background


class Pause:
    def __init__(self, screen_width, screen_height):
        self.background = Background(screen_width, screen_height)
        self.background_sprites_list = pygame.sprite.Group()
        self.background_sprites_list.add(self.background)

    def draw(self, screen):
        self.background_sprites_list.draw(screen)

