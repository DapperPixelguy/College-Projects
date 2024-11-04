import pygame
from random import *
from copy import deepcopy

resolution = WIDTH, HEIGHT = 800, 800
cell = 25
W, H = WIDTH // cell, HEIGHT // cell
FPS = 15

pygame.init()
window = pygame.display.set_mode(resolution)
clock = pygame.time.Clock()

next = [[0 for i in range (W)] for j in range(H)]
current = [[randint(0,1) for i in range (W)] for j in range(H)]

active = True

def check_cell(current, x, y):
    c = 0
    for j in range(y-1, y+2):
        for i in range(x-1, x+2):
            if current[j][i]:
                c +=1

    if current[y][x]:
        c -= 1
        if c == 2 or c == 3:
            return 1
    else:
        if c == 3:
            return 1
        return 0


while active:

    window.fill(color=(0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    [pygame.draw.line(window, (55,55,55), (x, 0), (x, HEIGHT)) for x in range(0, WIDTH, cell)]
    [pygame.draw.line(window, (55, 55, 55), (0, y), (WIDTH, y)) for y in range(0, HEIGHT, cell)]

    for x in range(1, W-1):
        for y in range(1, H-1):
            if current[y][x]:
                pygame.draw.rect(window, (55, 0, 150), (x*cell + 2, y*cell + 2, cell - 2, cell - 2))


    pygame.display.flip()
    clock.tick(FPS)