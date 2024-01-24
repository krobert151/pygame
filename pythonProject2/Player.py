import pygame

rambo_image = pygame.image.load("image/rambo.png")
rambo_image = pygame.transform.scale(rambo_image, (50, 50))


class Player:
    def __init__(self, spawn):
        self.position = spawn
        self.speed = 10
        self.image = rambo_image
        self.size = [50, 50]
        self.right = False
        self.left = False
        self.up = False
        self.down = False

    def move(self):
        if self.right:
            self.position[0] += self.speed
        elif self.left:
            self.position[0] -= self.speed
        elif self.up:
            self.position[1] -= self.speed
        elif self.down:
            self.position[1] += self.speed

    @staticmethod
    def check_collision(player, collection):
        for element in collection:
            if (
                    player.position[0] < element.position[0] + element.size[0]
                    and player.position[0] + player.size[0] > element.position[0]
                    and player.position[1] < element.position[1] + element.size[1]
                    and player.position[1] + player.size[1] > element.position[1]
            ):
                return True  # Return True if collision is detected

        return False  # Return False if no collision is detected
