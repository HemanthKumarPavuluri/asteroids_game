# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from shot import Shot
from asteroids import Asteroids
from asteroidfield import AsteroidField



def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()


    Player.containers = (updatable, drawable)
    Asteroids.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable,)
    Shot.containers = (updatable, drawable, shots)


    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        # Fill the screen with a solid "black" color (RGB: 0, 0, 0)
        screen.fill((0, 0, 0))

        # handles movement
        for updatable_obj in updatable:
            updatable_obj.update(dt) 

        for asteroid in asteroids:
            if player.check_collision(asteroid):
                print("Game Over!!")
                pygame.quit()
                return
            for shot in shots:
                if asteroid.check_collision(shot):
                    shot.kill()
                    asteroid.kill()
                
        
        #Draws player triangle to screen
        for drawable_object in drawable:
            drawable_object.draw(screen)
        # Refresh the display to show the updates
        pygame.display.flip()

        dt = clock.tick(60) / 1000

        


if __name__ == "__main__":
    main()