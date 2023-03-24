import pygame.locals
import sys
import random
from Ball import *

Black = (0, 0, 0)
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

        if event.type == pygame.MOUSEBUTTONUP:
            newBall = Ball(window, WindowWidth, WindowHeight)
            ballList.append(newBall)

    for ball in ballList:
        ball.update()

    window.fill(Black)
    for ball in ballList:
        ball.draw()

    pygame.display.update()

    clock.tick(FPS)
