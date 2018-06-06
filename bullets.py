import pygame
import utils

SCALE = 10
POSITION_OFFSET = 10
SPEED = 6


class BulletsSprites:
    def __init__(self):
        self.player_bullets = pygame.sprite.Group()
        self.enemy_bullets = pygame.sprite.Group()


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.shot_sound = pygame.mixer.Sound("Sounds/player_shot.ogg")
        self.shot_sound.set_volume(0.3)
        self.shot_sound.play(0, 400, 0)
        self.image = utils.load_and_scale(image, SCALE)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y - int(self.image.get_height() / 2) - POSITION_OFFSET)
        self.mask = pygame.mask.from_surface(self.image)


class PlayerBullet(Bullet):
    def __init__(self, x, y):
        super().__init__(x, y, "Images/bullet.png")

    def update(self):
        self.rect.y -= SPEED
        if self.rect.y < 0:
            self.kill()


class EnemyBullet(Bullet):
    def __init__(self, x, y):
        super().__init__(x, y, "Images/enemy_bullet.png")

    def update(self):
        self.rect.y += SPEED
        if self.rect.y > 800:
            self.kill()





