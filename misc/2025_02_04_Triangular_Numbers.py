from itertools import count

def tri(num=1, step=1, display=False, max_iter=100):
    if step < max_iter:
        if display:
            print(num)
            print_tri(step)
            print('-' * step*2)
        else:
            print(num)
        tri(num+(step+1), step+1, display=display, max_iter=max_iter)

def print_tri(step):
    triangle = []
    for i in range(1, step+1):
        print(' '*(step-i), end='')
        print('# '*i)
        triangle.append((step-i, i))

    return triangle

tri(display=True)

import pygame

pygame.init()
resolution = WIDTH, HEIGHT = 800,800
screen = pygame.display.set_mode(resolution)
size = 25

def draw_tri(step):
    triangle = []
    for i in range(1, step+1):
        # print(' '*(step-i), end='')
        # print('# '*i)
        triangle.append((step-i, i))
        for j in range(1,i+1):
            pygame.draw.rect(screen, (255,255,255), ((step-j)*size, i*size, size*i, size))
    # print(triangle)

running = True

clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    draw_tri(16)
    pygame.display.flip()
    clock.tick(60)