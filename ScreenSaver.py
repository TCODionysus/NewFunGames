import pygame.locals
import sys
from Ball import Ball
from Snake import Snake
from E import E
from Mouse import Mouse

Black = (0, 0, 0)
Green = (34, 177, 76)
FPS = 30

pygame.init()
window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
clock = pygame.time.Clock()

WindowWidth = window.get_width()
WindowHeight = window.get_height()
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
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

        if event.type == pygame.MOUSEBUTTONUP:
            newMouse = Mouse(window, WindowWidth, WindowHeight)
            ballList.append(newMouse)

    for ball in ballList:
        ball.update()

    window.fill(Green)
    for ball in ballList:
        ball.draw()

    pygame.display.update()

    clock.tick(FPS)
