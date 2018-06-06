import pygame
import utils
from enum import Enum
from buttons import StartButton, ExitButton

LOGO_SCALE = 1.5
INACTIVE = 0
ACTIVE = 1


class States(Enum):
    GAME = 1
    MENU = 2
    EXIT = 3
    PAUSE = 4
    RETRY = 5
    VICTORY = 6
    WON_LEVEL = 7
    GAME_OVER = 8
    NEXT_LEVEL = 9
    GO_TO_MENU = 10


class MenuBackground(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.image = pygame.image.load("Images/menu_background.png")
        self.image = pygame.transform.scale(self.image, screen)
        self.rect = self.image.get_rect()


class LogoSprite(pygame.sprite.Sprite):
    def __init__(self, screen_width):
        super().__init__()
        self.image = utils.load_and_scale("Images/menu_logo.png", LOGO_SCALE)
        self.rect = self.image.get_rect()
        self.rect.center = (int(screen_width / 2), int(self.image.get_height() / 2))


class MenuState:
    def __init__(self, screen):
        self.start_button = StartButton(screen)
        self.exit_button = ExitButton(screen)

        self.background = pygame.sprite.Group()
        self.background.add(MenuBackground(screen))

        self.menu_sprites = pygame.sprite.Group()
        self.menu_sprites.add(LogoSprite(screen[0]), self.start_button, self.exit_button)

    def update(self):
        new_state = States.MENU

        if self.start_button.check():
            pygame.mixer.music.play(-1)
            new_state = States.GAME

        if self.exit_button.check():
            new_state = States.EXIT

        self.menu_sprites.update()
        return new_state

    def draw(self, screen):
        self.background.draw(screen)
        self.menu_sprites.draw(screen)


