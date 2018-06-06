import pygame
import random
import utils
import math
from bullets import EnemyBullet

SCALE = 6
POSITION_OFFSET = 10
SPEED = 1
ENEMY_PATH = ["Images/enemy.png", "Images/enemy_up.png"]
DO_NOT_SHOT_TIME_INIT = 60


class Enemies:
    def __init__(self, num_of_enemies, screen_width, bullets, timer):
        self.enemies = pygame.sprite.Group()
        self.generate_enemies(num_of_enemies, screen_width, bullets, timer)

    def generate_enemies(self, num_of_enemies, screen_width, bullets, timer):
        rows = math.ceil(num_of_enemies / 10)
        enemy_per_row = math.ceil(num_of_enemies / rows)
        enemy_in_row = 0
        row = 1
        for i in range(num_of_enemies):
            if enemy_in_row + 1 > enemy_per_row:
                row += 1
                enemy_in_row = 0
            direction = 1
            if row % 2:
                width = (enemy_in_row + 1) * 80
            else:
                width = screen_width - ((enemy_per_row - enemy_in_row) * 80)
                direction = -1
            height = 70 + row * 55
            enemy_in_row += 1
            enemy = Enemy(width,
                          height,
                          bullets,
                          direction, timer)
            self.enemies.add(enemy)

    def get(self):
        return self.enemies


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, enemy_bullets, direction, timer):
        super().__init__()
        self.image_number = 0
        self.image = utils.load_and_scale(ENEMY_PATH[self.image_number], SCALE)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y - int(self.image.get_height() / 2) - POSITION_OFFSET)
        self.mask = pygame.mask.from_surface(self.image)
        self.speed = direction * SPEED
        self.enemy_bullets = enemy_bullets
        self.timer = timer

    def animation(self):
        if self.image_number == 0:
            self.image_number = 1
        else:
            self.image_number = 0
        position = self.rect.center
        self.image = utils.load_and_scale(ENEMY_PATH[self.image_number], SCALE)
        self.rect = self.image.get_rect()
        self.rect.center = position

    def change_direction(self):
        self.rect.y += self.image.get_height()
        self.speed *= -1

    def update(self):
        self.rect.x += self.speed
        if self.rect.x + self.image.get_width() / 2 > 980:
            self.change_direction()

        if self.rect.x + self.image.get_width() / 2 < 20:
            self.change_direction()

        if random.randrange(0, 200, 2) == 16 and not self.timer.is_running:
            self.shot_bullet()
            self.animation()

    def shot_bullet(self):
        bullet = EnemyBullet(self.rect.x + self.image.get_width() / 2,
                             self.rect.y + self.image.get_height() + POSITION_OFFSET)
        self.enemy_bullets.add(bullet)
