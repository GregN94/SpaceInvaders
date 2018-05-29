import pygame

BLACK = (0, 0, 0)


class Background(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.image = pygame.Surface([screen_width, screen_height])
        self.image.fill(BLACK)
        self.image.set_alpha(128)
        self.rect = self.image.get_rect()

