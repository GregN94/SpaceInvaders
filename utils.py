import pygame


LIFE_SPRITE_SCALE = 6


def load_and_scale(image, scale):
    image = pygame.image.load(image)
    image = pygame.transform.scale(image,
                                   [int(dimension / scale) for dimension in image.get_size()])
    return image


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
