import pygame
import utils
from enemy import Enemies
from player import Player
from States.menu_state import States
from explosion import Explosion

NUM_OF_ENEMIES_PER_LVL = 4
BACKGROUND_SCALE = 1.5
MAX_LVL = 15


class Background(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = utils.load_and_scale("Images/background", BACKGROUND_SCALE)
        self.rect = self.image.get_rect()


class PlayState:
    def __init__(self, screen, level, timer):
        self.timer = timer
        self.level = level
        self.screen_width = screen[0]
        self.screen_height = screen[1]
        self.player_bullets = pygame.sprite.Group()
        self.enemy_bullets = pygame.sprite.Group()
        self.player = Player(self.screen_width,
                             self.screen_height,
                             self.player_bullets)

        self.background_sprite = pygame.sprite.Group()
        self.background_sprite.add(Background())

        self.player_explosion_sprite = pygame.sprite.Group()
        self.pause_sprites = pygame.sprite.Group()

        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player)

        self.num_of_enemies = NUM_OF_ENEMIES_PER_LVL * self.level
        self.enemies = Enemies(self.num_of_enemies,
                               self.screen_width,
                               self.enemy_bullets,
                               self.timer,
                               self.player.initial_position[1])
        self.all_sprites.add(self.enemies)

        self.num_of_lives = 3
        self.lives = []
        utils.generate_lives(self.num_of_lives,
                             self.lives,
                             self.all_sprites,)

        self.state = States.GAME
        self.player_hit = False
        self.space_pressed = False

    def create_enemy_explosion(self, sprite_dict):
        for sprite in sprite_dict:
            if sprite_dict[sprite]:
                explosion = Explosion(sprite.rect.center)
                self.all_sprites.add(explosion)
                self.num_of_enemies -= 1

    def check_collision_bullets_enemies(self):

        sprite_dict = pygame.sprite.groupcollide(self.enemies,
                                                 self.player_bullets,
                                                 True,
                                                 True,
                                                 pygame.sprite.collide_mask)
        self.create_enemy_explosion(sprite_dict)

    def kill_player(self):
        if len(self.lives):
            life = self.lives.pop()
            life.kill()
            explosion = Explosion(self.player.rect.center)
            self.player_explosion_sprite.add(explosion)

    def check_collision_bullets_player(self):
        bullet = pygame.sprite.spritecollideany(self.player,
                                                self.enemy_bullets,
                                                pygame.sprite.collide_mask)
        if bullet:
            self.player_hit = True
            bullet.kill()
            self.kill_player()

    def check_if_won(self):
        if self.num_of_enemies == 0:
            if self.level == MAX_LVL:
                pygame.mixer.music.load("Sounds/win_music")
                pygame.mixer.music.play(-1)
                self.state = States.VICTORY
            self.state = States.WON_LEVEL

    def check_if_game_over(self):
        if len(self.lives) == 0 or self.enemies.is_any_down_the_screen():
            self.player.kill()
            self.state = States.GAME_OVER
            pygame.mixer.music.load("Sounds/game_over_music")
            pygame.mixer.music.play(-1)

    def control_player(self):
        if not self.timer.is_running:
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_LEFT]:
                self.player.move_left()

            if pressed[pygame.K_RIGHT]:
                self.player.move_right()

            if pressed[pygame.K_SPACE] and not self.space_pressed:
                self.space_pressed = True
                self.player.shoot_bullet()

            if not pressed[pygame.K_SPACE]:
                self.space_pressed = False

    def animation(self):
        self.all_sprites.add(self.enemy_bullets)
        self.all_sprites.update()

    def draw(self, screen):
        self.background_sprite.draw(screen)
        self.all_sprites.draw(screen)
        self.player_explosion_sprite.draw(screen)

    def player_got_hit(self):
        self.timer.start()

        self.player_explosion_sprite.update()
        if len(self.player_explosion_sprite.sprites()) == 0:
            self.player.go_to_initial_position()
            self.player_hit = False

        self.enemies.update()
        self.enemy_bullets.update()

    def fight(self):
        self.control_player()

        self.all_sprites.add(self.player_bullets,
                             self.enemy_bullets)
        self.all_sprites.update()
        if not self.timer.is_running:
            self.check_collision_bullets_player()
        self.check_collision_bullets_enemies()
        self.check_if_won()
        self.check_if_game_over()

    def update(self):
        if self.player_hit:
            self.player_got_hit()
        else:
            self.fight()
        return self.state


