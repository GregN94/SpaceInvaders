import pygame
from States.play_state import PlayState
from States.menu_state import MenuState, States
from States.additional_states import Pause, GameOver, WinState

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600


class Game:
    def __init__(self):
        pygame.mixer.pre_init(44100, -16, 3, 512)
        pygame.init()
        pygame.mixer.init()
        self.EXIT = False
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.play_state = PlayState(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.menu_state = MenuState(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.pause_state = Pause(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.game_over_state = GameOver(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.win_state = WinState(SCREEN_WIDTH, SCREEN_HEIGHT)
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

    def pause(self):
        self.play_state.draw(self.screen)
        self.state = self.pause_state.update()
        self.pause_state.draw(self.screen)

    def game(self):
        self.state = self.play_state.update()
        self.play_state.draw(self.screen)

    def menu(self):
        self.state = self.menu_state.update()
        self.menu_state.draw(self.screen)

    def retry(self):
        self.play_state = PlayState(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.state = States.GAME

    def go_to_menu(self):
        self.play_state = PlayState(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.state = States.MENU

    def game_over(self):
        self.play_state.animation()
        self.play_state.draw(self.screen)
        self.state = self.game_over_state.update()
        self.game_over_state.draw(self.screen)

    def victory(self):
        self.play_state.draw(self.screen)
        self.state = self.win_state.update()
        self.win_state.draw(self.screen)

    def exit(self):
        self.EXIT = True

    def main(self):

        pygame.mixer.music.load("Sounds/background_music")
        pygame.mixer.music.play(-1)

        do_state = {States.PAUSE: self.pause,
                    States.GAME: self.game,
                    States.MENU: self.menu,
                    States.RETRY: self.retry,
                    States.GO_TO_MENU: self.go_to_menu,
                    States.GAME_OVER: self.game_over,
                    States.WIN: self.victory,
                    States.EXIT: self.exit}

        while not self.EXIT:

            self.screen.fill((0, 0, 0))
            self.basic_input()

            do_state[self.state]()

            pygame.display.update()
            self.clock.tick(60)


game = Game()
game.main()
