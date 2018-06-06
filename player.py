import pygame
import utils
from bullets import PlayerBullet

SCALE = 5
POSITION_OFFSET = 10
MAX_SPEED = 6
MAX_ANGLE = 15
SPEED_DAMPING = 0.5
ANGLE_DAMPING = 1
SPEED_ACCELERATION = ANGLE_DAMPING + 2
ANGLE_ACCELERATION = SPEED_DAMPING + 1


class Player(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height, bullets):
        super().__init__()
        self.angle = 0
        self.speed = 0
        self.bullets = bullets
        self.image = utils.load_and_scale("Images/space_ship.png", SCALE)
        self.image_copy = self.image.copy()
        self.rect = self.image.get_rect()
        self.initial_position = (int(screen_width / 2),
                                 screen_height - int(self.image.get_height() / 2) - 2 * POSITION_OFFSET)
        self.rect.center = self.initial_position
        self.mask = pygame.mask.from_surface(self.image)
        self.bounds = [5 * POSITION_OFFSET,
                       screen_width - self.image.get_width() - 5 * POSITION_OFFSET]

    def decrease_angle(self):
        if self.angle > 0:
            self.angle -= ANGLE_DAMPING
        if self.angle < 0:
            self.angle += ANGLE_DAMPING

    def decrease_speed(self):
        if self.speed > 0:
            self.speed -= SPEED_DAMPING
        if self.speed < 0:
            self.speed += SPEED_DAMPING

    def update(self):
        self.decrease_angle()
        self.decrease_speed()

        self.image = pygame.transform.rotate(self.image_copy, self.angle)
        self.rect.x += self.speed

    def go_to_initial_position(self):
        self.rect.center = self.initial_position

    def move_left(self):
        if self.rect.x > self.bounds[0]:
            if self.speed > -MAX_SPEED:
                self.speed -= SPEED_ACCELERATION
        if self.angle < MAX_ANGLE:
            self.angle += ANGLE_ACCELERATION

    def move_right(self):
        if self.rect.x < self.bounds[1]:
            if self.speed < MAX_SPEED:
                self.speed += SPEED_ACCELERATION
        if self.angle > -MAX_ANGLE:
            self.angle -= ANGLE_ACCELERATION

    def shot_bullet(self):
        bullet = PlayerBullet(self.rect.x + self.image.get_width() / 2, self.rect.y)
        self.bullets.add(bullet)




