import pygame
import random
from bullet import EnemyBullet, enemy_bullets_list

SCALE = 6
POSITION_OFFSET = 10
SPEED = 1


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.image.load("Images/enemy.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, [int(dimension / SCALE) for dimension in self.image.get_size()])
        self.rect = self.image.get_rect()
        self.rect.center = (x, y - int(self.image.get_height() / 2) - POSITION_OFFSET)
        self.mask = pygame.mask.from_surface(self.image)
        self.speed = SPEED

    def update(self):
        self.rect.x += self.speed
        if self.rect.x + self.image.get_width() / 2 > 550:
            self.rect.y += self.image.get_height()
            self.speed = -SPEED
        if self.rect.x + self.image.get_width() / 2 < 50:
            self.rect.y += self.image.get_height()
            self.speed = SPEED

        if random.randrange(0, 100, 2) == 0:
            self.shot_bullet()

    def shot_bullet(self):
        bullet = EnemyBullet(self.rect.x + self.image.get_width() / 2,
                             self.rect.y + self.image.get_height() + POSITION_OFFSET)
        enemy_bullets_list.add(bullet)
