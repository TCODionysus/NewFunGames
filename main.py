import pygame.locals
import sys

pygame.init()
pygame.font.init()
myFont = pygame.font.SysFont('TimesNewRoman', 20)
window = pygame.display.set_mode((650, 650))
warning = myFont.render('you should have brought a torch', True, (255, 255, 255))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    window.fill((0, 0, 0))
    window.blit(warning, (300, 300))
    pygame.display.update()
