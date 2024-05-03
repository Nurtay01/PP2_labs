import pygame 
import random
import time
pygame.init()

speed = 5
score = 0
score_coins = 0

font = pygame.font.SysFont("Arial", 60)
font_score = pygame.font.SysFont("Arial", 20)
game_over = font.render(f"GAME OVER", True, "red")

image = pygame.image.load(r"lab9/images/AnimatedStreet.png")
pygame.mixer.Sound(r"lab9/music/catch-up-if-you-can-199590.mp3").play(-1)

screen = pygame.display.set_mode((400,600))
fps = pygame.time.Clock()
pygame.display.set_caption("RACE")

class Player(pygame.sprite.Sprite):
    def init(self):
        super().init()
        self.image = pygame.image.load(r'lab9/images/car2.png')
        self.rect = self.image.get_rect()
        self.rect.center = (160,520)
        self.damaged = False  # Флаг, указывающий на повреждение машины

    def move(self):
        pressed = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed[pygame.K_LEFT]:
                self.rect.move_ip(-7,0)
        if self.rect.right < 400:
            if pressed[pygame.K_RIGHT]:
                self.rect.move_ip(7,0)

class Enemy(pygame.sprite.Sprite):
    def init(self):
        super().init()
        self.image = pygame.image.load(r'lab9/images/car.png')
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,360),0)

    def move(self):
        global score
        self.rect.move_ip(0,speed)
        if self.rect.bottom > 600:
            score += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40,360),0)

class Coin(pygame.sprite.Sprite):
    def init(self):
        super().init()
        self.image = pygame.image.load(r"lab9/images/coin.png")
        self.image = pygame.transform.scale(self.image,(30,35))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,360),0)

    def move(self):
        self.rect.move_ip(0,5)
        global score_coins, coins ,speed
        if self.rect.bottom > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(40,360),0)
        if pygame.sprite.spritecollideany(p1,coins):
            speed += 2
            score_coins += (random.randint(1,5))
            self.rect.top = 0
            self.rect.center = (random.randint(40,360),0)
            pl = pygame.mixer.Sound(r"lab9/music/lab8_race_coinsMusic.mp3")
            pl.play()

class Hole(pygame.sprite.Sprite):
    def init(self):
        super().init()
        self.image = pygame.image.load(r'lab9/images/pit.png')
        self.image = pygame.transform.scale(self.image,(30.35))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, 360), 0)

    def move(self):
        self.rect.move_ip(0, 5)
        if self.rect.bottom > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(40, 360), 0)

def check_hole_collision(player):
    global status
    if pygame.sprite.spritecollide(player, holes, dokill=True):
        if not player.damaged:
            player.damaged = True
        else:
            pygame.mixer.stop()
            pygame.mixer.Sound(r'lab9/lab8_race_crash.wav').play()
            time.sleep(0.5)
            screen.fill((255, 0, 0))
            screen.blit(game_over, (30, 250))
            pygame.display.update()
            for sprite in all_sp:
                sprite.kill()
            time.sleep(5)
            status = False

p1 = Player()
e1 = Enemy()
c1 = Coin()
h1 = Hole()
h2 = Hole()

enemies = pygame.sprite.Group()
enemies.add(e1)
all_sp = pygame.sprite.Group()
all_sp.add(e1)
all_sp.add(p1)
all_sp.add(c1)
all_sp.add(h1)
all_sp.add(h2)
coins = pygame.sprite.Group()
coins.add(c1)
holes = pygame.sprite.Group()
holes.add(h1, h2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(image,(0,0))
    scores = font_score.render(str(score),True,(0,0,0))
    screen.blit(scores,(10,10))

    for x in all_sp:
        screen.blit(x.image, x.rect)
        x.move()

    check_hole_collision(p1)
    if pygame.sprite.spritecollideany(p1,enemies):
        pygame.mixer.stop()
        pygame.mixer.Sound(r'lab9/lab8_race_crash.wav').play()
        time.sleep(0.5)
        screen.fill((255,0,0))
        screen.blit(game_over,(30,250))
        pygame.display.update()
        for y in all_sp:
            y.kill()
        time.sleep(5)
        status = False

    ff = font_score.render(str(score_coins),True,(0,0,0))
    screen.blit(ff,(360,10))

    pygame.display.update()
    fps.tick(60)