import pygame

SCALE = 5
POSITION_OFFSET = 10
SPEED = 5


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.image.load("Images/space_ship.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, [int(dimension / SCALE) for dimension in self.image.get_size()])
        self.rect = self.image.get_rect()
        self.rect.center = (x, y - int(self.image.get_height() / 2) - POSITION_OFFSET)

    def move_left(self):
        self.rect.x -= SPEED

    def move_rght(self):
        self.rect.x += SPEED

    def move_up(self):
        self.rect.y -= SPEED

    def move_down(self):
        self.rect.y += SPEED
