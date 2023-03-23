import pygame.locals
import sys
import random

# 2 - Define constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
FRAMES_PER_SECOND = 30
ballWidth = 516
ballHeight = 256
BallMAX_HEIGHT = WINDOW_HEIGHT - 256
BallMAX_WIDTH = WINDOW_WIDTH - 516
TargetMAX_HEIGHT = WINDOW_HEIGHT - 93
TargetMAX_WIDTH = WINDOW_WIDTH - 656
move_distance = 10

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Cat Hell')
clock = pygame.time.Clock()
targetX = random.randrange(TargetMAX_WIDTH)
targetY = random.randrange(TargetMAX_HEIGHT)

# 4 - Load assets: image(s), sound(s), etc.
SNAKE = pygame.image.load('Images/SNAKE.png')
ANIMAL = pygame.image.load('Images/Animal.png')
GRASS = pygame.image.load('Images/Grass.png')
HISS = pygame.mixer.Sound('Sounds/HissSFX.wav')
pygame.mixer.music.load('Sounds/CatHellBG.wav')
pygame.mixer.music.play(-1, 0.0)

# 5 - Initialize variables
ballX = random.randrange(BallMAX_WIDTH)
ballY = random.randrange(BallMAX_HEIGHT)
targetRect = pygame.locals.Rect(targetX, targetY, 656, 93)

# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        # Clicked the close button? Quit pygame and end the program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 8 - Do any "per frame" actions
    key_pressed = pygame.key.get_pressed()
    if key_pressed[pygame.K_UP] == 1 and ballY > 0:
        ballY = ballY - move_distance
    if key_pressed[pygame.K_DOWN] == 1 and ballY < WINDOW_HEIGHT - ballHeight:
        ballY = ballY + move_distance
    if key_pressed[pygame.K_LEFT] == 1 and ballX > 0:
        ballX = ballX - move_distance
    if key_pressed[pygame.K_RIGHT] == 1 and ballX < WINDOW_WIDTH - ballWidth:
        ballX = ballX + move_distance

    ballRect = pygame.locals.Rect(ballX, ballY, 516, 256)
    if not ballRect.colliderect(targetRect):
        print('there is no escape')
        targetX = random.randrange(TargetMAX_WIDTH)
        targetY = random.randrange(TargetMAX_HEIGHT)
        targetRect = pygame.locals.Rect(targetX, targetY, 656, 93)
        HISS.play()

    # 9 - Clear the window
    window.fill(BLACK)

    # 10 - Draw all window elements
    window.blit(GRASS, (0, 0))
    window.blit(ANIMAL, (ballX, ballY))
    window.blit(SNAKE, (targetX, targetY))

    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)
