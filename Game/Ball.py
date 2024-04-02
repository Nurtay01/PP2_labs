import pygame
pygame.init()

W = 600
H = 400
sc = pygame.display.set_mode((W,H))
pygame.display.set_caption("Ball")
x = W // 2
y = H // 2
speed = 10
WHITE = (255,255,255)
RED = (255,0,0)

clock = pygame.time.Clock()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()    
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -= speed 
            if event.key == pygame.K_RIGHT:
                x += speed 
    sc.fill(WHITE)
    pygame.draw.rect(sc,RED,(x,y,20,20)) 
    pygame.display.update()  
    clock.tick(60)