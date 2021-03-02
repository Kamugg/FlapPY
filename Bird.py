import pygame


# This class describes the bird

class Bird:

    def __init__(self, y):
        self.y = y  # Spawn point
        self.birdspeed = -0.1  # The vertical speed of the bird
        self.angle = 45  # Inclination of the bird
        self.time = 0  # Time since last jump

    def move(self, grav):  # This function makes the bird move in a parabolic motion... kind of
        self.y += self.birdspeed + grav * self.time + 0.005 * grav * self.time ** 2
        self.angle -= 0.005 * grav * self.time ** 2
        self.time += 0.1

    def getpos(self):  # ...
        return self.y

    def getrect(self):  # ...
        return pygame.rect.Rect(50, self.y, 13, 13)

    def getangle(self):  # ...
        return self.angle

    def jump(self):  # Jumping resets the "time since last jump" and the angle
        self.time = 0
        self.angle = 45
