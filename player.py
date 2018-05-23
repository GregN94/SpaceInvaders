import pygame
from enum import Enum

SCALE = 5
POSITION_OFFSET = 10
SPEED = 5


class Direction(Enum):
    LEFT = 0;
    RIGHT = 1;
    UP = 2;
    DOWN = 3;


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.image.load("Images/space_ship.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, [int(dimension / SCALE) for dimension in self.image.get_size()])
        self.rect = self.image.get_rect()
        self.rect.center = (int(x / 2), y - int(self.image.get_height() / 2) - POSITION_OFFSET)
        self.mask = pygame.mask.from_surface(self.image)
        self.bounds = [POSITION_OFFSET,
                       x - self.image.get_width() - POSITION_OFFSET,
                       y / 2,
                       y - self.image.get_height() - POSITION_OFFSET]

    def move(self, direction):
        if direction == Direction.LEFT:
            self.move_left()
        if direction == Direction.RIGHT:
            self.move_right()
        # if direction == Direction.UP:
        #     self.move_up()
        # if direction == Direction.DOWN:
        #     self.move_down()

    def move_left(self):
        if self.rect.x > self.bounds[0]:
            self.rect.x -= SPEED

    def move_right(self):
        if self.rect.x < self.bounds[1]:
            self.rect.x += SPEED

    def move_up(self):
        if self.rect.y > self.bounds[2]:
            self.rect.y -= SPEED

    def move_down(self):
        if self.rect.y < self.bounds[3]:
            self.rect.y += SPEED

