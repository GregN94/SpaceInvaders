import pygame

BUTTON_SCALE = 2
START_BUTTONS = ["Images/Buttons/start_button_inactive.png", "Images/Buttons/start_button_active.png"]
EXIT_BUTTONS = ["Images/Buttons/exit_button_inactive.png", "Images/Buttons/exit_button_active.png"]
RESUME_BUTTONS = ["Images/Buttons/resume_button_inactive.png", "Images/Buttons/resume_button_active.png"]
RETRY_BUTTONS =  ["Images/Buttons/retry_button_inactive.png", "Images/Buttons/retry_button_active.png"]


class Button(pygame.sprite.Sprite):
    def __init__(self, images, x, y):
        super().__init__()
        self.images = images
        self.image = pygame.image.load(images[0])
        self.image = pygame.transform.scale(self.image,
                                            [int(dimension / BUTTON_SCALE) for dimension in self.image.get_size()])
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def set_state(self, state):
        position = self.rect.center
        self.image = pygame.image.load(self.images[state])
        self.image = pygame.transform.scale(self.image,
                                            [int(dimension / BUTTON_SCALE) for dimension in self.image.get_size()])
        self.rect = self.image.get_rect()
        self.rect.center = position


class StartButtonSprite(Button):
    def __init__(self, screen_width, screen_height):
        super().__init__(START_BUTTONS, int(screen_width / 2), int(screen_height / 2))


class ExitButtonSprite(Button):
    def __init__(self, screen_width, screen_height):
        super().__init__(EXIT_BUTTONS, int(screen_width / 2), int(screen_height / 1.5))


class ResumeButton(Button):
    def __init__(self, screen_width, screen_height):
        super().__init__(RESUME_BUTTONS, 0, 0)
        self.rect.center = (int(screen_width / 2), int(screen_height / 2) - 2 * self.image.get_height())


class RetryButton(Button):
    def __init__(self, screen_width, screen_height):
        super().__init__(RETRY_BUTTONS, 0, 0)
        self.rect.center = (int(screen_width / 2), int(screen_height / 2) - 0.5 * self.image.get_height())




