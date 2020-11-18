import pygame
from pygame.draw import *
import numpy as np

# Constants

# Size of screen and FPS
x = 800
y = 800
FPS = 30

# Scale
a = 1  # Scale coefficient for an abscissas' axis
b = 1  # Scale coefficient for an ordinates' axis

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
LIGHTBLUE = (0, 255, 255)
YELLOW = (255, 255, 0)
BROWN = (65, 25, 0)
PINK = (243, 0, 191)
LIGHTBLUE_LAS_1 = (111, 205, 252)
LIGHTBLUE_LAS_2 = (4, 138, 205)
GREEN_BLACK = (4, 138, 1)
PINK_LIGHT = (254, 169, 163)

# Creating a screen and initializing pygame
screen = pygame.display.set_mode((x, y))
pygame.init()


# Functions

# Draw a tree in particular place (d,e) with a given scale (a,b)
def draw_tree(d, e, a, b):
    image_tree = pygame.Surface((int(x * a), int(y * b)), pygame.SRCALPHA)
    pygame.draw.rect(image_tree, BLACK, (int(a * 40), int(a * 70), int(a * 20), int(100 * a)))
    circle(image_tree, GREEN_BLACK, (int(a * 30), int(a * 70)), int(a * 20))
    circle(image_tree, BLACK, (int(a * 30), int(a * 70)), int(a * 20), 1)
    circle(image_tree, GREEN_BLACK, (int(a * 40), int(a * 70)), int(a * 20))
    circle(image_tree, BLACK, (int(a * 40), int(a * 70)), int(a * 20), 1)
    circle(image_tree, GREEN_BLACK, (int(a * 50), int(a * 70)), int(a * 20))
    circle(image_tree, BLACK, (int(a * 50), int(a * 70)), int(a * 20), 1)
    circle(image_tree, GREEN_BLACK, (int(a * 60), int(a * 70)), int(a * 20))
    circle(image_tree, BLACK, (int(a * 60), int(a * 70)), int(a * 20), 1)
    circle(image_tree, GREEN_BLACK, (int(a * 70), int(a * 70)), int(a * 20))
    circle(image_tree, BLACK, (int(a * 70), int(a * 70)), int(a * 20), 1)
    circle(image_tree, GREEN_BLACK, (int(a * 40), int(a * 50)), int(a * 20))
    circle(image_tree, BLACK, (int(a * 40), int(a * 50)), int(a * 20), 1)
    circle(image_tree, GREEN_BLACK, (int(a * 50), int(a * 50)), int(a * 20))
    circle(image_tree, BLACK, (int(a * 50), int(a * 50)), int(a * 20), 1)
    circle(image_tree, GREEN_BLACK, (int(a * 60), int(a * 50)), int(a * 20))
    circle(image_tree, BLACK, (int(a * 60), int(a * 50)), int(a * 20), 1)
    circle(image_tree, GREEN_BLACK, (int(a * 50), int(a * 30)), int(a * 20))
    circle(image_tree, BLACK, (int(a * 50), int(a * 30)), int(a * 20), 1)
    screen.blit(image_tree, (d, e))


# Draw a cloud in particular place (d,e) with a given scale (a,b)
def draw_cloud(d, e, a, b):
    image_cloud = pygame.Surface((int(x * a), int(y * b)), pygame.SRCALPHA)
    circle(image_cloud, WHITE, (int(a * 30), int(a * 100)), int(a * 30))
    circle(image_cloud, BLACK, (int(a * 30), int(a * 100)), int(a * 30), 1)
    circle(image_cloud, WHITE, (int(a * 60), int(a * 100)), int(a * 30))
    circle(image_cloud, BLACK, (int(a * 60), int(a * 100)), int(a * 30), 1)
    circle(image_cloud, WHITE, (int(a * 90), int(a * 100)), int(a * 30))
    circle(image_cloud, BLACK, (int(a * 90), int(a * 100)), int(a * 30), 1)
    circle(image_cloud, WHITE, (int(a * 120), int(a * 100)), int(a * 30))
    circle(image_cloud, BLACK, (int(a * 120), int(a * 100)), int(a * 30), 1)
    circle(image_cloud, WHITE, (int(a * 60), int(a * 70)), int(a * 30))
    circle(image_cloud, BLACK, (int(a * 60), int(a * 70)), int(a * 30), 1)
    circle(image_cloud, WHITE, (int(a * 90), int(a * 70)), int(a * 30))
    circle(image_cloud, BLACK, (int(a * 90), int(a * 70)), int(a * 30), 1)
    screen.blit(image_cloud, (d, e))


# Draw a house in particular place (d,e) with a given scale (a,b)
def draw_house(d, e, a, b):
    image_house = pygame.Surface((int(x * a), int(y * b)))
    image_house.set_colorkey(BLACK)
    image_house.set_alpha(255)
    rect(image_house, BROWN, (int(100 * a), int(200 * b), int(100 * a), int(100 * b)))
    rect(image_house, LIGHTBLUE_LAS_2, (int(135 * a), int(260 * b), int(30 * a), int(30 * a)))
    rect(image_house, LIGHTBLUE_LAS_2, (int(135 * a), int(210 * b), int(30 * a), int(30 * a)))
    polygon(image_house, PINK, [(int(100 * a), int(200 * b)), (int(150 * a), int(150 * b)),
                                (int(200 * a), int(200 * b))])
    screen.blit(image_house, (d, e))


# Draw a sun in particular place (d, e) with a given scale (a,b)
def draw_sun(d, e, a, b):
    image_sun = pygame.Surface((int(x * a), int(y * b)), pygame.SRCALPHA)
    phi = 0
    for i in range(360):
        polygon(image_sun, PINK_LIGHT,
                ([a * (105 - int(70 * np.cos(2 * np.pi / 3 - phi))), b * (105 + int(70 * np.sin(2 * np.pi / 3 - phi)))],
                 [a * (105 + int(70 * np.sin(phi))), b * (105 - int(70 * np.cos(phi)) // 4)],
                 [a * (105 + int(70 * np.cos(2 * np.pi / 3 + phi))), b *
                  (105 + int(70 * np.sin(2 * np.pi / 3 + phi)))]))
        phi += np.pi / 12
    screen.blit(image_sun, (d, e))


# Creating a picture with functions
pygame.draw.rect(screen, GREEN, (0, 400, 800, 400))  # Draw a grass
pygame.draw.rect(screen, LIGHTBLUE_LAS_1, (0, 0, 800, 400))  # Draw a sky
draw_house(-110, 150, 1.5, 1.5)
draw_house(330, 170, 1, 1)
draw_tree(550, 350, 0.6, 0.6)
draw_tree(200, 450, 1, 1)
draw_cloud(300, 150, 1, 1)
draw_cloud(600, 150, 0.7, 0.7)
draw_cloud(100, 200, 1, 1)
draw_cloud(600, 50, 0.7, 0.7)
draw_sun(50, 50, 1, 1)

# Initializing picture
pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
