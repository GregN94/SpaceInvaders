import pygame
import random
from bullet import EnemyBullet

SCALE = 6
POSITION_OFFSET = 10
SPEED = 1
ENEMY_PATH = ["Images/enemy.png", "Images/enemy_up.png"]


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, enemy_bullets):
        super().__init__()
        self.image_number = 0
        self.image = pygame.image.load(ENEMY_PATH[self.image_number])
        self.image = pygame.transform.scale(self.image,
                                            [int(dimension / SCALE) for dimension in self.image.get_size()])
        self.rect = self.image.get_rect()
        self.rect.center = (x, y - int(self.image.get_height() / 2) - POSITION_OFFSET)
        self.mask = pygame.mask.from_surface(self.image)
        self.speed = SPEED
        self.enemy_bullets = enemy_bullets

    def animation(self):
        if self.image_number == 0:
            self.image_number = 1
        else:
            self.image_number = 0
        position = self.rect.center
        self.image = pygame.image.load(ENEMY_PATH[self.image_number])
        self.image = pygame.transform.scale(self.image,
                                            [int(dimension / SCALE) for dimension in self.image.get_size()])
        self.rect = self.image.get_rect()
        self.rect.center = position

    def change_direction(self, speed):
        self.rect.y += self.image.get_height()
        self.speed = speed

    def update(self):
        self.rect.x += self.speed
        if self.rect.x + self.image.get_width() / 2 > 980:
            self.change_direction(-SPEED)

        if self.rect.x + self.image.get_width() / 2 < 20:
            self.change_direction(SPEED)

        if random.randrange(0, 200, 2) == 16:
            self.shot_bullet()
            self.animation()

    def shot_bullet(self):
        bullet = EnemyBullet(self.rect.x + self.image.get_width() / 2,
                             self.rect.y + self.image.get_height() + POSITION_OFFSET)
        self.enemy_bullets.add(bullet)
