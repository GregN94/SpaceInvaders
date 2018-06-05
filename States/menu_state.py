import pygame
import utils
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
    RETRY = 5
    GO_TO_MENU = 6
    GAME_OVER = 7
    WIN = 8


class MenuBackground(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.image = pygame.image.load("Images/menu_background.png")
        self.image = pygame.transform.scale(self.image, [screen_width, screen_height])
        self.rect = self.image.get_rect()


class LogoSprite(pygame.sprite.Sprite):
    def __init__(self, screen_width):
        super().__init__()
        self.image = utils.load_and_scale("Images/menu_logo.png", LOGO_SCALE)
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

    def update(self):
        new_state = States.MENU

        if self.start_button_sprite.check():
            pygame.mixer.music.play(-1)
            new_state = States.GAME

        if self.exit_button_sprite.check():
            new_state = States.EXIT

        self.menu_sprites_list.update()
        return new_state

    def draw(self, screen):
        self.background_sprite_list.draw(screen)
        self.menu_sprites_list.draw(screen)


