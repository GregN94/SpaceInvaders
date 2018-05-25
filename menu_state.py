import pygame
from menu_sprites import MenuSprite, LogoSprite, StartButtonSprite

INACTIVE = 0
ACTIVE = 1


class MenuState:
    def __init__(self, screen_width, screen_height):
        self.menu_sprite = MenuSprite(screen_width, screen_height)
        self.logo_sprite = LogoSprite(screen_width)
        self.start_button_sprite = StartButtonSprite(screen_width, screen_height)

        self.menu_sprites_list = pygame.sprite.Group()
        self.menu_sprites_list.add(self.menu_sprite)
        self.menu_sprites_list.add(self.logo_sprite)
        self.menu_sprites_list.add(self.start_button_sprite)

    def menu(self):
        self.start_button_sprite.set_state(INACTIVE)
        mouse_position = pygame.mouse.get_pos()
        if self.start_button_sprite.rect.collidepoint(mouse_position):
            self.start_button_sprite.set_state(ACTIVE)
            pressed = pygame.mouse.get_pressed()
            if pressed[0]:
                return True
            else:
                return False

    def draw(self, screen):
        self.menu_sprites_list.draw(screen)

