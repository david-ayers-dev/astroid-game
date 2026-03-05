import constants
import random
import pygame
from circleshape import CircleShape
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, constants.LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")

        angle = random.uniform(20, 50)

        v1 = pygame.math.Vector2.rotate(self.velocity, angle)
        v2 = pygame.math.Vector2.rotate(self.velocity, -angle)

        new_radius = self.radius - constants.ASTEROID_MIN_RADIUS

        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = v1 * 1.2
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = v2 * 1.2
