import random

import pygame

from Backpack import BackPack
from Player import Player
from Scenery import Scenery

if __name__ == '__main__':

    pygame.init()

    background_image = pygame.image.load("media/image/first_zone.png")
    background_image = pygame.transform.scale(background_image, (1480, 860))
    rambo_image = pygame.image.load("media/image/rambo.png")
    rambo_image = pygame.transform.scale(rambo_image, (50, 50))
    stone_block = pygame.image.load("media/image/wall.png")
    leaf_block = pygame.image.load("media/image/leaft.png")
    backpack_image = pygame.image.load("media/image/backpack.png")
    backpack_image = pygame.transform.scale(backpack_image, (50, 50))
    stone_block = pygame.transform.scale(stone_block, (20, 20))
    leaf_block = pygame.transform.scale(leaf_block, (20, 20))

    backpack = BackPack([random.randint(0, 1460), random.randint(0, 840)], [20, 20], backpack_image)

    player = Player(300, [150, 280], [50, 50], rambo_image, 300, [150, 280], 0, backpack)

    hobbiton_scene = Scenery('media/maps/hobbiton.csv', background_image, [150, 280], 5,5, player)

    map = hobbiton_scene

    game_running = True
    clock = pygame.time.Clock()

    first_zone_music = pygame.mixer.Sound('media/audio/first_zone.mp3')
    first_zone_music.set_volume(1)
    first_zone_music.play()

    while game_running:
        game_running = map.handle_events()

        if map.player.live_bar < 1:
            game_running = False

        if not map.update():
            break

        map.render()

        clock.tick(60)

    pygame.quit()
