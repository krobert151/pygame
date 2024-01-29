import pygame


class Media:
    pygame.init()

    info = pygame.display.Info()

    H = info.current_h
    W = info.current_w

    ROWS = 42
    COLS = 73

    NormalItemSize = (W/COLS), (H/ROWS)

    # Map
    hobbiton_map = 'media/maps/hobbiton.csv'

    # Items
    hobbition_items = 'media/items/hobbiton.csv'

    # Backgound
    background_image = pygame.transform.scale(pygame.image.load("media/image/first_zone.png"), (W, H))

    # Characters
    rambo_image = pygame.transform.scale(pygame.image.load("media/image/rambo.png"), ((W/COLS)*2, (H/ROWS)*2))

    # StaticsObject
    stone_block = pygame.transform.scale(pygame.image.load("media/image/wall.png"), NormalItemSize)
    leaf_block = pygame.transform.scale(pygame.image.load("media/image/leaft.png"), NormalItemSize)
    water_block = pygame.transform.scale(pygame.image.load("media/image/water.png"), NormalItemSize)

    # DynamicObjects
    backpack_image = pygame.transform.scale(pygame.image.load("media/image/backpack.png"), NormalItemSize)
    diamond_block = pygame.transform.scale(pygame.image.load("media/image/diamond.png"), NormalItemSize)
    health_potion = pygame.transform.scale(pygame.image.load("media/image/healht_potion.png"), NormalItemSize)
    water_potion = pygame.transform.scale(pygame.image.load("media/image/water_potion.png"), NormalItemSize)
    boom = pygame.transform.scale(pygame.image.load("media/image/boom.png"), NormalItemSize)

    # Music
    @staticmethod
    def fisrtZone():
        pygame.mixer.Sound('media/audio/first_zone.mp3').play().set_volume(1)

    pass

    @staticmethod
    def wallCollision():
        pygame.mixer.Sound('media/audio/metal_pipe_falling.mp3').play().set_volume(1)

    pass

    @classmethod
    def set_resolution(cls, width, height):
        cls.W = width
        cls.H = height

    @classmethod
    def set_grid_size(cls, rows, cols):
        cls.ROWS = rows
        cls.COLS = cols
