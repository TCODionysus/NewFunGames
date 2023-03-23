import pygame.locals
import sys
import random


def newHole():
    x = 330
    while 275 <= x <= 340:
        x = random.randrange(615)
    return x


Red = (255, 0, 0)
Black = (0, 0, 0)
White = (255, 255, 255)
WindowWidth = 650
WindowHeight = 650
SquareX = 310
SquareY = 310
FPS = 20
Step = 2
SquareWidth = 30
SquareHeight = 30
HoleWidth = 35
HoleHeight = 35

pygame.init()
pygame.font.init()
myFont = pygame.font.SysFont('TimesNewRoman', 20)
window = pygame.display.set_mode((WindowWidth, WindowHeight))
pygame.display.set_caption('The Descent')
clock = pygame.time.Clock()
pygame.mixer.music.load('Sounds/Descent.wav')
pygame.mixer.music.set_volume(0.05)
pygame.mixer.music.play(-1, 0.0)

Whoosh = pygame.mixer.Sound('Sounds/WhooshSFX.wav')
f1 = pygame.image.load('Images/DescentFrames/DescentFrame1.png')
f2 = pygame.image.load('Images/DescentFrames/DescentFrame2.png')
f3 = pygame.image.load('Images/DescentFrames/DescentFrame3.png')
f4 = pygame.image.load('Images/DescentFrames/DescentFrame4.png')
f5 = pygame.image.load('Images/DescentFrames/DescentFrame5.png')
f6 = pygame.image.load('Images/DescentFrames/DescentFrame6.png')
f7 = pygame.image.load('Images/DescentFrames/DescentFrame7.png')
f8 = pygame.image.load('Images/DescentFrames/DescentFrame8.png')
f9 = pygame.image.load('Images/DescentFrames/DescentFrame9.png')
f10 = pygame.image.load('Images/DescentFrames/DescentFrame10.png')
f11 = pygame.image.load('Images/DescentFrames/DescentFrame11.png')
f12 = pygame.image.load('Images/DescentFrames/DescentFrame12.png')
f13 = pygame.image.load('Images/DescentFrames/DescentFrame13.png')
f14 = pygame.image.load('Images/DescentFrames/DescentFrame14.png')
f15 = pygame.image.load('Images/DescentFrames/DescentFrame15.png')
f16 = pygame.image.load('Images/DescentFrames/DescentFrame16.png')
f17 = pygame.image.load('Images/DescentFrames/DescentFrame17.png')
f18 = pygame.image.load('Images/DescentFrames/DescentFrame18.png')
f19 = pygame.image.load('Images/DescentFrames/DescentFrame19.png')

level = 0
endgame = 0
warning = myFont.render('you should have brought a torch', True, White)
currentShade = Red
currentX = SquareX
currentY = SquareY
HoleX = newHole()
HoleY = newHole()

while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    key_pressed = pygame.key.get_pressed()
    if key_pressed[pygame.K_UP] == 1 and currentY > 0:
        currentY = currentY - Step
    if key_pressed[pygame.K_DOWN] == 1 and currentY < WindowHeight - SquareHeight:
        currentY = currentY + Step
    if key_pressed[pygame.K_LEFT] == 1 and currentX > 0:
        currentX = currentX - Step
    if key_pressed[pygame.K_RIGHT] == 1 and currentX < WindowWidth - SquareWidth:
        currentX = currentX + Step

    if (HoleX <= currentX <= HoleX + 5) and (HoleY <= currentY <= HoleY + 5):
        currentX = SquareX
        currentY = SquareY
        HoleX = newHole()
        HoleY = newHole()
        currentShade = (currentShade[0] - 5, 0, 0)
        Whoosh.play()
        level += 1
        # play noises
        if level % 5 == 0:
            pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() + 0.1)
        if level == 20:
            pygame.mixer.music.load('Sounds/Descent2.wav')
            pygame.mixer.music.play(-1, 0.0)
        if level == 38:
            pygame.mixer.music.load('Sounds/Descent3.wav')
            pygame.mixer.music.play(-1, 0.0)
        if level == 49:
            pygame.mixer.music.load('Sounds/Descent.wav')
            pygame.mixer.music.play(-1, 0.0)

    Square = pygame.rect.Rect(currentX, currentY, SquareWidth, SquareHeight)
    Hole = pygame.rect.Rect(HoleX, HoleY, HoleWidth, HoleHeight)

    window.fill(currentShade)
    pygame.draw.rect(window, Black, Square)
    pygame.draw.rect(window, Black, Hole)
    if level == 49:
        window.blit(warning, (150, 300))
        endgame += 1
    if endgame == 61:
        FPS = 15
        window.blit(f1, (0, 0))
    if endgame == 62:
        window.blit(f2, (0, 0))
    if endgame == 63:
        window.blit(f3, (0, 0))
    if endgame == 64:
        window.blit(f4, (0, 0))
    if endgame == 65:
        window.blit(f5, (0, 0))
    if endgame == 66:
        window.blit(f6, (0, 0))
    if endgame == 67:
        window.blit(f7, (0, 0))
    if endgame == 68:
        window.blit(f8, (0, 0))
    if endgame == 69:
        window.blit(f9, (0, 0))
    if endgame == 70:
        window.blit(f10, (0, 0))
    if endgame == 71:
        window.blit(f11, (0, 0))
    if endgame == 72:
        window.blit(f12, (0, 0))
    if endgame == 73:
        window.blit(f13, (0, 0))
    if endgame == 74:
        window.blit(f14, (0, 0))
    if endgame == 75:
        window.blit(f15, (0, 0))
    if endgame == 76:
        window.blit(f16, (0, 0))
    if endgame == 77:
        window.blit(f17, (0, 0))
    if endgame == 78:
        window.blit(f18, (0, 0))
    if endgame >= 79:
        window.blit(f19, (0, 0))

    pygame.display.update()

    if endgame == 82:
        pygame.quit()
        sys.exit()

    clock.tick(FPS)
