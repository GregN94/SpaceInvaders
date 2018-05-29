import pygame
from pause_sprites import Background, PausePanel, PauseLogo
from menu_sprites import ExitButtonSprite
from menu_state import States


class Pause:
    def __init__(self, screen_width, screen_height):
        self.background = Background(screen_width, screen_height)
        self.pause_panel = PausePanel(screen_width, screen_height)
        self.pause_logo = PauseLogo(screen_width, screen_height)
        self.exit_button = ExitButtonSprite(screen_width, screen_height)

        self.background_sprites_list = pygame.sprite.Group()
        self.background_sprites_list.add(self.background)

        self.panel_sprite_list = pygame.sprite.Group()
        self.panel_sprite_list.add(self.pause_panel)

        self.pause_sprite_list = pygame.sprite.Group()
        self.pause_sprite_list.add(self.pause_logo, self.exit_button)
        self.new_state = States.PAUSE

    def update(self):
        mouse_position = pygame.mouse.get_pos()
        pressed = pygame.mouse.get_pressed()

        self.exit_button.set_state(0)

        if self.exit_button.rect.collidepoint(mouse_position):
            if pressed[0]:
                self.new_state = States.EXIT
            self.exit_button.set_state(1)

        self.pause_sprite_list.update()
        return self.new_state

    def draw(self, screen):
        self.background_sprites_list.draw(screen)
        self.panel_sprite_list.draw(screen)
        self.pause_sprite_list.draw(screen)


