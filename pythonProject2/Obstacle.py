import pygame

wall_image = pygame.image.load("image/wall.png")
wall_image = pygame.transform.scale(wall_image,(20,20))

class Obstacle:
    def __init__(self):
        self.position = [150, 100]
        self.size = [20,20]
        self.image = wall_image

