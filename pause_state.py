import pygame
from pause_sprites import Background, PausePanel, PauseLogo, ResumeButton
from menu_sprites import ExitButtonSprite
from menu_state import States

INACTIVE = 0
ACTIVE = 1


class Pause:
    def __init__(self, screen_width, screen_height):
        self.background = Background(screen_width, screen_height)
        self.pause_panel = PausePanel(screen_width, screen_height)
        self.pause_logo = PauseLogo(screen_width, screen_height)
        self.resume_button = ResumeButton(screen_width, screen_height)
        self.exit_button = ExitButtonSprite(screen_width, screen_height)

        self.background_sprites_list = pygame.sprite.Group()
        self.background_sprites_list.add(self.background)

        self.panel_sprite_list = pygame.sprite.Group()
        self.panel_sprite_list.add(self.pause_panel)

        self.buttons_sprite_list = pygame.sprite.Group()
        self.buttons_sprite_list.add(self.pause_logo, self.exit_button, self.resume_button)

    def update(self):
        new_state = States.PAUSE
        mouse_position = pygame.mouse.get_pos()
        pressed = pygame.mouse.get_pressed()

        self.exit_button.set_state(INACTIVE)
        self.resume_button.set_state(INACTIVE)

        if self.exit_button.rect.collidepoint(mouse_position):
            if pressed[0]:
                new_state = States.EXIT
            self.exit_button.set_state(ACTIVE)

        if self.resume_button.rect.collidepoint(mouse_position):
            if pressed[0]:
                new_state = States.GAME
            self.resume_button.set_state(ACTIVE)

        self.buttons_sprite_list.update()
        return new_state

    def draw(self, screen):
        self.background_sprites_list.draw(screen)
        self.panel_sprite_list.draw(screen)
        self.buttons_sprite_list.draw(screen)


