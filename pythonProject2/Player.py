import pygame

from Boom import Boom
from Character import Character
from Diamond import Diamond
wwwwwwdwfrom Potion import Potion
from Wall import Wall
from Water import Water


class Player(Character):
    def __init__(self, live_bar, position, size, image, breath, spawn, score, backpack):
        super().__init__(live_bar, position, size, image, breath, spawn)
        self.score = score
        self.live_bar = live_bar
        self.position = spawn
        self.speed = 10
        self.image = image
        self.size = size
        self.breath = breath
        self.backpack = backpack
        self.right = False
        self.left = False
        self.up = False
        self.down = False
        self.inventory = False

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
    def check_static_object_collision(player, collection, spawn):
        for element in collection:
            if (
                    player.position[0] < element.position[0] + element.size[0]
                    and player.position[0] + player.size[0] > element.position[0]
                    and player.position[1] < element.position[1] + element.size[1]
                    and player.position[1] + player.size[1] > element.position[1]
            ):
                if isinstance(element, Wall):
                    player.score -= 1
                    player.live_bar -= 30
                    Media.wallCollision()
                    player.position = spawn
                elif isinstance(element, Water):
                    player.speed = 2
                    player.breath -= 1

                    if player.breath < 1:
                        player.live_bar -= 1
                return True
            player.speed = 10
        return False

    @staticmethod
    def check_consumable_object_collision(player, collection):
        for element in collection:
            if (player.position[0] < element.position[0] + element.size[0] and
                    player.position[0] + player.size[0] > element.position[0] and
                    player.position[1] < element.position[1] + element.size[1] and
                    player.position[1] + player.size[1] > element.position[1]):
                if isinstance(element, Diamond):
                    element.hide()
                    player.score += 1
                    collection.remove(element)
                    get_diamond_sound = pygame.mixer.Sound('media/audio/get_diamonds.mp3')
                    get_diamond_sound.set_volume(1)
                    get_diamond_sound.play()
                elif isinstance(element, Potion):
                    if player.backpack.equipped and player.backpack.add_item(element):
                        pickup_back_pack_sound = pygame.mixer.Sound("media/audio/pickup_back_pack.mp3")
                        pickup_back_pack_sound.set_volume(1)
                        pickup_back_pack_sound.play()
                        element.hide()
                elif isinstance(element, Boom):
                    if player.backpack.equipped and player.backpack.add_item(element):
                        element.hide()
                return True
        return False

    def getBackpack(self):
        if (self.position[0] < self.backpack.position[0] + self.backpack.size[0]
                and self.position[0] + self.size[0] > self.backpack.position[0]
                and self.position[1] < self.backpack.position[1] + self.backpack.size[1]
                and self.position[1] + self.size[1] > self.backpack.position[1]):
            if not self.backpack.equipped:
                pickup_back_pack_sound = pygame.mixer.Sound("media/audio/pickup_back_pack.mp3")
                pickup_back_pack_sound.set_volume(1)
                pickup_back_pack_sound.play()
            self.backpack.position = [1100, 800]
            self.backpack.image = pygame.transform.scale(self.backpack.image, (30, 30))
            self.backpack.equipped = True


            return True
        return False
