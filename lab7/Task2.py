import pygame

pygame.init()
W = 222
H = 332
sc = pygame.display.set_mode((W, H))
pygame.display.set_caption("Music_Player")
bg = pygame.image.load("lab7/images/d179c5c424ed339058effcb85c3f0f49.jpg")
clock = pygame.time.Clock()

music_list = ["lab7/musics/music1.mp3", "lab7/musics/music2.mp3"]
index = 0
track = pygame.mixer.Sound(music_list[index])

playing = False

while True:
    sc.blit(bg,(0,0))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if playing:
                    track.stop()
                    playing = False
                else:
                    track.play()
                    playing = True
            elif event.key == pygame.K_RIGHT:
                track.stop()
                index += 1
                track = pygame.mixer.Sound(music_list[index])
                if playing:
                    track.play()
            elif event.key == pygame.K_LEFT:
                track.stop()
                index -= 1
                track = pygame.mixer.Sound(music_list[index])
                if playing:
                    track.play()

    pygame.display.update()
    clock.tick(60)
