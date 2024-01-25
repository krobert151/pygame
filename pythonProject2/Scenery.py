import csv
import random

import pygame

from Potion import Potion
from Wall import Wall
from Diamond import Diamond
from Player import Player
from Water import Water

stone_block = pygame.image.load("media/image/wall.png")
leaf_block = pygame.image.load("media/image/leaft.png")
diamond_block = pygame.image.load("media/image/diamond.png")
water_block = pygame.image.load("media/image/water.png")
health_potion = pygame.image.load("media/image/healht_potion.png")

diamond_block = pygame.transform.scale(diamond_block, (20, 20))
stone_block = pygame.transform.scale(stone_block, (20, 20))
leaf_block = pygame.transform.scale(leaf_block, (20, 20))
water_block = pygame.transform.scale(water_block, (20, 20))
health_potion = pygame.transform.scale(health_potion, (50, 50))


class Scenery:
    def __init__(self, map_filename, background_image, spawn, diamond_count, health_potion_count, player):
        self.obstacles = self.load_obstacle_map(map_filename)
        self.consumable_list = self.instance_consumable(diamond_count, health_potion_count)
        self.spawn = spawn.copy()
        self.player = player
        self.background_image = background_image
        self.screen = pygame.display.set_mode((1480, 860))
        self.font = pygame.font.Font(None, 36)

    @staticmethod
    def instance_consumable(diamond_counts, potion_counts):

        consubamble = []

        diamond_list = [Diamond([random.randint(0, 1460), random.randint(0, 840)], [20, 20], diamond_block) for _ in
                        range(diamond_counts)]

        health_potion_list = [
            Potion([random.randint(0, 1460), random.randint(0, 840)], [50, 50], health_potion, "HP(10)") for
            _ in range(potion_counts)]

        for diamond in diamond_list:
            consubamble.append(diamond)

        for potion in health_potion_list:
            consubamble.append(potion)

        return consubamble

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

        if Player.check_static_object_collision(self.player, self.obstacles, self.spawn.copy()):
            pass
        elif self.player.getBackpack():
            pass
        elif Player.check_consumable_object_collision(self.player, self.consumable_list):
            pass
        elif self.player.breath < 300:
            self.player.breath += 3

        return True

    @staticmethod
    def load_obstacle_map(filename):

        object = []

        with open(filename, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                x = int(row['x'])
                y = int(row['y'])
                block_type = row['type'].lower()

                if block_type == 'stone_block':
                    object.append(Wall([x, y], [20, 20], stone_block))
                elif block_type == 'diamond':
                    object.append(Diamond([x, y], [20, 20], leaf_block))
                elif block_type == 'leaf_block':
                    object.append(Wall([x, y], [20, 20], leaf_block))
                elif block_type == "water_block":
                    object.append(Water([x, y], [20, 20], water_block))
        return object

    def render(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.background_image, (0, 0))

        pygame.draw.rect(self.screen, (0, 0, 0), (880, 700, 600, 200))

        printable_items = {}
        for item in self.player.backpack.items:

            if item.image not in printable_items:
                printable_items[item.image] = 1
            else:
                printable_items[item.image] += 1


        print(printable_items)
        c = 1
        for item in printable_items:

            image = pygame.transform.scale(item,(20,20))
            self.screen.blit(image, [1100+30*c, 810])
            self.screen.blit(self.font.render(str(item.get(item)),1, (255, 255, 255)),[1100+60*c, 810])
            c +=1
        c = 0
        while c < self.player.live_bar:
            pygame.draw.rect(self.screen, (255, 0, 0),
                             (1100 + c, 730, 1, 20))
            c += 1

        c = 0
        while c < self.player.breath:
            pygame.draw.rect(self.screen, (0, 0, 255),
                             (1100 + c, 770, 1, 20))
            c += 1

        for consumable in self.consumable_list:
            self.screen.blit(consumable.image, (consumable.position[0], consumable.position[1]))

        for object in self.obstacles:
            self.screen.blit(object.image, (object.position[0], object.position[1]))

        self.screen.blit(self.player.backpack.image,
                         (self.player.backpack.position[0], self.player.backpack.position[1]))

        self.screen.blit(self.player.image, (self.player.position[0], self.player.position[1]))

        # Draw score
        text = self.font.render("Score: " + str(self.player.score), 1, (255, 255, 255))
        self.screen.blit(text, (900, 730))

        pygame.display.flip()
