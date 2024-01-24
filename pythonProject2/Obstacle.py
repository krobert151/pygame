import csv

import pygame


class Obstacle:
    def __init__(self, position, wall_image):
        self.position = position
        self.size = [20,20]
        self.image = wall_image

    @staticmethod
    def load_obstacle_map(filename, image):
        obstacles = []

        with open(filename, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                x = int(row['x'])
                y = int(row['y'])
                obstacles.append(Obstacle([x, y], image))

        return obstacles