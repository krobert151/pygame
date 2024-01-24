import pygame

from Scenery import Scenery

if __name__ == '__main__':

    pygame.init()

    background_image = pygame.image.load("image/first_zone.png")
    background_image = pygame.transform.scale(background_image, (1480, 860))

    stone_block = pygame.image.load("image/wall.png")
    leaft_block = pygame.image.load("image/leaft.png")

    stone_block = pygame.transform.scale(stone_block, (20, 20))
    leaft_block = pygame.transform.scale(leaft_block, (20, 20))

    hobbiton_scene = Scenery('media/maps/hobbiton.csv', background_image, leaft_block, [150, 280], 5, 300)

    map = hobbiton_scene

    game_running = True
    clock = pygame.time.Clock()

    first_zone_music = pygame.mixer.Sound('media/audio/first_zone.mp3')
    first_zone_music.set_volume(1)
    first_zone_music.play()

    while game_running:
        game_running = map.handle_events()

        if map.live_bar < 1:
            game_running = False

        if not map.update():
            break

        map.render()

        clock.tick(60)

    pygame.quit()
