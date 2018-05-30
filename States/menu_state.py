import pygame
from enum import Enum
from buttons import StartButtonSprite, ExitButtonSprite

LOGO_SCALE = 1.5
INACTIVE = 0
ACTIVE = 1


class States(Enum):
    GAME = 1
    MENU = 2
    EXIT = 3
    PAUSE = 4


class MenuBackground(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.image = pygame.image.load("Images/menu_background.png")
        self.image = pygame.transform.scale(self.image, [screen_width, screen_height])
        self.rect = self.image.get_rect()


class LogoSprite(pygame.sprite.Sprite):
    def __init__(self, screen_width):
        super().__init__()
        self.image = pygame.image.load("Images/menu_logo.png")
        self.image = pygame.transform.scale(self.image,
                                            [int(dimension / LOGO_SCALE) for dimension in self.image.get_size()])
        self.rect = self.image.get_rect()
        self.rect.center = (int(screen_width / 2), int(self.image.get_height() / 2))


class MenuState:
    def __init__(self, screen_width, screen_height):
        self.menu_sprite = MenuBackground(screen_width, screen_height)
        self.logo_sprite = LogoSprite(screen_width)
        self.start_button_sprite = StartButtonSprite(screen_width, screen_height)
        self.exit_button_sprite = ExitButtonSprite(screen_width, screen_height)

        self.menu_sprites_list = pygame.sprite.Group()
        self.background_sprite_list = pygame.sprite.Group()
        self.background_sprite_list.add(self.menu_sprite)
        self.menu_sprites_list.add(self.logo_sprite, self.start_button_sprite, self.exit_button_sprite)
        self.new_state = States.MENU

    def menu(self):
        mouse_position = pygame.mouse.get_pos()
        pressed = pygame.mouse.get_pressed()

        self.start_button_sprite.set_state(INACTIVE)
        self.exit_button_sprite.set_state(INACTIVE)

        if self.start_button_sprite.rect.collidepoint(mouse_position):
            if pressed[0]:
                self.new_state = States.GAME
            self.start_button_sprite.set_state(ACTIVE)

        if self.exit_button_sprite.rect.collidepoint(mouse_position):
            if pressed[0]:
                self.new_state = States.EXIT
            self.exit_button_sprite.set_state(ACTIVE)

        self.menu_sprites_list.update()
        return self.new_state

    def draw(self, screen):
        self.background_sprite_list.draw(screen)
        self.menu_sprites_list.draw(screen)


