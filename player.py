import pygame
from enum import Enum
from bullet import Bullet

SCALE = 5
POSITION_OFFSET = 10
MAX_SPEED = 4
MAX_ANGLE = 15
SPEED_DAMPING = 0.5
ANGLE_DAMPING = 1
SPEED_ACCELERATION = ANGLE_DAMPING + 2
ANGLE_ACCELERATION = SPEED_DAMPING + 1


class Direction(Enum):
    LEFT = 0
    RIGHT = 1
    UP = 2
    DOWN = 3


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, bullets_list):
        super().__init__()

        self.space_pressed = False  # TODO change pressing space so this var can be removed
        self.image = pygame.image.load("Images/space_ship.png")
        self.image = pygame.transform.scale(self.image, [int(dimension / SCALE) for dimension in self.image.get_size()])
        self.image2 = self.image.copy()
        self.rect = self.image.get_rect()
        self.initial_position = (int(x / 2), y - int(self.image.get_height() / 2) - 2 * POSITION_OFFSET)
        self.rect.center = self.initial_position
        self.mask = pygame.mask.from_surface(self.image)
        self.bounds = [POSITION_OFFSET,
                       x - self.image.get_width() - POSITION_OFFSET,
                       y / 2,
                       y - self.image.get_height() - POSITION_OFFSET]
        self.angle = 0
        self.speed = 0
        self.bullets_list = bullets_list

    def update_angle(self):
        if self.angle > 0:
            self.angle -= ANGLE_DAMPING
        if self.angle < 0:
            self.angle += ANGLE_DAMPING

    def update_speed(self):
        if self.speed > 0:
            self.speed -= SPEED_DAMPING
        if self.speed < 0:
            self.speed += SPEED_DAMPING

    def update(self):
        self.update_angle()
        self.update_speed()

        self.image = pygame.transform.rotate(self.image2, self.angle)
        self.rect.x += self.speed

    def damage(self):
        self.rect.center = self.initial_position

    def move(self, direction):
        if direction == Direction.LEFT:
            self.move_left()
            if self.angle < MAX_ANGLE:
                self.angle += ANGLE_ACCELERATION
        if direction == Direction.RIGHT:
            self.move_right()
            if self.angle > -MAX_ANGLE:
                self.angle -= ANGLE_ACCELERATION

    def move_left(self):
        if self.rect.x > self.bounds[0]:
            if self.speed > -MAX_SPEED:
                self.speed -= SPEED_ACCELERATION

    def move_right(self):
        if self.rect.x < self.bounds[1]:
            if self.speed < MAX_SPEED:
                self.speed += SPEED_ACCELERATION

    def shot_bullet(self):
        self.space_pressed = True
        bullet = Bullet(self.rect.x + self.image2.get_width() / 2, self.rect.y)
        self.bullets_list.add(bullet)


