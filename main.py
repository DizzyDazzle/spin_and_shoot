from constants import *
import pygame
import player



clock = pygame.time.Clock()
surface = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))

pygame.init()

player = player.Player()

def main():
    running = True

    while running:
        clock.tick(TICK_RATE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if event.key == pygame.K_r:
                    board.reset()
                if event.key == pygame.K_q:
                    running = False
        update()
        draw()


    pygame.quit()



def draw():
    surface.fill((0, 0, 0))#background
    player.draw(surface)
    pygame.display.flip()



def update():
    player.update()



if __name__ == "__main__":
    main()
