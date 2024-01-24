import random

import pygame

from Obstacle import Obstacle
from Diamond import Diamond
from Player import Player


class Scenery:
    def __init__(self, map_filename, background_image, obstacle_image, spawn, diamond_count, live):
        self.obstacles = Obstacle.load_obstacle_map(map_filename, obstacle_image)
        self.diamonds = [Diamond([random.randint(0, 1460), random.randint(0, 840)]) for _ in range(diamond_count)]
        self.spawn = spawn.copy()
        self.player = Player(spawn)
        self.background_image = background_image
        self.live_bar = live
        self.screen = pygame.display.set_mode((1480, 860))
        self.font = pygame.font.Font(None, 36)
        self.score = 0

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.player.right = True
                elif event.key == pygame.K_LEFT:
                    self.player.left = True
                elif event.key == pygame.K_UP:
                    self.player.up = True
                elif event.key == pygame.K_DOWN:
                    self.player.down = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.player.right = False
                elif event.key == pygame.K_LEFT:
                    self.player.left = False
                elif event.key == pygame.K_UP:
                    self.player.up = False
                elif event.key == pygame.K_DOWN:
                    self.player.down = False
        return True

    def update(self):
        self.player.move()

        if Player.check_collision(self.player, self.obstacles):
            self.score -= 1
            self.live_bar -= 30
            self.player.position = self.spawn.copy()
            metal_pipe = pygame.mixer.Sound('media/audio/metal_pipe_falling.mp3')
            metal_pipe.set_volume(1)
            metal_pipe.play()
        else:
            for diamond in self.diamonds:
                if diamond.check_diamond_collision(self.player, self.diamonds):
                    self.score += 1
                    self.diamonds.remove(diamond)
                    get_diamond_sound = pygame.mixer.Sound('media/audio/get_diamonds.mp3')
                    get_diamond_sound.set_volume(1)
                    get_diamond_sound.play()

        return True

    def render(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.background_image, (0, 0))

        pygame.draw.rect(self.screen,(0,0,0),(880,700,600,200))

        c = 0
        while c < self.live_bar:
            pygame.draw.rect(self.screen, (255, 0, 0),
                             (1100+c, 730, 1, 20))
            c += 1

        for diamond in self.diamonds:
            self.screen.blit(diamond.image, (diamond.position[0], diamond.position[1]))

        self.screen.blit(self.player.image, (self.player.position[0], self.player.position[1]))

        for wall in self.obstacles:
            self.screen.blit(wall.image, (wall.position[0], wall.position[1]))

        # Draw score
        text = self.font.render("Score: " + str(self.score), 1, (255, 255, 255))
        self.screen.blit(text, (900, 730))

        pygame.display.flip()
