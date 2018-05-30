import pygame

BLACK = (0, 0, 0)
PANEL_SCALE = 3
SCALE = 2
RESUME_BUTTONS = ["Images/Buttons/resume_button_inactive.png", "Images/Buttons/resume_button_active.png"]


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


class ResumeButton(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.image = pygame.image.load(RESUME_BUTTONS[0])
        self.image = pygame.transform.scale(self.image,
                                            [int(dimension / SCALE) for dimension in self.image.get_size()])
        self.rect = self.image.get_rect()
        self.rect.center = (int(screen_width / 2), int(screen_height / 2) - 2 * self.image.get_height())

    def set_state(self, state):
        position = self.rect.center
        self.image = pygame.image.load(RESUME_BUTTONS[state])
        self.image = pygame.transform.scale(self.image,
                                            [int(dimension / SCALE) for dimension in self.image.get_size()])
        self.rect = self.image.get_rect()
        self.rect.center = position




