import pygame
from pause_sprites import Background, PausePanel, PauseLogo


class Pause:
    def __init__(self, screen_width, screen_height):
        self.background = Background(screen_width, screen_height)
        self.pause_panel = PausePanel(screen_width, screen_height)
        self.pause_logo = PauseLogo(screen_width, screen_height)

        self.background_sprites_list = pygame.sprite.Group()
        self.background_sprites_list.add(self.background)

        self.panel_sprite_list = pygame.sprite.Group()
        self.panel_sprite_list.add(self.pause_panel)

        self.logo_sprite_list = pygame.sprite.Group()
        self.logo_sprite_list.add(self.pause_logo)

    def draw(self, screen):
        self.background_sprites_list.draw(screen)
        self.panel_sprite_list.draw(screen)
        self.logo_sprite_list.draw(screen)


