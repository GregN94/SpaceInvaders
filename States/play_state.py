import pygame
from player import Player, Direction
from enemy import Enemy
from bullet import BulletsSprites
from States.menu_state import States


NUM_OF_ENEMIES = 10
SCALE = 4


class Heart(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("Images/heart.png")
        self.image = pygame.transform.scale(self.image, [int(dimension / SCALE) for dimension in self.image.get_size()])
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


class PlayState:
    def __init__(self, screen_width, screen_height):
        self.num_of_lives = 3
        self.lives = []
        self.num_of_enemies = NUM_OF_ENEMIES
        self.bullets_sprites = BulletsSprites()
        self.player = Player(screen_width, screen_height, self.bullets_sprites.bullets_list)

        self.all_sprites_list = pygame.sprite.Group()
        self.enemies_sprites_list = pygame.sprite.Group()
        self.pause_sprites_list = pygame.sprite.Group()
        self.all_sprites_list.add(self.player)
        self.generate_enemies()
        self.generate_lives()
        self.state = States.GAME
        self.shot_sound = pygame.mixer.Sound("Sounds/explosion.ogg")
        self.shot_sound.set_volume(0.3)

    def generate_lives(self):
        for i in range(self.num_of_lives):
            heart = Heart(40 + i * 80, 40)
            self.lives.append(heart)
            self.all_sprites_list.add(heart)

    def generate_enemies(self):
        for i in range(self.num_of_enemies):
            enemy = Enemy((i + 1) * 80, 100, self.bullets_sprites.enemy_bullets_list)
            self.enemies_sprites_list.add(enemy)
            self.all_sprites_list.add(self.enemies_sprites_list)

    def bullet_enemy_collision_handler(self):
        if pygame.sprite.groupcollide(self.enemies_sprites_list,
                                      self.bullets_sprites.bullets_list,
                                      True,
                                      True,
                                      pygame.sprite.collide_mask):
            self.num_of_enemies -= 1
            self.shot_sound.play(0, 700, 0)
        if self.num_of_enemies == 0:
            pygame.mixer.music.load("Sounds/win_music")
            pygame.mixer.music.play(-1)
            self.state = States.WIN

    def bullet_player_collision_handler(self):
        sprite = pygame.sprite.spritecollideany(self.player,
                                                self.bullets_sprites.enemy_bullets_list,
                                                pygame.sprite.collide_mask)
        if sprite:
            if len(self.lives):
                heart = self.lives.pop()
                heart.kill()
                self.player.damage()
                self.shot_sound.play(0, 700, 0)
            if len(self.lives) == 0:
                self.player.kill()
                self.state = States.GAME_OVER
                pygame.mixer.music.load("Sounds/game_over_music")
                pygame.mixer.music.play(-1)
            sprite.kill()

    def play(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:
            self.player.move(Direction.LEFT)

        if pressed[pygame.K_RIGHT]:
            self.player.move(Direction.RIGHT)

        if pressed[pygame.K_SPACE] and not self.player.space_pressed:
            self.player.shot_bullet()

        if not pressed[pygame.K_SPACE]:
            self.player.space_pressed = False

        self.all_sprites_list.add(self.bullets_sprites.bullets_list, self.bullets_sprites.enemy_bullets_list)
        self.all_sprites_list.update()

        self.bullet_enemy_collision_handler()
        self.bullet_player_collision_handler()

        return self.state

    def animation(self):
        self.all_sprites_list.add(self.bullets_sprites.enemy_bullets_list)
        self.all_sprites_list.update()

    def draw(self, screen):
        self.all_sprites_list.draw(screen)



