﻿#Импортируем нужные библиотеки
import pygame 
import random
import time
pygame.init()

#Даем значения скорости, счета машин и счета монет
speed = 5
score = 0
score_coins = 0

#Устанавливем размер и шрифт текста 
font = pygame.font.SysFont("Arial", 60)
font_score = pygame.font.SysFont("Arial", 20)
game_over = font.render(f"GAME OVER", True, "red")

#Загружаем фотку улицы и музыку заднего фона (что бы она играла бесконечно)
image = pygame.image.load(r"lab9/images/AnimatedStreet.png")
pygame.mixer.Sound(r"lab9/music/catch-up-if-you-can-199590.mp3").play(-1)

#создаем окно с длинной 400 и высотой 600, фпс это для скорости обнавления игры, название игры
screen = pygame.display.set_mode((400,600))
fps = pygame.time.Clock()
pygame.display.set_caption("RACE")

#Класс нашей машины
class Player(pygame.sprite.Sprite):
    #Загружаем фотку нашей машины и даем ей размеры и координаты центра где она должна появиться в начали игры
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r'lab9/images/car2.png')
        self.rect = self.image.get_rect()
        self.rect.center = (160,520)
    
    #Отвечает за движение 
    def move(self):
        pressed = pygame.key.get_pressed()

        if self.rect.left > 0:
            if pressed[pygame.K_LEFT]:
                self.rect.move_ip(-7,0)


        if self.rect.right < 400:
            if pressed[pygame.K_RIGHT]:
                self.rect.move_ip(7,0)

#Класс врага
class Enemy(pygame.sprite.Sprite):
    #Загружаем фотку нашей машины и даем ей размеры и координаты центра где она должна появиться в начали игры
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r'lab9/images/car.png')
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,360),0)

    #Отвечает за движение 
    def move(self):
        global score
        self.rect.move_ip(0,speed)
        #Если она достигла нижней точки то появляется с рандомными координатами с верху
        if self.rect.bottom > 600:
            score += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40,360),0)

#класс монеты 
class Coin(pygame.sprite.Sprite):
    #Загружаем фотку, даем размеры и рандомные координаты
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"lab9/images/coin.png")
        self.image = pygame.transform.scale(self.image,(30,35))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,360),0)

    # #Отвечает за движение 
    def move(self):
        self.rect.move_ip(0,5)
        global score_coins, coins ,speed
        #Если она достигла нижней точки то появляется с рандомными координатами с верху
        if self.rect.bottom > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(40,360),0)
        #проверяет на соприкосновение и обн счет 
        if pygame.sprite.spritecollideany(p1,coins):
            speed += 2
            score_coins += (random.randint(1,5))
            self.rect.top = 0
            self.rect.center = (random.randint(40,360),0)
            pl = pygame.mixer.Sound(r"lab9/music/lab8_race_coinsMusic.mp3")
            pl.play()


p1 = Player()
e1 = Enemy()
c1 = Coin()
#создаем спрайт группы для рисования и для удобства проверки на прикосновение
enemies = pygame.sprite.Group()
enemies.add(e1)
all_sp = pygame.sprite.Group()
all_sp.add(e1)
all_sp.add(p1)
all_sp.add(c1)
coins = pygame.sprite.Group()
coins.add(c1)


#Цикл игры
running = True
while running:
    #Что бы закрыть игру в удобный момент
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        
    #Отображаем задний фон и счет 
    screen.blit(image,(0,0))
    scores = font_score.render(str(score),True,(0,0,0))
    screen.blit(scores,(10,10))

    #вызываем функцию мув для этой группы спрайтов
    for x in all_sp:
        screen.blit(x.image, x.rect)
        x.move()
    
    #Проверка на соприкосновение с противником
    if pygame.sprite.spritecollideany(p1,enemies):
        pygame.mixer.stop()
        pygame.mixer.Sound(r'lab9/lab8_race_crash.wav').play()
        time.sleep(0.5)

        #заливаем экран красным и выводим текст
        screen.fill((255,0,0))
        screen.blit(game_over,(30,250))
        pygame.display.update()
        #Убиваем все спрайты из этой группы
        for y in all_sp:
            y.kill()
        #ждем 2сек перед выходом их игры
        time.sleep(5)
        status = False

    #Отображаем счет монет
    ff = font_score.render(str(score_coins),True,(0,0,0))
    screen.blit(ff,(360,10))

    #Обн экран и задаем скорость для обн экрана
    pygame.display.update()
    fps.tick(60)