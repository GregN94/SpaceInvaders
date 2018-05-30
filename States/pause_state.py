import pygame
from buttons import ExitButtonSprite, ResumeButton, RetryButton
from States.menu_state import States

INACTIVE = 0
ACTIVE = 1
BLACK = (0, 0, 0)
PANEL_SCALE = 3
SCALE = 2


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


class PauseLogo(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.image = pygame.image.load("Images/pause_logo.png")
        self.image = pygame.transform.scale(self.image,
                                            [int(dimension / SCALE) for dimension in self.image.get_size()])
        self.rect = self.image.get_rect()
        self.rect.center = (int(screen_width / 2), int(screen_height / 2) - 3 * self.image.get_height())


class Pause:
    def __init__(self, screen_width, screen_height):
        self.background = Background(screen_width, screen_height)
        self.pause_panel = PausePanel(screen_width, screen_height)
        self.pause_logo = PauseLogo(screen_width, screen_height)
        self.resume_button = ResumeButton(screen_width, screen_height)
        self.retry_button = RetryButton(screen_width, screen_height)
        self.exit_button = ExitButtonSprite(screen_width, screen_height)

        self.background_sprites_list = pygame.sprite.Group()
        self.background_sprites_list.add(self.background)

        self.panel_sprite_list = pygame.sprite.Group()
        self.panel_sprite_list.add(self.pause_panel)

        self.buttons_sprite_list = pygame.sprite.Group()
        self.buttons_sprite_list.add(self.pause_logo, self.exit_button, self.resume_button, self.retry_button)

    def update(self):
        new_state = States.PAUSE
        mouse_position = pygame.mouse.get_pos()
        pressed = pygame.mouse.get_pressed()

        self.exit_button.set_state(INACTIVE)
        self.resume_button.set_state(INACTIVE)
        self.retry_button.set_state(INACTIVE)

        if self.exit_button.rect.collidepoint(mouse_position):
            if pressed[0]:
                new_state = States.EXIT
            self.exit_button.set_state(ACTIVE)

        if self.resume_button.rect.collidepoint(mouse_position):
            if pressed[0]:
                new_state = States.GAME
            self.resume_button.set_state(ACTIVE)

        if self.retry_button.rect.collidepoint(mouse_position):
            if pressed[0]:
                new_state = States.RETRY
            self.retry_button.set_state(ACTIVE)

        self.buttons_sprite_list.update()
        return new_state

    def draw(self, screen):
        self.background_sprites_list.draw(screen)
        self.panel_sprite_list.draw(screen)
        self.buttons_sprite_list.draw(screen)


