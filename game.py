import pygame
from play_state import PlayState
from menu_state import MenuState

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600


class Game:
    def __init__(self):
        pygame.init()
        self.QUIT = False
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.play_state = PlayState(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.play_state.generate_enemies()
        self.menu_state = MenuState(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.start = False

    def check_if_game_quited(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.QUIT = True

    def main(self):
        while not self.QUIT:

            self.screen.fill((0, 0, 0))
            self.check_if_game_quited()

            if self.start:
                self.play_state.play()
                self.play_state.draw(self.screen)
            else:
                self.menu_state.draw(self.screen)
                self.start = self.menu_state.menu()
            pygame.display.update()
            self.clock.tick(60)


game = Game()
game.main()
