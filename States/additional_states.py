import pygame
from buttons import ExitButtonSprite, ResumeButton, RetryButton, GoToMenu
from States.menu_state import States

BLACK = (0, 0, 0)
PANEL_SCALE = 3
SCALE = 2
WON_IMAGES = ["Images/won_inactive.png", "Images/won_active.png"]


class Background(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.image = pygame.Surface([screen_width, screen_height])
        self.image.fill(BLACK)
        self.image.set_alpha(128)
        self.rect = self.image.get_rect()


class PausePanel(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.image = pygame.image.load("Images/pause_panel.png")
        self.image = pygame.transform.scale(self.image,
                                            [int(dimension / PANEL_SCALE) for dimension in self.image.get_size()])
        self.rect = self.image.get_rect()
        self.rect.center = (int(screen_width / 2), int(screen_height / 2))


class Logo(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height, image):
        super().__init__()
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image,
                                            [int(dimension / SCALE) for dimension in self.image.get_size()])
        self.rect = self.image.get_rect()
        self.rect.center = (int(screen_width / 2), int(screen_height / 2) - 3 * self.image.get_height())
        self.state = 1

    def toggle(self, images):
        if self.state == 1:
            self.state = 0
        else:
            self.state = 1
        position = self.rect.center
        self.image = pygame.image.load(images[self.state])
        self.image = pygame.transform.scale(self.image,
                                            [int(dimension / SCALE) for dimension in self.image.get_size()])
        self.rect = self.image.get_rect()
        self.rect.center = position


class BasicState:
    def __init__(self, screen_width, screen_height, image):
        self.background = Background(screen_width, screen_height)
        self.panel = PausePanel(screen_width, screen_height)

        self.logo = Logo(screen_width, screen_height, image)
        self.resume_button = ResumeButton(screen_width, screen_height)
        self.retry_button = RetryButton(screen_width, screen_height)
        self.go_to_menu_button = GoToMenu(screen_width, screen_height)
        self.exit_button = ExitButtonSprite(screen_width, screen_height)

        self.background_sprites_list = pygame.sprite.Group()
        self.background_sprites_list.add(self.background)

        self.panel_sprite_list = pygame.sprite.Group()
        self.panel_sprite_list.add(self.panel)

        self.buttons_sprite_list = pygame.sprite.Group()

        self.buttons_sprite_list.add(self.logo,
                                     self.exit_button,
                                     self.retry_button,
                                     self.go_to_menu_button)

    def draw(self, screen):
        self.background_sprites_list.draw(screen)
        self.panel_sprite_list.draw(screen)
        self.buttons_sprite_list.draw(screen)


class Pause(BasicState):
    def __init__(self, screen_width, screen_height):
        super().__init__(screen_width, screen_height, "Images/pause_logo.png")
        self.resume_button = ResumeButton(screen_width, screen_height)
        self.buttons_sprite_list.add(self.resume_button)

    def update(self):
        new_state = States.PAUSE

        if self.exit_button.check():
            new_state = States.EXIT

        if self.resume_button.check():
            new_state = States.GAME

        if self.retry_button.check():
            new_state = States.RETRY

        if self.go_to_menu_button.check():
            new_state = States.GO_TO_MENU

        self.buttons_sprite_list.update()
        return new_state


class GameOver(BasicState):
    def __init__(self, screen_width, screen_height):
        super().__init__(screen_width, screen_height, "Images/game_over.png")

    def update(self):
        new_state = States.GAME_OVER

        if self.exit_button.check():
            new_state = States.EXIT

        if self.retry_button.check():
            new_state = States.RETRY

        if self.go_to_menu_button.check():
            new_state = States.GO_TO_MENU

        self.buttons_sprite_list.update()
        return new_state


class WinState(BasicState):
    def __init__(self, screen_width, screen_height):
        super().__init__(screen_width, screen_height, WON_IMAGES[0])

    def update(self):
        self.logo.toggle(WON_IMAGES)
        new_state = States.WIN

        if self.exit_button.check():
            new_state = States.EXIT

        if self.retry_button.check():
            new_state = States.RETRY

        if self.go_to_menu_button.check():
            new_state = States.GO_TO_MENU

        self.buttons_sprite_list.update()
        return new_state






