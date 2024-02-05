import random

import pygame

import Media
from Backpack import BackPack
from Player import Player
from Scenery import Scenery

if __name__ == '__main__':

    pygame.init()



    backpack = BackPack([random.randint(0, 1460), random.randint(0, 840)], [20, 20], Media.backpack_image)

    player = Player(300, [150, 280], [50, 50], Media.rambo_image, 300, [150, 280], 0, backpack)

    hobbiton_scene = Scenery(Media.hobbiton_map, Media.background_image, [150, 280], Media.hobbiton_items, player)

    map = hobbiton_scene

    game_running = True
    clock = pygame.time.Clock()

    Media.MusicBox.playFoundMusic()

    while game_running:
        game_running = map.handle_events()

        if map.player.live_bar < 1:
            game_running = False

        if not map.update():
            break

        map.render()

        clock.tick(60)

    pygame.quit()