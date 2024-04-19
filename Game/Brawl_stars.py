import pygame
pygame.init()

W = 600
H = 400
sc = pygame.display.set_mode((W,H))
pygame.display.set_caption("OHIO_STARS")
pygame.display.set_icon(pygame.image.load('Game/dragon.png'))
bg = pygame.image.load("Game/Phon.jpg")
walk_right = [pygame.image.load('Game/Person1/a.png'),
              pygame.image.load('Game/Person1/b.png'),
              pygame.image.load('Game/Person1/c.png'),
              pygame.image.load('Game/Person1/d.png')]
walk_left = [pygame.image.load('Game/Person2/q.png'),
              pygame.image.load('Game/Person2/w.png'),
              pygame.image.load('Game/Person2/e.png'),
              pygame.image.load('Game/Person2/r.png')]


clock = pygame.time.Clock()
count = 0
bg_x = 0
bg_s = pygame.mixer.Sound('Game/Sakura-Girl-Motivation-chosic.com_.mp3')
bg_s.play()
while 1:
    sc.blit(bg,(bg_x,0))
    sc.blit(bg,(bg_x+600,0))
    pygame.display.update()
    
    sc.blit(walk_right[count],(300,250))
    if count == 3:
        count = 0
    else:
        count += 1
    bg_x -= 2
    if bg_x == -618:
        bg_x = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()    
    pygame.display.update()  
    clock.tick(10)