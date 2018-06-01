import pygame

SCALE = 10
POSITION_OFFSET = 10
SPEED = 5


class BulletsSprites:
    def __init__(self):
        self.bullets_list = pygame.sprite.Group()
        self.enemy_bullets_list = pygame.sprite.Group()


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.shot_sound = pygame.mixer.Sound("Sounds/player_shot.ogg")
        self.shot_sound.play(0, 400, 0)
        self.image = pygame.image.load("Images/bullet.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, [int(dimension / SCALE) for dimension in self.image.get_size()])
        self.rect = self.image.get_rect()
        self.rect.center = (x, y - int(self.image.get_height() / 2) - POSITION_OFFSET)
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect.y -= SPEED
        if self.rect.y < 0:
            self.kill()


class EnemyBullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.shot_sound = pygame.mixer.Sound("Sounds/enemy_shot.ogg")
        self.shot_sound.play(0, 400, 0)
        self.image = pygame.image.load("Images/enemy_bullet.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, [int(dimension / SCALE) for dimension in self.image.get_size()])
        self.rect = self.image.get_rect()
        self.rect.center = (x, y - int(self.image.get_height() / 2) - POSITION_OFFSET)
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect.y += SPEED
        if self.rect.y > 800:
            self.kill()





