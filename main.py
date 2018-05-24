import pygame
from player import Player, Direction
from enemy import Enemy
from bullet import bullets_list, enemy_bullets_list

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
QUIT = False
NUM_OF_ENEMIES = 1
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player = Player(SCREEN_WIDTH, SCREEN_HEIGHT)

all_sprites_list = pygame.sprite.Group()

enemies_sprites_list = pygame.sprite.Group()


def generate_enemies():
    for i in range(NUM_OF_ENEMIES):
        enemy = Enemy((i + 1) * 80, 100)
        enemies_sprites_list.add(enemy)


generate_enemies()
all_sprites_list.add(enemies_sprites_list)
all_sprites_list.add(player)

clock = pygame.time.Clock()


def bullet_enemy_collision_handler():
    global NUM_OF_ENEMIES
    if pygame.sprite.groupcollide(enemies_sprites_list,
                                  bullets_list,
                                  True,
                                  True,
                                  pygame.sprite.collide_mask):
        NUM_OF_ENEMIES -= 1


def bullet_player_collision_handler():
    sprite = pygame.sprite.spritecollideany(player, enemy_bullets_list, pygame.sprite.collide_mask)
    if sprite:
        player.kill()
        sprite.kill()


def check_if_game_quited():
    global QUIT
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            QUIT = True


while not QUIT:
    check_if_game_quited()

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        player.move(Direction.LEFT)

    if pressed[pygame.K_RIGHT]:
        player.move(Direction.RIGHT)

    if pressed[pygame.K_SPACE] and not player.space_pressed:
        player.shot_bullet()

    if not pressed[pygame.K_SPACE]:
        player.space_pressed = False

    all_sprites_list.update()
    all_sprites_list.add(bullets_list)
    all_sprites_list.add(enemy_bullets_list)

    bullet_enemy_collision_handler()
    bullet_player_collision_handler()

    screen.fill((0, 0, 0))
    all_sprites_list.draw(screen)
    pygame.display.update()
    clock.tick(60)



