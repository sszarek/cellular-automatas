from random import randint
import pygame
from math import floor
from .configuration import Configuration
from pycells.automata import Automata

class Application:
    _config: Configuration
    _clock: pygame.time.Clock
    _automata: Automata
    _is_pressing: bool = False
    _frame_rate: int = 10

    def __init__(self, config: Configuration) -> None:
        self._config = config

        self._clock = pygame.time.Clock()
        self._automata = Automata.from_size(self._config.rows, self._config.cols)
        self._frame_rate = self._config.frame_rate
    
    def _fill_random_cells(self):
        rows = self._config.rows
        cols = self._config.cols

        for _ in range(1000):
            self._automata.set(randint(0, cols - 1), randint(0, rows - 1), 1)

    def on_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self._frame_rate = self._frame_rate + 1

                if event.key == pygame.K_DOWN:
                    self._frame_rate = self._frame_rate - 1

                if event.key == pygame.K_r:
                    self._fill_random_cells()

            if event.type == pygame.MOUSEBUTTONDOWN:
                self._is_pressing = True

            if event.type == pygame.MOUSEMOTION and self._is_pressing:
                pos = event.pos
                col = floor(pos[0] / self._config.cell_size)
                row = floor(pos[1] / self._config.cell_size)
                self._automata.set(row, col, 1)

            if event.type == pygame.MOUSEBUTTONUP:
                self._is_pressing = False

    def on_render(self, window: pygame.Surface):
        cur_matrix = self._automata.get_matrix()
        config = self._config
        
        for idx_y, y_val in enumerate(cur_matrix):
            for idx_x, x_val in enumerate(y_val):
                if x_val == 1:
                    pygame.draw.rect(
                        window,
                        (0, 255, 0),
                        (idx_x * config.cell_size, idx_y * config.cell_size, config.cell_size, config.cell_size),
                    )

    def run(self):
        config = self._config

        pygame.init()
        pygame.display.set_caption(config.window_caption)
        window = pygame.display.set_mode(
            (config.cols * config.cell_size, config.rows * config.cell_size)
        )

        while True:
            window.fill((0, 0, 0))

            self.on_event()

            if not self._is_pressing:
                self._automata.transition()

            self.on_render(window)

            pygame.display.update()
            self._clock.tick(self._frame_rate)
