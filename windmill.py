import numpy as np
import pygame
import os

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800

WOOD = (142, 80, 29)
BLACK = (0, 0, 0)

current_path = os.path.dirname(__file__)
house_img = pygame.image.load(os.path.join(current_path, "assets/windmill_house.jpg"))
center_img = pygame.image.load(os.path.join(current_path, "assets/windmill_center.png"))

wing_height = 100
wing = np.array([[0, -30, 1], [100, 0, 1], [0, 30, 1]])

def Rmat(deg):
    radian = np.deg2rad(deg)
    c = np.cos(radian)
    s = np.sin(radian)
    R = np.array([[c, -s, 0], [s, c, 0], [0, 0, 1]])
    return R

def Tmat(a, b):
    H = np.eye(3)
    H[0, 2] = a
    H[1, 2] = b
    return H

def remove3D(p):
    p_fin = p[:2].T
    return p_fin

def main():
    pygame.init()

    pygame.display.set_caption("Windmill_20180035 Maeng")
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()

    # 밑변이 160, 높이가 300인 이등변삼각형
    wing_height = 300
    wing = np.array([[0, -80, 1], [wing_height, 0, 1], [0, 80, 1]])

    degree = 90

    done = False
    while not done: 
        screen.blit(house_img, (0, 0))

        degree += 1

        H1 = Tmat(380, 330) @ Tmat(-wing_height, 0)
        wing1 = remove3D(H1 @ wing.T)
        H2 = H1 @ Tmat(wing_height, 0) @ Rmat(degree) @ Tmat(-wing_height, 0)
        wing2 = remove3D(H2 @ wing.copy().T)
        H3 = H2 @ Tmat(wing_height, 0) @ Rmat(degree) @ Tmat(-wing_height, 0)
        wing3 = remove3D(H3 @ wing.copy().T)
        H4 = H3 @ Tmat(wing_height, 0) @ Rmat(degree) @ Tmat(-wing_height, 0)
        wing4 = remove3D(H4 @ wing.copy().T)

        pygame.draw.polygon(screen, WOOD, wing1)
        pygame.draw.polygon(screen, BLACK, wing1, 5)
        pygame.draw.polygon(screen, WOOD, wing2)
        pygame.draw.polygon(screen, BLACK, wing2, 5)
        pygame.draw.polygon(screen, WOOD, wing3)
        pygame.draw.polygon(screen, BLACK, wing3, 5)
        pygame.draw.polygon(screen, WOOD, wing4)
        pygame.draw.polygon(screen, BLACK, wing4, 5)

        screen.blit(center_img, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
    pygame.quit()