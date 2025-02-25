import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255,0,0)

# Paddle settings
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
PADDLE_SPEED = 7
rand_n = 0

# Ball settings
BALL_SIZE = 20
BALL_SPEED_X, BALL_SPEED_Y = 5, 5


# Paddle positions
left_paddle = pygame.Rect(30, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
right_paddle = pygame.Rect(WIDTH - 40, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

# Ball position
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    PREDICTION_END = [ball.x, ball.y]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and left_paddle.top > 0:
        left_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_s] and left_paddle.bottom < HEIGHT:
        left_paddle.y += PADDLE_SPEED
    # if keys[pygame.K_UP] and right_paddle.top > 0:
    #     right_paddle.y -= PADDLE_SPEED
    # if keys[pygame.K_DOWN] and right_paddle.bottom < HEIGHT:
    #     right_paddle.y += PADDLE_SPEED

    if ball.x > WIDTH//2 - 100 and BALL_SPEED_X > 0:
        if not rand_n:
            rand_n = random.uniform(0.2, 0.9)
            print(rand_n)
            rand_y = random.randint(25,100)
        if rand_n:
            indicator = pygame.Rect((right_paddle.x, right_paddle.y+PADDLE_HEIGHT*rand_n, PADDLE_WIDTH, BALL_SIZE))
        if right_paddle.y + PADDLE_HEIGHT*rand_n< ball.y - 50 and right_paddle.y + PADDLE_HEIGHT< HEIGHT:
            right_paddle.y += PADDLE_SPEED
        if right_paddle.y + PADDLE_HEIGHT * rand_n> ball.y + 50 and right_paddle.y >0:
            right_paddle.y -= PADDLE_SPEED
    else:
        rand_n = None
        rand_y = None

    # Ball movement
    ball.x += BALL_SPEED_X
    ball.y += BALL_SPEED_Y

    # Ball collision with top and bottom
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        BALL_SPEED_Y *= -1

    # Ball collision with paddles
    if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
        BALL_SPEED_X *= -1

    # Ball out of bounds
    if ball.left <= 0:
        ball.x, ball.y = WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2
        BALL_SPEED_X *= -1
        print('AI Scores')

    if ball.right >= WIDTH:
        ball.x, ball.y = WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2
        BALL_SPEED_X *= -1
        print('Player scores')

    screen.fill(BLACK)

    SPD_X, SPD_Y = BALL_SPEED_X, BALL_SPEED_Y
    # Prediction
    while True:
        PREDICTION_END[0] += SPD_X
        PREDICTION_END[1] += SPD_Y
        print(PREDICTION_END)
        if PREDICTION_END[1] <= 0 or PREDICTION_END[1] >= HEIGHT:
            SPD_Y *= -1
            pygame.draw.line(screen, RED, (ball.x, ball.y), (PREDICTION_END[0], PREDICTION_END[1]), 1)

            s1, s2 = PREDICTION_END[0], PREDICTION_END[1]

            while 0 < PREDICTION_END[0] < WIDTH:
                PREDICTION_END[0] += SPD_X
                PREDICTION_END[1] += SPD_Y
                if PREDICTION_END[0] <= 0 or PREDICTION_END[0] >= WIDTH:
                    pygame.draw.line(screen, RED, (s1, s2), (PREDICTION_END[0], PREDICTION_END[1]), 1)

            break
                #
          #  break

        # if PREDICTION_END[0] <= 0 or PREDICTION_END[0] >= WIDTH:
        #     pygame.draw.line(screen, RED, (ball.x, ball.y), (PREDICTION_END[0], PREDICTION_END[1]), 1)
        #     break


        # PREDICTION_START = [PREDICTION_END[0], PREDICTION_END[1]]
        #
        # PREDICTION_START[0] = PREDICTION_END[0] - SPD_X
        # PREDICTION_START[1] = PREDICTION_END[1] - SPD_Y
        # pygame.draw.line(screen, RED, (PREDICTION_END[0], PREDICTION_END[1]), (PREDICTION_START[0], PREDICTION_START[1]))


        print('D')



        print(PREDICTION_END[0])

    # Drawing
    pygame.draw.rect(screen, WHITE, left_paddle)
    pygame.draw.rect(screen, WHITE, right_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))
    pygame.draw.rect(screen, RED, indicator)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()