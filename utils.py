import pygame
import math
from enemy import Enemy

LIFE_SPRITE_SCALE = 6


def load_and_scale(image, scale):
    image = pygame.image.load(image)
    image = pygame.transform.scale(image,
                                   [int(dimension / scale) for dimension in image.get_size()])
    return image


def generate_enemies(num_of_enemies, screen_width, enemy_bullets, enemies_sprites):
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
                      enemy_bullets,
                      direction)
        enemies_sprites.add(enemy)
    return enemies_sprites


class Life(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = load_and_scale("Images/heart.png", LIFE_SPRITE_SCALE)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


def generate_lives(num_of_lives, lives, all_sprites):
    for i in range(num_of_lives):
        heart = Life(30 + i * 45, 20)
        lives.append(heart)
        all_sprites.add(heart)
