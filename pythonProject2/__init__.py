from Diamond import Diamond
from Obstacle import Obstacle
from Player import Player
import pygame

if __name__ == '__main__':

    pygame.init()

    back_ground_image = pygame.image.load("image/first_zone.png")
    back_ground_image = pygame.transform.scale(back_ground_image, (1480, 860))

    game_running = True

    clock = pygame.time.Clock()

    diamonds_count = 5
    c = 0
    diamonds = [Diamond([200,200]),Diamond([250,250])]


    obstacles = [Obstacle()]

    player_one = Player()
    screen = pygame.display.set_mode((1480, 860))
    font = pygame.font.Font(None, 36)
    score = 0

    first_zone_music = pygame.mixer.Sound('media/audio/first_zone.mp3')
    first_zone_music.set_volume(1)
    first_zone_music.play()

    while game_running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    player_one.right = True
                elif event.key == pygame.K_LEFT:
                    player_one.left = True
                elif event.key == pygame.K_UP:
                    player_one.up = True
                elif event.key == pygame.K_DOWN:
                    player_one.down = True

            elif event.type == pygame.KEYUP:
                player_one.right = False
                player_one.left = False
                player_one.up = False
                player_one.down = False

        player_one.move()

        if player_one.check_collision(obstacles):
            score -= 1
            player_one.position = [150, 280]
            metal_pipe = pygame.mixer.Sound('media/audio/metal_pipe_falling.mp3')
            metal_pipe.set_volume(1)
            metal_pipe.play()
        else:
            if Diamond.check_diamond_collision(player_one, diamonds):
                score += 1
                get_diamond_sound = pygame.mixer.Sound('media/audio/get_diamonds.mp3')
                get_diamond_sound.set_volume(1)
                get_diamond_sound.play()

            screen.fill((0, 0, 0))
            screen.blit(back_ground_image, (0, 0))
            # print diamond

            for diamond in diamonds:
                screen.blit(diamond.image, (diamond.position[0], diamond.position[1]))

            screen.blit(player_one.image, (player_one.position[0], player_one.position[1]))

            for wall in obstacles:
                screen.blit(wall.image, (wall.position[0], wall.position[1]))

            # Dibujar puntuación
            text = font.render("Score: " + str(score), 1, (255, 255, 255))
            screen.blit(text, (10, 10))
            # Actualizar pantalla
            pygame.display.flip()
            clock.tick(60)

    pygame.quit()
