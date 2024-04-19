import pygame 
pygame.init()
pygame.font.init()

W = 500
H = 600
sc = pygame.display.set_mode((W,H))
pygame.display.set_caption("Paint")

WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
active_size = 0
active_color = WHITE

sc.fill(WHITE)
pygame.display.update()
clock = pygame.time.Clock()
startdraw = False
kstart = kend = None

def draw_menu():
    pygame.draw.rect(sc,(0,191,255),(0,0,W,70))
    brush = pygame.draw.rect(sc,BLACK,(10,10,50,50))
    pygame.draw.circle(sc,WHITE,(35,35),20)
    brush_list = [brush]

    blue = pygame.draw.rect(sc,BLUE,(90,10,50,50))
    red = pygame.draw.rect(sc,RED,(170,10,50,50))
    green = pygame.draw.rect(sc,GREEN,(250,10,50,50))
    white = pygame.draw.rect(sc,WHITE,(330,10,50,50))
    color_list = [blue,red,green,white]
    rgb_list = [(0,0,255),(255,0,0),(0,255,0),(255,255,255)]
    return brush_list,color_list,rgb_list
while True:
    mouse = pygame.mouse.get_pos()
    if mouse[1] > 70:
        pygame.draw.circle(sc,active_color,mouse,active_size)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
         
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            startdraw = True
            kstart = event.pos
        elif event.type == pygame.MOUSEMOTION:
            if startdraw:
                pos = event.pos
                width = pos[0] - kstart[0]
                height = pos[1] - kstart[1]
                pygame.draw.rect(sc,active_color,(kstart[0],kstart[1], width,height))
                pygame.display.update()
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            startdraw = False
         
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(colors)):
                if colors[i].collidepoint(event.pos):
                   active_color = rgbs[i] 
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(brushes)):
                if brushes[i].collidepoint(event.pos):
                    active_size = 20 - (i * 5)
            
                    
    brushes , colors , rgbs = draw_menu()       
    pygame.display.update()        
    clock.tick(60)