import pygame
import utils

INACTIVE = 0
ACTIVE = 1
BUTTON_SCALE = 2
OFFSET = 50

START_BUTTONS = ["Images/Buttons/start_button_inactive.png", "Images/Buttons/start_button_active.png"]
EXIT_BUTTONS = ["Images/Buttons/exit_button_inactive.png", "Images/Buttons/exit_button_active.png"]
RESUME_BUTTONS = ["Images/Buttons/resume_button_inactive.png", "Images/Buttons/resume_button_active.png"]
RETRY_BUTTONS = ["Images/Buttons/retry_button_inactive.png", "Images/Buttons/retry_button_active.png"]
GO_TO_MENU_BUTTONS = ["Images/Buttons/go_to_menu_inactive.png", "Images/Buttons/go_to_menu_active.png"]


class Button(pygame.sprite.Sprite):
    def __init__(self, images, x=0, y=0):
        super().__init__()
        self.images = images
        self.image = utils.load_and_scale(self.images[INACTIVE], BUTTON_SCALE)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def set_state(self, state):
        position = self.rect.center
        self.image = utils.load_and_scale(self.images[state], BUTTON_SCALE)
        self.rect = self.image.get_rect()
        self.rect.center = position

    def check(self):
        self.set_state(INACTIVE)
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.set_state(ACTIVE)
            pressed = pygame.mouse.get_pressed()
            return pressed[0]
        return False


class StartButtonSprite(Button):
    def __init__(self, screen_width, screen_height):
        super().__init__(START_BUTTONS, int(screen_width / 2), int(screen_height / 2))


class ExitButtonSprite(Button):
    def __init__(self, screen_width, screen_height):
        super().__init__(EXIT_BUTTONS, int(screen_width / 2), int(screen_height / 1.5))


class ResumeButton(Button):
    def __init__(self, screen_width, screen_height):
        super().__init__(RESUME_BUTTONS, int(screen_width / 2), int(screen_height / 1.5) - 3 * OFFSET)


class RetryButton(Button):
    def __init__(self, screen_width, screen_height):
        super().__init__(RETRY_BUTTONS, int(screen_width / 2), int(screen_height / 1.5) - 2 * OFFSET)


class GoToMenu(Button):
    def __init__(self, screen_width, screen_height):
        super().__init__(GO_TO_MENU_BUTTONS, int(screen_width / 2), int(screen_height / 1.5) - OFFSET)





