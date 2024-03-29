import csv
import random

import pygame

import Media
from Boom import Boom
from Potion import Potion
from Wall import Wall
from Diamond import Diamond
from Player import Player
from Water import Water


class Scenery:
    def __init__(self, map_filename, background_image, spawn, consumable_file, player):
        self.obstacles = self.load_obstacle_map(map_filename)
        self.consumable_list = self.instance_consumable(consumable_file)
        self.spawn = spawn.copy()
        self.player = player
        self.background_image = background_image
        self.screen = pygame.display.set_mode((1480, 860))
        self.font = pygame.font.Font(None, 36)

    @staticmethod
    def instance_consumable(consumable_file):

        consumables = []

        # Read consumable information from CSV file
        with open(consumable_file, newline='') as csvfile:
            consumables_data = list(csv.reader(csvfile))

            for row in consumables_data:
                consumable_type = row[0].strip()
                quantity = int(row[1])

                for _ in range(quantity):
                    if consumable_type == 'Diamond':
                        consumables.append(
                            Diamond([random.randint(0, 1460), random.randint(0, 840)], [20, 20], Media.diamond_block))
                    elif consumable_type == 'HealthPotion+10':
                        consumables.append(
                            Potion([random.randint(0, 1460), random.randint(0, 840)], [20, 20], Media.health_potion,
                                   "HP(10)"))
                    elif consumable_type == 'WaterPotion':
                        consumables.append(
                            Potion([random.randint(0, 1460), random.randint(0, 840)], [50, 50], Media.water_potion,
                                   "O"))
                    elif consumable_type == 'Boom':
                        consumables.append(
                            Boom([random.randint(0, 1460), random.randint(0, 840)], [50, 50], Media.boom,
                                 5))

        return consumables

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    self.player.right = True
                elif event.key == pygame.K_a:
                    self.player.left = True
                elif event.key == pygame.K_w:
                    self.player.up = True
                elif event.key == pygame.K_s:
                    self.player.down = True
                elif event.key == pygame.K_e and self.player.backpack.equipped:
                    self.player.inventory = not self.player.inventory
                elif self.player.inventory:
                    if pygame.K_0 <= event.key <= pygame.K_9:
                        index = event.key - pygame.K_0 - 1
                        self.player.backpack.consume_item_by_index(index, self.player, self)

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    self.player.right = False
                elif event.key == pygame.K_a:
                    self.player.left = False
                elif event.key == pygame.K_w:
                    self.player.up = False
                elif event.key == pygame.K_s:
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

        items = []

        with open(filename, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                x = int(row['x'])
                y = int(row['y'])
                block_type = row['type'].lower()

                if block_type == 'stone_block':
                    items.append(Wall([x, y], [20, 20], Media.stone_block, False))
                elif block_type == 'cobblestone_block':
                    items.append(Wall([x, y], [20, 20], Media.cobblestone_block, True))
                elif block_type == "water_block":
                    items.append(Water([x, y], [20, 20], Media.water_block))
        return items

    def render(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.background_image, (0, 0))

        pygame.draw.rect(self.screen, (0, 0, 0), (880, 20, 600, 100))
        text = self.font.render("Score: " + str(self.player.score), 1, (255, 255, 255))
        self.screen.blit(text, (900, 60))

        if self.player.inventory:
            pygame.draw.rect(self.screen, (0, 0, 0), (20, 20, 600, 50))

            printable_items = {}
            for item in self.player.backpack.items:

                if item.image not in printable_items:
                    printable_items[item.image] = 1
                else:
                    printable_items[item.image] += 1

            c = 1
            for image, quantity in printable_items.items():
                image = pygame.transform.scale(image, (20, 20))
                self.screen.blit(image, [40 * c, 30])
                self.screen.blit(self.font.render(str(quantity), 1, (255, 255, 255)), [(40 * c) + 20, 30])
                c += 1

        c = 0
        while c < self.player.live_bar:
            pygame.draw.rect(self.screen, (255, 0, 0),
                             (1100 + c, 40, 1, 20))
            c += 1

        c = 0
        while c < self.player.breath:
            pygame.draw.rect(self.screen, (0, 0, 255),
                             (1099 + c, 80, 1, 20))
            c += 1

        for consumable in self.consumable_list:
            self.screen.blit(consumable.image, (consumable.position[0], consumable.position[1]))

        for item in self.obstacles:
            self.screen.blit(item.image, (item.position[0], item.position[1]))
        if not self.player.backpack.equipped:
            self.screen.blit(self.player.backpack.image,
                             (self.player.backpack.position[0], self.player.backpack.position[1]))

        self.screen.blit(self.player.image, (self.player.position[0], self.player.position[1]))

        pygame.display.flip()
