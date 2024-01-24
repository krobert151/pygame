import pygame

diamond_image = pygame.image.load("image/diamond.png")
diamond_image = pygame.transform.scale(diamond_image, (20, 20))


class Diamond:

    def __init__(self, position):
        self.position = position
        self.size = [20, 20]
        self.image = diamond_image

    @staticmethod
    def check_diamond_collision(player, collection):
        for element in collection:
            if (player.position[0] < element.position[0] + element.size[0] and
                    player.position[0] + player.size[0] > element.position[0] and
                    player.position[1] < element.position[1] + element.size[1] and
                    player.position[1] + player.size[1] > element.position[1]):
                element.hide()
                return True  # Return True if collision is detected
        return False  # Return False if no collision is detected



    def hide(self):
        self.position = [-100, -100]
