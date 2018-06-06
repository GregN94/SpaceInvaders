import pygame
from utils import WaitTimer
from States.play_state import PlayState
from States.menu_state import MenuState, States
from States.additional_states import Pause, BasicState, WinState, WonLevel

SCREEN = (1000, 600)
FIRST_LEVEL = 1


class Game:
    def __init__(self):
        pygame.mixer.pre_init(44100, -16, 3, 512)
        pygame.init()
        pygame.mixer.init()
        self.level = FIRST_LEVEL
        self.EXIT = False
        self.screen = pygame.display.set_mode(SCREEN)
        self.clock = pygame.time.Clock()
        self.win_state = WinState(SCREEN)
        self.pause_state = Pause(SCREEN)
        self.menu_state = MenuState(SCREEN)
        self.won_level_state = WonLevel(SCREEN)
        self.game_over_state = BasicState(SCREEN, "Images/game_over.png", States.GAME_OVER)
        self.timer = WaitTimer()
        self.play_state = PlayState(SCREEN, self.level, self.timer)
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

    def print_wait(self):
        font = pygame.font.Font(None, 48)
        text = font.render("Wait", True, (255, 255, 255))
        if self.timer.is_running:
            self.screen.blit(text,
                             (SCREEN[0] / 2 - text.get_width() / 2,
                              SCREEN[1] / 2 - text.get_height() / 2))

    def print_level(self):
        font = pygame.font.Font(None, 48)
        text = font.render("Level: " + str(self.level), True, (255, 255, 255))
        self.screen.blit(text,
                         (SCREEN[0] - text.get_width() - 10, 10))

    def exit(self):
        self.EXIT = True

    def game(self):
        self.state = self.play_state.update()
        self.play_state.draw(self.screen)
        self.timer.update()
        self.print_level()
        self.print_wait()

    def menu(self):
        self.state = self.menu_state.update()
        self.menu_state.draw(self.screen)

    def pause(self):
        self.play_state.draw(self.screen)
        self.state = self.pause_state.update()
        self.pause_state.draw(self.screen)

    def retry(self):
        self.level = FIRST_LEVEL
        self.play_state = PlayState(SCREEN, self.level, self.timer)
        self.state = States.GAME

    def victory(self):
        self.play_state.draw(self.screen)
        self.state = self.win_state.update()
        self.win_state.draw(self.screen)

    def game_over(self):
        self.play_state.animation()
        self.play_state.draw(self.screen)
        self.state = self.game_over_state.update()
        self.game_over_state.draw(self.screen)

    def won_level(self):
        self.play_state.animation()
        self.play_state.draw(self.screen)
        self.state = self.won_level_state.update()
        self.won_level_state.draw(self.screen)

    def go_to_menu(self):
        self.level = FIRST_LEVEL
        self.play_state = PlayState(SCREEN, self.level, self.timer)
        self.state = States.MENU

    def next_level(self):
        self.level += 1
        self.play_state = PlayState(SCREEN, self.level, self.timer)
        self.state = States.GAME

    def main(self):

        pygame.mixer.music.load("Sounds/background_music")
        pygame.mixer.music.play(-1)

        do_state = {States.EXIT:        self.exit,
                    States.GAME:        self.game,
                    States.MENU:        self.menu,
                    States.PAUSE:       self.pause,
                    States.RETRY:       self.retry,
                    States.VICTORY:     self.victory,
                    States.GAME_OVER:   self.game_over,
                    States.WON_LEVEL:   self.won_level,
                    States.GO_TO_MENU:  self.go_to_menu,
                    States.NEXT_LEVEL:  self.next_level}

        while not self.EXIT:

            self.screen.fill((0, 0, 0))
            self.basic_input()

            do_state[self.state]()
            pygame.display.update()
            self.clock.tick(60)


game = Game()
game.main()
pygame.quit()
quit()
