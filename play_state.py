import pygame
from player import Player, Direction
from enemy import Enemy
from bullet import bullets_list, enemy_bullets_list


NUM_OF_ENEMIES = 10


class PlayState:
    def __init__(self, screen_width, screen_height):
        self.player = Player(screen_width, screen_height)
        self.all_sprites_list = pygame.sprite.Group()
        self.enemies_sprites_list = pygame.sprite.Group()
        self.all_sprites_list.add(self.player)

    def generate_enemies(self):
        for i in range(NUM_OF_ENEMIES):
            enemy = Enemy((i + 1) * 80, 100)
            self.enemies_sprites_list.add(enemy)
            self.all_sprites_list.add(self.enemies_sprites_list)

    def bullet_enemy_collision_handler(self):
        global NUM_OF_ENEMIES
        if pygame.sprite.groupcollide(self.enemies_sprites_list,
                                      bullets_list,
                                      True,
                                      True,
                                      pygame.sprite.collide_mask):
            NUM_OF_ENEMIES -= 1

    def bullet_player_collision_handler(self):
        sprite = pygame.sprite.spritecollideany(self.player, enemy_bullets_list, pygame.sprite.collide_mask)
        if sprite:
            self.player.kill()
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

        self.all_sprites_list.update()
        self.all_sprites_list.add(bullets_list)
        self.all_sprites_list.add(enemy_bullets_list) # TODO cehck if this add can be combined with one above

        self.bullet_enemy_collision_handler()
        self.bullet_player_collision_handler()

    def draw(self, screen):
        self.all_sprites_list.draw(screen)
