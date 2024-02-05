import pygame

background_image = pygame.transform.scale(pygame.image.load("assets/image/first_zone.png"), (1480, 860))
rambo_image = pygame.transform.scale(pygame.image.load("assets/image/rambo.png"), (50, 50))
backpack_image = pygame.transform.scale(pygame.image.load("assets/image/backpack.png"), (50, 50))
stone_block = pygame.transform.scale(pygame.image.load("assets/image/wall.png"), (20, 20))
leaf_block = pygame.transform.scale(pygame.image.load("assets/image/leaft.png"), (20, 20))
diamond_block = pygame.transform.scale(pygame.image.load("assets/image/diamond.png"), (20, 20))
cobblestone_block = pygame.transform.scale(pygame.image.load("assets/image/cobblestone.png"), (20, 20))
water_block = pygame.transform.scale(pygame.image.load("assets/image/water.png"), (20, 20))
health_potion = pygame.transform.scale(pygame.image.load("assets/image/healht_potion.png"), (20, 20))
water_potion = pygame.transform.scale(pygame.image.load("assets/image/water_potion.png"), (20, 20))
boom = pygame.transform.scale(pygame.image.load("assets/image/boom.png"), (20, 20))


hobbiton_map = 'assets/maps/hobbiton.csv'
hobbiton_items = 'assets/items/hobbiton.csv'


class MusicBox:

    @staticmethod
    def playFoundMusic():
        first_zone_music = pygame.mixer.Sound('assets/audio/first_zone.mp3')
        first_zone_music.set_volume(1)
        first_zone_music.play()

    @staticmethod
    def metalPipe():
        first_zone_music = pygame.mixer.Sound('assets/audio/metal_pipe_falling.mp3')
        first_zone_music.set_volume(1)
        first_zone_music.play()

    @staticmethod
    def getDiamondSound():
        get_diamond_sound = pygame.mixer.Sound('assets/audio/get_diamonds.mp3')
        get_diamond_sound.set_volume(1)
        get_diamond_sound.play()

    @staticmethod
    def backPackSound():
        pickup_back_pack_sound = pygame.mixer.Sound("assets/audio/pickup_back_pack.mp3")
        pickup_back_pack_sound.set_volume(1)
        pickup_back_pack_sound.play()