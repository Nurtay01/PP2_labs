import pygame
from random import randrange 
pygame.init()

W = 600
H = 600
snake_size = 50 # Размер одного кубика змейки

sc = pygame.display.set_mode((W,H))
pygame.display.set_caption("Snake")

clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    clock.tick(60)        
    