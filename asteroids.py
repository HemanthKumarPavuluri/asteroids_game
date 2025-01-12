from circleshape import CircleShape
from constants import *
import random
import pygame


class Asteroids(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2 )

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20,50)
        velocity1 = self.velocity.rotate(angle) * 1.2
        velocity2 = self.velocity.rotate(-angle) * 1.2

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        Asteroids(self.position.x, self.position.y, new_radius).velocity = velocity1
        Asteroids(self.position.x, self.position.y, new_radius).velocity = velocity2
