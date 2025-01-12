# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")

    while True:
        # Fill the screen with a solid "black" color (RGB: 0, 0, 0)
        screen.fill((0, 0, 0))

        # Refresh the display to show the updates
        pygame.display.flip()


if __name__ == "__main__":
    main()