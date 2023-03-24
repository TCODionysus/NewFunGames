import pygame.locals
import sys
import random
from Ball import Ball
from Snake import Snake
from E import E

Black = (0, 0, 0)
Green = (0, 255, 0)
WindowWidth = 1200
WindowHeight = 600
FPS = 30

pygame.init()
window = pygame.display.set_mode((WindowWidth, WindowHeight))
clock = pygame.time.Clock()

ball1 = Ball(window, WindowWidth, WindowHeight)
ballList = [ball1]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                newBall = Ball(window, WindowWidth, WindowHeight)
                ballList.append(newBall)
            if event.key == pygame.K_s:
                newSnake = Snake(window, WindowWidth, WindowHeight)
                ballList.append(newSnake)
            if event.key == pygame.K_e:
                newE = E(window, WindowWidth, WindowHeight)
                ballList.append(newE)

    for ball in ballList:
        ball.update()

    window.fill(Black)
    for ball in ballList:
        ball.draw()

    pygame.display.update()

    clock.tick(FPS)
