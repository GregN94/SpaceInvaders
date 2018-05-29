import pygame
from play_state import PlayState
from menu_state import MenuState, States
from pause_state import Pause

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
        self.pause_state = Pause(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.state = States.MENU

    def execute_basic_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.QUIT = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    if self.state == States.PAUSE:
                        self.state = States.GAME
                    elif self.state == States.GAME:
                        self.state = States.PAUSE

    def main(self):
        while not self.QUIT:
            self.screen.fill((0, 0, 0))
            self.execute_basic_input()

            if self.state == States.PAUSE:
                self.play_state.draw(self.screen)
                self.pause_state.draw(self.screen)

            if self.state == States.GAME:
                self.play_state.play()
                self.play_state.draw(self.screen)

            if self.state == States.MENU:
                self.state = self.menu_state.menu()
                self.menu_state.draw(self.screen)
            if self.state == States.EXIT:
                self.QUIT = True

            pygame.display.update()
            self.clock.tick(60)


game = Game()
game.main()
