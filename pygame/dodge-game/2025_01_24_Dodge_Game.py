import pygame
import sys
import random
import threading
import time

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Dodge game')

GREEN = (50, 168, 82)

clock = pygame.time.Clock()

player_width, player_height = 50, 50
player_x = WIDTH // 2
player_y = HEIGHT - 2 * player_height
player_speed = 7
player_colour = (200,0,255)
lives = 3
immune = False

obstacle_width, obstacle_height = 50, 50
obstacle_x = random.randint(0, WIDTH-obstacle_width)
obstacle_y = -obstacle_height
obstacle_speed = 6

bullet_width, bullet_height = 10, 50
bullet_speed = -15


score = 0
ob_count = 1
count = 0
font = pygame.font.Font(None, 36)

obstacles = [[random.randint(0, WIDTH - obstacle_width), random.randint(-obstacle_height-obstacle_height, -obstacle_height+obstacle_height)] for i in range(ob_count)]

bullets = []

def score_check(score):
    global ob_count,obstacle_speed
    if score % 5 == 0:
        ob_count += 1
        obstacle_speed += 0.1

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                paused = True
                while paused:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            sys.exit()
                        elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE:
                                paused = False

            if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                if len(bullets) < 2:
                    bullets.append([(player_x+player_width/2)-bullet_width/2, player_y - player_height - 10, bullet_width, bullet_height])

    screen.fill((0,0,0))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] or keys[pygame.K_a] and player_x > 0:
        player_x -= player_speed

    if keys[pygame.K_RIGHT] or keys[pygame.K_d] and  player_x < WIDTH-player_width:
        player_x += player_speed


    if len(obstacles) < ob_count:
        for i in range(ob_count-len(obstacles)):
            obstacles.append([random.randint(0, WIDTH - obstacle_width), random.randint(-obstacle_height-obstacle_height, -obstacle_height+obstacle_height)])

    for obstacle in obstacles:
        obstacle[1] += obstacle_speed

        for bullet in bullets:
            if bullet:
                if (bullet[0] < obstacle[0] + obstacle_width
                    and bullet[0] + bullet_width > obstacle[0]
                    and bullet[1] < obstacle[1] + obstacle_height
                    and bullet[1] + bullet_height > obstacle[1]):
                        obstacle[1], obstacle[0] = random.randint(-obstacle_height-obstacle_height, -obstacle_height+obstacle_height), random.randint(0,WIDTH-obstacle_width)
                        bullets.remove(bullet)
                        score += 1
                        score_check(score)

        if obstacle[1] > HEIGHT:
            obstacle[1] = random.randint(-obstacle_height-obstacle_height, -obstacle_height+obstacle_height)
            obstacle[0] = random.randint(0,WIDTH-obstacle_width)
            count += 1
            if count == ob_count:
                score += 1
                count = 0
                score_check(score)

        if (player_x < obstacle[0] + obstacle_width
            and player_x + player_width > obstacle[0]
            and player_y < obstacle[1] + obstacle_height
            and player_y + player_height > obstacle[1]):

            if not immune:
                lives -= 1
                immune = True
                threading.Timer(3, lambda: globals().__setitem__('immune', False)).start()

            if lives <= 0:
                x = None
                j=0
                print(f"Game Over, your score was: {score}")
                if int(score) > int(highscore):
                    with open('highscore.txt', 'w') as f:
                        f.write(str(score))
                threading.Timer(1, lambda: globals().__setitem__('x', 1)).start()
                while True:
                    screen.fill((0,0,0))
                    if not x:
                        pygame.draw.rect(screen, (200, 0, 255), (player_x, player_y, player_width, player_height))

                    if x == 1:
                        if player_colour == (200,0,255):
                            pygame.draw.rect(screen, (105,105,105), (player_x, player_y, player_width, player_height))
                            player_colour = (105,105,105)

                        elif player_colour == (105,105,105):
                            pygame.draw.rect(screen, (200,0,255), (player_x, player_y, player_width, player_height))
                            player_colour = (200,0,255)

                        threading.Timer(2, lambda: globals().__setitem__('x', 2)).start()

                    elif x == 2:
                        pygame.draw.rect(screen, (105, 105, 105), (player_x, player_y, player_width, player_height))
                        if j == 0:
                            threading.Timer(0.5, lambda: globals().__setitem__('j', 1)).start()
                        if j == 1:
                            break

                    clock.tick(3)
                    pygame.display.flip()

                running = False
                pygame.quit()
                sys.exit()

        pygame.draw.rect(screen, (255, 255, 255), (obstacle[0], obstacle[1], obstacle_width, obstacle_height))



    def remove_bullet(bullet):
        bullets.remove(bullet)

    if len(bullets) < 2:
        if len(bullets) == 0:
            screen.blit(font.render('| |', True, (0,0,255)), (WIDTH-50,50))
        else:
            screen.blit(font.render('|', True, (0,0,255)), (WIDTH-50,50))

    for bullet in bullets:
        if bullet:
            if bullet[1] < 0:
                bullets.remove(bullet)
                bullets.append(None)
                timeout = 3
                threading.Timer(timeout, lambda: remove_bullet(None)).start()

            #d print(bullet)
            pygame.draw.rect(screen, (255, 255, 255), (bullet[0], bullet[1], bullet_width, bullet_height))
            bullet[1] += bullet_speed


    if not immune:
        pygame.draw.rect(screen, (200,0,255), (player_x, player_y, player_width, player_height))
    if immune:
        pygame.draw.rect(screen, (255, 0, 0), (player_x, player_y, player_width, player_height))
    with open ('highscore.txt', 'r') as f:
        highscore = f.read()
    score_text = font.render(f'Score: {score}       High Score: {highscore.strip()}', True, (0,0,255))
    ammo_text = font.render(f'Ammo', True, (0,0,255))
    lives_text = font.render(f'Lives: {lives}', False, (0,0,255))
    screen.blit(ammo_text, (WIDTH-100, 10))
    screen.blit(score_text, (10,10))
    screen.blit(lives_text, (10,50))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()


