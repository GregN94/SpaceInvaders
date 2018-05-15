import pygame
from player import Player

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
QUIT = False

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player = Player(int(SCREEN_WIDTH / 2), SCREEN_HEIGHT)

all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(player)

clock = pygame.time.Clock()

while not QUIT:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            QUIT = True

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: player.move_up()
    if pressed[pygame.K_DOWN]: player.move_down()
    if pressed[pygame.K_LEFT]: player.move_left()
    if pressed[pygame.K_RIGHT]: player.move_rght()

    screen.fill((0, 0, 0))
    all_sprites_list.draw(screen)
    pygame.display.update()
    clock.tick(60)
