import pygame
from play_state import PlayState
from menu_state import MenuState, States

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

    def check_if_game_quited(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.QUIT = True

    def main(self):
        state = States.MENU
        while not self.QUIT:

            self.screen.fill((0, 0, 0))
            self.check_if_game_quited()

            if state == States.GAME:
                self.play_state.play()
                self.play_state.draw(self.screen)
            if state == States.MENU:
                state = self.menu_state.menu()
                self.menu_state.draw(self.screen)
            if state == States.EXIT:
                self.QUIT = True
            pygame.display.update()
            self.clock.tick(60)


game = Game()
game.main()
