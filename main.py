from random import randint
from math import floor
import pygame
from pymata.automata import Automata

CELL_SIZE = 5
X_CELLS = 120
Y_CELLS = 120

frame_rate = 10

pygame.init()
pygame.display.set_caption("Game of Life")
window = pygame.display.set_mode((X_CELLS * CELL_SIZE, Y_CELLS * CELL_SIZE))
clock = pygame.time.Clock()

at = Automata.from_size(X_CELLS, Y_CELLS)

for _ in range(1000):
    at.set(randint(0, X_CELLS - 1), randint(0, Y_CELLS - 1), 1)

RUNNING = True
IS_PRESSING = False

while RUNNING:
    window.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            raise SystemExit

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                frame_rate = frame_rate + 1

            if event.key == pygame.K_DOWN:
                frame_rate = frame_rate - 1

        if event.type == pygame.MOUSEBUTTONDOWN:
            IS_PRESSING = True

        if event.type == pygame.MOUSEMOTION and IS_PRESSING:
            pos = event.pos
            col = floor(pos[0]/CELL_SIZE)
            row = floor(pos[1]/CELL_SIZE)
            at.set(row, col, 1)

        if event.type == pygame.MOUSEBUTTONUP:
            IS_PRESSING = False

    if not IS_PRESSING:
        at.transition()

    cur_matrix = at.get_matrix()
    for idx_y, y_val in enumerate(cur_matrix):
        for idx_x, x_val in enumerate(y_val):
            if x_val == 1:
                pygame.draw.rect(
                    window,
                    (0, 255, 0),
                    (idx_x * CELL_SIZE, idx_y * CELL_SIZE, CELL_SIZE, CELL_SIZE),
                )

    pygame.display.update()
    clock.tick(frame_rate)

pygame.quit()
