import pygame
from States.play_state import PlayState
from States.menu_state import MenuState, States
from States.pause_state import Pause

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600


class Game:
    def __init__(self):
        pygame.init()
        self.EXIT = False
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.play_state = PlayState(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.play_state.generate_enemies()
        self.menu_state = MenuState(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.pause_state = Pause(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.state = States.MENU

    def basic_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.EXIT = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    if self.state == States.PAUSE:
                        self.state = States.GAME
                    elif self.state == States.GAME:
                        self.state = States.PAUSE

    def state_pause(self):
        self.play_state.draw(self.screen)
        self.state = self.pause_state.update()
        self.pause_state.draw(self.screen)

    def state_game(self):
        self.play_state.play()
        self.play_state.draw(self.screen)

    def state_menu(self):
        self.state = self.menu_state.menu()
        self.menu_state.draw(self.screen)

    def main(self):
        while not self.EXIT:

            self.screen.fill((0, 0, 0))
            self.basic_input()

            if self.state == States.PAUSE:
                self.state_pause()

            if self.state == States.GAME:
                self.state_game()

            if self.state == States.MENU:
                self.state_menu()

            if self.state == States.EXIT:
                self.EXIT = True

            pygame.display.update()
            self.clock.tick(60)


game = Game()
game.main()
