import pygame
from play_state import PlayState

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


class Game:
    def __init__(self):
        pygame.init()
        self.QUIT = False
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.play_state = PlayState(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.play_state.generate_enemies()

    def check_if_game_quited(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.QUIT = True

    def main(self):
        while not self.QUIT:

            self.screen.fill((0, 0, 0))
            self.check_if_game_quited()

            self.play_state.play()
            self.play_state.draw(self.screen)
            pygame.display.update()
            self.clock.tick(60)


game = Game()
game.main()
