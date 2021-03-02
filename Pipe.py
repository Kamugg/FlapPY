import random

import pygame


# This class describes how a pipe works

class Pipe:

    def __init__(self, x, maxsize):
        self.x = x  # Poition
        self.scored = False  # If the bird jumped on it or no
        self.gap = 100  # Space between bottom pipe and upper pipe
        self.maxsize = maxsize  # Maximum height for the pipe (the size of the screen)
        self.height = random.randint(50, maxsize - 50 - self.gap)  # Deciding a size for the upper pipe
        # Creating images for the upper e bottom pipe
        image = pygame.image.load('pipe_body.png').convert()
        self.bottomimage = pygame.transform.scale(image, (50, self.height))
        self.upperimage = pygame.transform.scale(pygame.transform.rotate(image, 180),
                                                 (50, maxsize - self.height - self.gap - 30))

    def move(self, speed):  # ...
        self.x -= speed

    def getrects(self):  # Returns both of the pipe's rects
        return pygame.rect.Rect(self.x, 0, 50, self.maxsize - self.gap - self.height), pygame.rect.Rect(self.x,
                                                                                                        self.maxsize - self.height,
                                                                                                        50, self.height)

    def getpos(self):  # ...
        return self.x

    def getheight(self):  # ...
        return self.height

    def reset(self):  # Called when the pipe has been passed
        self.__init__(410, self.maxsize)
