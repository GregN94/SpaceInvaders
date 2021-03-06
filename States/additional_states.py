import pygame
import utils
from buttons import ExitButton, ResumeButton, RetryButton, GoToMenuButton, NextLevelButton
from States.menu_state import States

BLACK = (0, 0, 0)
PANEL_SCALE = 3
SCALE = 2
WON_IMAGES = ["Images/won_inactive.png", "Images/won_active.png"]


class Background(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.image = pygame.Surface(screen)
        self.image.fill(BLACK)
        self.image.set_alpha(128)
        self.rect = self.image.get_rect()


class PausePanel(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.image = utils.load_and_scale("Images/pause_panel.png", PANEL_SCALE)
        self.rect = self.image.get_rect()
        self.rect.center = (int(screen[0] / 2), int(screen[1] / 2))


class Logo(pygame.sprite.Sprite):
    def __init__(self, screen, image):
        super().__init__()
        self.image = utils.load_and_scale(image, SCALE)
        self.rect = self.image.get_rect()
        self.rect.center = (int(screen[0] / 2), int(screen[1]/ 2) - 3 * self.image.get_height())
        self.state = 1

    def toggle(self, images):
        if self.state == 1:
            self.state = 0
        else:
            self.state = 1
        position = self.rect.center
        self.image = utils.load_and_scale(images[self.state], SCALE)
        self.rect = self.image.get_rect()
        self.rect.center = position


class BasicState:
    def __init__(self, screen, image, state):
        self.logo = Logo(screen, image)
        self.retry_button = RetryButton(screen)
        self.go_to_menu_button = GoToMenuButton(screen)
        self.exit_button = ExitButton(screen)

        self.background_sprites_list = pygame.sprite.Group()
        self.background_sprites_list.add(Background(screen))

        self.panel_sprite_list = pygame.sprite.Group()
        self.panel_sprite_list.add(PausePanel(screen))

        self.buttons_sprite_list = pygame.sprite.Group()
        self.buttons_sprite_list.add(self.logo,
                                     self.exit_button,
                                     self.retry_button,
                                     self.go_to_menu_button)
        self.init_state = state
        self.new_state = self.init_state

    def draw(self, screen):
        self.background_sprites_list.draw(screen)
        self.panel_sprite_list.draw(screen)
        self.buttons_sprite_list.draw(screen)

    def update(self):
        self.new_state = self.init_state
        if self.exit_button.check():
            self.new_state = States.EXIT

        if self.retry_button.check():
            pygame.mixer.music.load("Sounds/background_music")
            pygame.mixer.music.play(-1)
            self.new_state = States.RETRY

        if self.go_to_menu_button.check():
            pygame.mixer.music.load("Sounds/background_music")
            pygame.mixer.music.play(-1)
            self.new_state = States.GO_TO_MENU

        self.buttons_sprite_list.update()
        return self.new_state


class Pause(BasicState):
    def __init__(self, screen):
        super().__init__(screen, "Images/pause_logo.png", States.PAUSE)
        self.resume_button = ResumeButton(screen)
        self.buttons_sprite_list.add(self.resume_button)

    def update(self):
        super().update()
        if self.resume_button.check():
            self.new_state = States.GAME

        self.buttons_sprite_list.update()
        return self.new_state


class WonLevel(BasicState):
    def __init__(self, screen):
        super().__init__(screen, "Images/level_finished.png", States.WON_LEVEL)
        self.next_level_button = NextLevelButton(screen)
        self.buttons_sprite_list.add(self.next_level_button)

    def update(self):
        super().update()
        if self.next_level_button.check():
            self.new_state = States.NEXT_LEVEL

        self.buttons_sprite_list.update()
        return self.new_state


class WinState(BasicState):
    def __init__(self, screen):
        super().__init__(screen, WON_IMAGES[0], States.VICTORY)

    def update(self):
        self.logo.toggle(WON_IMAGES)
        super().update()

        self.buttons_sprite_list.update()
        return self.new_state






