import pygame
import utils
from player import Player
from enemy import Enemy
from bullets import BulletsSprites
from States.menu_state import States
from explosion import Explosion


NUM_OF_ENEMIES = 10
SCALE = 4
BACKGROUND_SCALE = 1.5


class Life(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = utils.load_and_scale("Images/heart.png", SCALE)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


class Background(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = utils.load_and_scale("Images/background", BACKGROUND_SCALE)
        self.rect = self.image.get_rect()


class PlayState:
    def __init__(self, screen_width, screen_height):
        self.bullets_sprites = BulletsSprites()
        self.player = Player(screen_width,
                             screen_height,
                             self.bullets_sprites.bullets)

        self.background = Background()
        self.background_sprite = pygame.sprite.Group()
        self.background_sprite.add(self.background)

        self.player_explosion_sprite = pygame.sprite.Group()
        self.pause_sprites = pygame.sprite.Group()

        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player)

        self.num_of_enemies = NUM_OF_ENEMIES
        self.enemies_sprites = pygame.sprite.Group()
        self.generate_enemies()

        self.num_of_lives = 3
        self.lives = []
        self.generate_lives()

        self.state = States.GAME
        self.player_hit = False
        self.space_pressed = False

    def generate_lives(self):
        for i in range(self.num_of_lives):
            heart = Life(40 + i * 80, 40)
            self.lives.append(heart)
            self.all_sprites.add(heart)

    def generate_enemies(self):
        for i in range(self.num_of_enemies):
            enemy = Enemy((i + 1) * 80,
                          100,
                          self.bullets_sprites.enemy_bullets)
            self.enemies_sprites.add(enemy)
            self.all_sprites.add(self.enemies_sprites)

    def check_if_won(self):
        if self.num_of_enemies == 0:
            pygame.mixer.music.load("Sounds/win_music")
            pygame.mixer.music.play(-1)
            self.state = States.WIN

    def check_collision_bullets_enemies(self):

        sprite_dict = pygame.sprite.groupcollide(self.enemies_sprites,
                                                 self.bullets_sprites.bullets,
                                                 True,
                                                 True,
                                                 pygame.sprite.collide_mask)
        for sprite in sprite_dict:
            if sprite_dict[sprite]:
                explosion = Explosion(sprite.rect.center)
                self.all_sprites.add(explosion)
                self.num_of_enemies -= 1

    def check_collision_bullets_player(self):
        bullet = pygame.sprite.spritecollideany(self.player,
                                                self.bullets_sprites.enemy_bullets,
                                                pygame.sprite.collide_mask)
        if bullet:
            self.player_hit = True
            bullet.kill()
            if len(self.lives):
                heart = self.lives.pop()
                heart.kill()
                explosion = Explosion(self.player.rect.center)
                self.player_explosion_sprite.add(explosion)

    def check_if_game_over(self):
        if len(self.lives) == 0:
            self.player.kill()
            self.state = States.GAME_OVER
            pygame.mixer.music.load("Sounds/game_over_music")
            pygame.mixer.music.play(-1)

    def control_player(self):
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_LEFT]:
            self.player.move_left()

        if pressed[pygame.K_RIGHT]:
            self.player.move_right()

        if pressed[pygame.K_SPACE] and not self.space_pressed:
            self.space_pressed = True
            self.player.shot_bullet()

        if not pressed[pygame.K_SPACE]:
            self.space_pressed = False

    def animation(self):
        self.all_sprites.add(self.bullets_sprites.enemy_bullets)
        self.all_sprites.update()

    def draw(self, screen):
        self.background_sprite.draw(screen)
        self.all_sprites.draw(screen)
        self.player_explosion_sprite.draw(screen)

    def player_got_hit_state(self):

        self.player_explosion_sprite.update()
        if len(self.player_explosion_sprite.sprites()) == 0:
            self.player.go_to_initial_position()
            self.player_hit = False

        self.enemies_sprites.update()
        self.bullets_sprites.enemy_bullets.update()

    def fight_state(self):
        self.control_player()

        self.all_sprites.add(self.bullets_sprites.bullets,
                             self.bullets_sprites.enemy_bullets)
        self.all_sprites.update()

        self.check_collision_bullets_player()
        self.check_collision_bullets_enemies()
        self.check_if_won()
        self.check_if_game_over()

    def update(self):
        if self.player_hit:
            self.player_got_hit_state()
        else:
            self.fight_state()

        return self.state


