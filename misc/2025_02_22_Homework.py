import pygame
import json
import numpy as np
import textwrap

with open('data/Homework_Data.json', 'r') as f:
    data = json.load(f)

for _item in data:
    for item in _item:
        print(f'{item}: {_item[item]}')
    print()

RESOLUTION = WIDTH, HEIGHT = 1000, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.init()
clock = pygame.time.Clock()
surfaces = []

def gen(ans):
    _ans = iter(ans)
    x= []
    for i in np.linspace(50, 900, len(ans)):
        x.append([next(_ans), [int(i), 50]])

    for answer in x:
        surface = pygame.Surface((110, 110))
        surface.fill((255, 0, 0))

        pygame.draw.rect(surface, (255, 255, 255), (0, 0, 110, 110))
        answer_text = textwrap.wrap(answer[0], 10)

        for i, line in enumerate(answer_text):
            surface.blit(ans_font.render(line, True, (0,0,0)), (0, 25*i))

        surfaces.append((surface, (answer[1][0]-50/2, answer[1][1]), answer[0]))

    return x



q_count = 0
font = pygame.font.Font(None, 36)
ans_font = pygame.font.Font(None, 25  )
question = data[q_count]['Question']
answers = data[q_count]['Answers']
correct = data[q_count]['Correct']

ans = gen(answers)

controller_width, controller_height = 50, 50
controller_speed = 7
controller = pygame.Rect(WIDTH/2-controller_width/2, HEIGHT-100, controller_width, controller_height)



bullet = None
bullet_width = 10


print(f'QUESTION {q_count+1}\nQuestion: {question}\nAnswers: {answers}\nCorrect: {correct}')

Active = True
while Active:
    question = data[q_count]['Question']
    answers = data[q_count]['Answers']
    correct = data[q_count]['Correct']
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Active = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if not bullet:
                    bullet = pygame.Rect(controller.x+controller.width//2-bullet_width//2, controller.y-controller.height-10, bullet_width, 50)


    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        if controller.x >0:
            controller.x -= 7
    if keys[pygame.K_RIGHT]:
        if controller.x < WIDTH-controller.width:
            controller.x += 7

    if bullet:
        pygame.draw.rect(screen, (255, 255, 255), bullet)

        for surface, position, answer_text in surfaces:
            surface_rect = surface.get_rect(topleft=position)

            if bullet.colliderect(surface_rect):
                print(f'{answer_text}')
                if answer_text == correct:
                    print('correct')
                    if q_count + 1 >= len(data):
                        pygame.quit()
                        print('Quiz over')
                        quit()
                    else:
                        q_count += 1
                bullet = None
                break

        if bullet:
            bullet.y -= 15
            if bullet.y < 0-50:
                bullet = None

    screen.blit(font.render(question, True, (255,255,255)), ((WIDTH/2)-font.size(question)[0]/2, 10))

    for surface in surfaces:
        screen.blit(surface[0], (surface[1][0], surface[1][1]))

    pygame.draw.rect(screen, (255,255,255), controller)

    pygame.display.flip()
    clock.tick(60)
    surfaces = []
    gen(answers)

