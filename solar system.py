import numpy as np
import pygame
import os
from pygame.math import Vector2

# load images
current_path = os.path.dirname(__file__)
univ_img = pygame.image.load(os.path.join(current_path, "assets/universe.jpg"))
sun_img = pygame.image.load(os.path.join(current_path, "assets/Sun.png"))
venus_img = pygame.image.load(os.path.join(current_path, "assets/Venus.png"))
earth_img = pygame.image.load(os.path.join(current_path, "assets/Earth.png"))
saturn_img = pygame.image.load(os.path.join(current_path, "assets/Saturn.png"))
moon_img = pygame.image.load(os.path.join(current_path, "assets/Moon.png"))

# rescaling the planet images
# 지구의 반지름을 1이라 하면 태양은 109(너무 크므로 20배로 임의조정), 금성은 0.9, 토성은 9.4, 달은 0.27
sun_img = pygame.transform.scale(sun_img, (200, 200))
venus_img = pygame.transform.scale(venus_img, (9, 9))
earth_img = pygame.transform.scale(earth_img, (10, 10))
saturn_img = pygame.transform.scale(saturn_img, (376, 246))
moon_img = pygame.transform.scale(saturn_img, (2.7, 2.7))

class Planet():
    def __init__(self, img, mass, x, y, dx, dy):
        self.img = img
        self.x = x
        self.y = y
        self.mass = mass
        self.speed = 2
        self.velocity = Vector2(dx, dy)

    def draw(self, screen):
        screen.blit(self.img, (self.x, self.y))
    
    def move(self):
        self.x += int(self.speed * self.velocity.x)
        self.y += int(self.speed * self.velocity.y)


def drawPlanets(screen, planets, sun):
    sun.draw(screen)

    for planet in planets:
        planet.draw(screen)

    pygame.display.update()

def calculateAngle(p1, p2):
    # calculates the angle between p1 and p2
    x1, y1 = p1
    x2, y2 = p2
    return np.arctan2((y2 - y1), (x2 - x1))

def calculateDis(p1, p2):
    # calculates the distance between p1 and p2
    x1, y1 = p1
    x2, y2 = p2
    return np.hypot((x2 - x1), (y2 - y1))

def translatePlanet(planets, sun):
    for planet in planets:
        theta = calculateAngle((planet.x, planet.y), (sun.x, sun.y))
        dis = calculateDis((planet.x, planet.y), (sun.x, sun.y))

        gravity = (planet.mass * sun.mass) / (dis ** 2)
        dx = np.cos(theta)
        dy = np.sin(theta)
        gravity_vec = gravity * pygame.Vector2(dx, dy)

        # new direction vector
        planet.velocity += gravity_vec

        planet.move()

def main():
    pygame.init()

    info = pygame.display.Info()
    WINDOW_WIDTH = info.current_w
    WINDOW_HEIGHT = info.current_h

    pygame.display.set_caption("Solar System_20180035 Maeng")
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()

    sun = Planet(sun_img, 75, WINDOW_WIDTH/2, WINDOW_HEIGHT/2, 0, 0)
    venus = Planet(venus_img, 2, WINDOW_WIDTH/2 - 50, WINDOW_HEIGHT/2, 0, 1)
    earth = Planet(earth_img, 2, WINDOW_WIDTH/2 - 100, WINDOW_HEIGHT/2, 0, 1)
    saturn = Planet(saturn_img, 10, WINDOW_WIDTH/2 - 185, WINDOW_HEIGHT/2, 0, 1)

    planets = [venus, earth, saturn]

    done = False
    while not done: 
        screen.blit(univ_img, (0, 0))

        drawPlanets(screen, planets, sun)
        translatePlanet(planets, sun)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
    pygame.quit()