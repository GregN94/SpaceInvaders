import pygame
from player import Player

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 128, 255)

pygame.init()
screen = pygame.display.set_mode((400, 300))

done = False

player = Player()

all_sprites_list = pygame.sprite.Group()

all_sprites_list.add(player)

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        # if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        #    is_blue = not is_blue

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: player.rect.y -= 3
    if pressed[pygame.K_DOWN]: player.rect.y += 3
    if pressed[pygame.K_LEFT]: player.rect.x -= 3
    if pressed[pygame.K_RIGHT]: player.rect.x += 3

    screen.fill(BLACK)
    color = (0, 128, 255)
    all_sprites_list.draw(screen)



    pygame.display.update()
    clock.tick(60)
