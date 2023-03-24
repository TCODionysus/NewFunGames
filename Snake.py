import pygame.locals
import random


class Snake:
    def __init__(self, window, windowWidth, windowHeight):
        self.window = window
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight

        self.image = pygame.image.load('Images/SNAKE.png')
        self.noise = pygame.mixer.Sound('Sounds/HissSFX.wav')
        self.aRect = self.image.get_rect()
        self.width = self.aRect.width
        self.height = self.aRect.height
        self.maxWidth = windowWidth - self.width
        self.maxHeight = windowHeight - self.height

        self.X = random.randrange(self.maxWidth)
        self.Y = random.randrange(self.maxHeight)

        speedList = [-4, -3, -2, -1, 1, 2, 3, 4]
        self.XSpeed = random.choice(speedList)
        self.YSpeed = random.choice(speedList)

    def update(self):
        if self.X < 0 or self.X >= self.maxWidth:
            self.XSpeed = -self.XSpeed
            self.noise.play()
        if self.Y < 0 or self.Y >= self.maxHeight:
            self.YSpeed = -self.YSpeed
            self.noise.play()

        self.X += self.XSpeed
        self.Y += self.YSpeed

    def draw(self):
        self.window.blit(self.image, (self.X, self.Y))
