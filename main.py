from random import randint
from pymata.automata import Automata
import pygame

X = 120
Y = 120

cell_size = 5
x_cells = 120
y_cells = 120

pygame.init()
window = pygame.display.set_mode((x_cells * cell_size, y_cells * cell_size))
clock = pygame.time.Clock()

at = Automata.from_size(x_cells, y_cells)

for X in range(100):
    at.set(randint(0, x_cells - 1), randint(0, y_cells - 1), 1)

RUNNING = True

while RUNNING:
    window.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
            break

        if event.type == pygame.MOUSEBUTTONUP:
            pos = event.pos
            print(pos)

    at.transition()
    cur_matrix = at.get_matrix()
    for idx_y, Y in enumerate(cur_matrix):
        for idx_x, X in enumerate(Y):
            # apply_rules(cells, x, y)

            if X == 1:
                pygame.draw.rect(
                    window,
                    (0, 0, 255),
                    (idx_x * cell_size, idx_y * cell_size, cell_size, cell_size),
                )

    pygame.display.update()
    clock.tick(30)

pygame.quit()
