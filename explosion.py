import pygame
import glob

ANIMATION = glob.glob("Images/Explosion/boom*.png")
ANIMATION.sort()
SCALE = 4

class Explosion(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.animation_index = 0
        self.image = pygame.image.load(ANIMATION[self.animation_index])
        self.image = pygame.transform.scale(self.image,
                                            [int(dimension / SCALE) for dimension in self.image.get_size()])
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.animation_time_init = 12
        self.animation_time = self.animation_time_init
        self.sound = pygame.mixer.Sound("Sounds/explosion.ogg")
        self.sound.set_volume(0.3)
        self.sound.play(0, 700, 0)

    def update(self):
        if self.animation_time == 0:
            self.kill()
        self.animation_time -= 1
        if self.animation_time % 2 == 0:
            position = self.rect.center
            self.image = pygame.image.load(ANIMATION[self.animation_index])
            self.image = pygame.transform.scale(self.image,
                                                [int(dimension / SCALE) for dimension in self.image.get_size()])
            self.rect.center = position
            self.animation_index += 1




