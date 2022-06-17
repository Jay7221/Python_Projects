import pygame
import time
import math

from utils import scale_image

GRASS = scale_image(pygame.image.load("./Images/grass.jpeg"), 30)
TRACK = scale_image( pygame.image.load("./Images/track.png"), 3)

TRACK_BORDER = pygame.image.load("./Images/race-track-border.img")
FINISH = pygame.image.load("./Images/finish.img")

RED_CAR = pygame.image.load("./Images/red-car.img")
GREEN_CAR = pygame.image.load("./Images/green-car.img")

WIDTH, HEIGHT = TRACK.get_width(), TRACK.get_height()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racing Game!")

run = True
clock = pygame.time.Clock()
FPS = 60
while run:
    clock.tick(FPS)
    WIN.blit(GRASS, (0, 0))
    WIN.blit(TRACK, (0, 0))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break

pygame.quit()