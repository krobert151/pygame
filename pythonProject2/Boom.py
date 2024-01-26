import pygame.draw

from Consumable import Consumable


class Boom(Consumable):
    def __init__(self, position, size, image, radius):
        super().__init__(position, size, image)
        self.radius = radius

    def consume(self, player, scenery):
        super().consume(player, scenery)
        left_corner = (player.position[0] - self.radius, player.position[1] - self.radius)
        area = []
        for a in range(self.radius):
            for b in range(self.radius):
                coord = (left_corner[0] + a * 20, left_corner[1] + b * 20)
                area.append(coord)
                for element in scenery.obstacles:
                    if (coord[0] < element.position[0] + element.size[0] and
                            coord[0] + 20 > element.position[0] and
                            coord[1] < element.position[1] + element.size[1] and
                            coord[1] + 20 > element.position[1]):
                        if element.breakable:
                            element.position = [-100, -100]

