import numpy as np
import pygame
import datetime

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800

BLACK = (0, 0, 0)
RED = (255, 0 ,0)

def degrees_to_pos(R, theta):
    y = np.cos(2 * np.pi * theta / 360) * R
    x = np.sin(2 * np.pi * theta / 360) * R
    return x + 400 -15 , -(y - 400) - 15

def main():
    pygame.init()

    pygame.display.set_caption("Clock_20180035 Maeng")
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()

    def displayNum(num, pos):
        font = pygame.font.SysFont("FixedSys", 50, True, False)
        num_surface = font.render(num, True, BLACK)
        screen.blit(num_surface, pos)

    done = False
    while not done: 
        screen.fill((255, 255, 255))
        
        current_time = datetime.datetime.now()
        s = current_time.second
        m = current_time.minute
        h = current_time.hour

        pygame.draw.circle(screen, BLACK, (400, 400), 400, 4)
        
        for num in range(1, 13):
            displayNum(str(num), degrees_to_pos(350, num * 30))

        # second hand
        R = 300
        theta = s * (360 / 60)
        pygame.draw.line(screen, RED, (400, 400), degrees_to_pos(R, theta), 8)
        
        # minute hand
        R = 350
        theta = (m + s / 60) * (360 / 60)
        pygame.draw.line(screen, BLACK, (400, 400), degrees_to_pos(R, theta), 8)
       
        # hour hand
        R = 210
        theta = (h + m / 60) * (360 / 12)
        pygame.draw.line(screen, BLACK, (400, 400), degrees_to_pos(R, theta), 8)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        pygame.display.flip()
        clock.tick(50)

if __name__ == "__main__":
    main()
    pygame.quit()