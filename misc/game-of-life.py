import pygame
from random import *
from copy import deepcopy

resolution = WIDTH, HEIGHT = 1500, 1000
cell = 20
W, H = WIDTH // cell, HEIGHT // cell
FPS = 15

pygame.init()
window = pygame.display.set_mode(resolution, pygame.SRCALPHA)
clock = pygame.time.Clock()

next = [[0 for i in range(W)] for j in range(H)]
current = [[randint(0, 1) for i in range (W)] for j in range(H)]

active = True
gameloop = True # Add a way to toggle this

def check_cell(current, x, y):
    c = 0
    for H in range(y-1, y+2):
        for W in range(x-1, x+2):
           c += current[H][W]

    if current[y][x]:
        c -= 1

    return c


def update_board():
    global current
    global next
    [pygame.draw.line(window, (55, 55, 55), (x, 0), (x, HEIGHT)) for x in range(0, WIDTH, cell)]
    [pygame.draw.line(window, (55, 55, 55), (0, y), (WIDTH, y)) for y in range(0, HEIGHT, cell)]

    for x in range(1, W - 1):
        for y in range(1, H - 1):
            neighbors = check_cell(current, x, y)

            if current[y][x] == 1:
                if neighbors == 2 or neighbors == 3:
                    next[y][x] = 1
                else:
                    next[y][x] = 0
            else:
                if neighbors == 3:
                    next[y][x] = 1

    current = [row[:] for row in next]

    for x in range(1, W - 1):
        for y in range(1, H - 1):
            if current[y][x]:
                pygame.draw.rect(window, (255, 255, 255), (x * cell + 2, y * cell + 2, cell - 2, cell - 2))

    print(current)

    pygame.display.flip()
while active:

    window.fill(color=(0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:  # Check for mouse click
            mouse_x, mouse_y = pygame.mouse.get_pos()
            grid_x, grid_y = mouse_x // cell, mouse_y // cell
            if 0 <= grid_x < W and 0 <= grid_y < H:
                # Toggle the cell state (alive <-> dead)
                current[grid_y][grid_x] = 1 - current[grid_y][grid_x]
                [pygame.draw.line(window, (55, 55, 55), (x, 0), (x, HEIGHT)) for x in range(0, WIDTH, cell)]
                [pygame.draw.line(window, (55, 55, 55), (0, y), (WIDTH, y)) for y in range(0, HEIGHT, cell)]

                for x in range(1, W - 1):
                    for y in range(1, H - 1):
                        if current[y][x]:
                            pygame.draw.rect(window, (255, 255, 255), (x * cell + 2, y * cell + 2, cell - 2, cell - 2))

                pygame.display.flip()

        elif event.type == pygame.KEYDOWN:
            update_board()


    if gameloop:
        update_board()
