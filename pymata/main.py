from itertools import count
from random import randint, random
import pygame

x = 120
y = 120

cell_size = 5
x_cells = 120
y_cells = 120

pygame.init()
window = pygame.display.set_mode((x_cells * cell_size, y_cells * cell_size))
clock = pygame.time.Clock()

cells = [[0 for x in range(y_cells)] for x in range(x_cells)]

for x in range(100):
    cells[randint(0, x_cells - 1)][randint(0, y_cells - 1)] = 1

running = True

while running:
    window.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    for idx_y, y in enumerate(cells):
        for idx_x, x in enumerate(y):
            apply_rules(cells, x, y)

            if x == 1:
                pygame.draw.rect(
                    window,
                    (0, 0, 255),
                    (idx_x * cell_size, idx_y * cell_size, cell_size, cell_size),
                )

    pygame.display.update()
    clock.tick(30)

pygame.quit()


def count_neighbors(cells, x, y):
    count = 0

    if y > 0:
        count += cells[x][y - 1]

    if y < len(cells):
        count += cells[x][y + 1]

    if x > 0:
        count += cells[x - 1][y]

        if y > 0:
            count += cells[x - 1][y - 1]

        if y < len(cells):
            count += cells[x - 1][y + 1]

    if x < len(cells[y]):
        count += cells[x + 1][y]

        if y > 0:
            count += cells[x + 1][y - 1]

        if y < len(cells):
            count += cells[x + 1][y + 1]


def apply_rules(cells, x, y):
    neighbors = count_neighbors(cells, x, y)
    if cells[x][y] == 0 and neighbors == 3:
        cells[x][y] = 1

    if cells[x][y] == 1:
        if neighbors > 1 or neighbors < 4:
            cells[x][y] = 0
        else:
            cells[x][y] = 1
    else:
        if neighbors == 3:
            cells[x][y] = 1
