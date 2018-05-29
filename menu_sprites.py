import pygame


LOGO_SCALE = 1.5
BUTTON_SCALE = 2


class MenuSprite(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.image = pygame.image.load("Images/menu_background.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, [screen_width, screen_height])
        self.rect = self.image.get_rect()


class LogoSprite(pygame.sprite.Sprite):
    def __init__(self, screen_width):
        super().__init__()
        self.image = pygame.image.load("Images/menu_logo.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,
                                            [int(dimension / LOGO_SCALE) for dimension in self.image.get_size()])
        self.rect = self.image.get_rect()
        self.rect.center = (int(screen_width / 2), int(self.image.get_height() / 2))


START_BUTTON = ["Images/start_button_inactive.png", "Images/start_button_active.png"]


class StartButtonSprite(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.image = pygame.image.load(START_BUTTON[0]).convert_alpha()
        self.image = pygame.transform.scale(self.image,
                                            [int(dimension / BUTTON_SCALE) for dimension in self.image.get_size()])
        self.rect = self.image.get_rect()
        self.rect.center = (int(screen_width / 2), int(screen_height / 2))

    def set_state(self, state):
        position = self.rect.center
        self.image = pygame.image.load(START_BUTTON[state]).convert_alpha()
        self.image = pygame.transform.scale(self.image,
                                            [int(dimension / BUTTON_SCALE) for dimension in self.image.get_size()])
        self.rect = self.image.get_rect()
        self.rect.center = position


EXIT_BUTTON = ["Images/exit_button_inactive.png", "Images/exit_button_active.png"]


class ExitButtonSprite(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.image = pygame.image.load(EXIT_BUTTON[0]).convert_alpha()
        self.image = pygame.transform.scale(self.image,
                                            [int(dimension / BUTTON_SCALE) for dimension in self.image.get_size()])
        self.rect = self.image.get_rect()
        self.rect.center = (int(screen_width / 2), int(screen_height / 1.5))

    def set_state(self, state):
        position = self.rect.center
        self.image = pygame.image.load(EXIT_BUTTON[state]).convert_alpha()
        self.image = pygame.transform.scale(self.image,
                                            [int(dimension / BUTTON_SCALE) for dimension in self.image.get_size()])
        self.rect = self.image.get_rect()
        self.rect.center = position





