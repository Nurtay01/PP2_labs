import pygame
import random
pygame.init()

# Устанавливаем размеры окна и создаем его
W = 720
H = 480
sc = pygame.display.set_mode((W, H))
pygame.display.set_caption("SNAKE_2")

# Размер кубика и размеры поля
cub_size = 30
MSIZE = W // cub_size, H // cub_size

# Начальные координаты змеи
start_pos = MSIZE[0] // 2, MSIZE[1] // 2
snake = [start_pos]

# Направление движения змеи
direction = 0
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

# Типы еды и их вероятности
foods = {
    "apple": 0.5,
    "banana": 0.3,
    "orange": 0.2
}

# Функция выбора типа еды
def select_food():
    return random.choices(list(foods.keys()), weights=list(foods.values()))[0]

# Инициализация начальной еды
food_type = select_food()
food_pos = random.randint(0, MSIZE[0]-1), random.randint(0, MSIZE[1]-1)

# Переменные состояния игры
alive = True
running = True

# Инициализация шрифтов
pygame.font.init()
font_score = pygame.font.SysFont("Arial", 25)
font_game_over = pygame.font.SysFont("Arial", 45)
font_level = pygame.font.SysFont("Arial", 25)
food_timer = 0
score = 0

# Инициализация часов для контроля FPS
clock = pygame.time.Clock()
FPS = 5

# Основной игровой цикл
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if alive:
                if event.key == pygame.K_RIGHT and direction != 2:
                    direction = 0
                if event.key == pygame.K_DOWN and direction != 3:
                    direction = 1
                if event.key == pygame.K_LEFT and direction != 0:
                    direction = 2
                if event.key == pygame.K_UP and direction != 1:
                    direction = 3
            else:
                if event.key == pygame.K_SPACE:
                    alive = True
                    snake = [start_pos]
                    food_type = select_food()
                    food_pos = random.randint(0, MSIZE[0]-1), random.randint(0, MSIZE[1]-1)
                    FPS += 1
                    food_timer = 0

    sc.fill((0, 0, 0))

    # Отрисовка змеи
    for x, y in snake:
        pygame.draw.rect(sc, "green", (x * cub_size, y * cub_size, cub_size - 1, cub_size - 1))
        
    # Отрисовка еды
    if food_type == "apple":
        pygame.draw.rect(sc, "red", (food_pos[0] * cub_size, food_pos[1] * cub_size, cub_size - 1, cub_size - 1))
    elif food_type == "banana":
        pygame.draw.rect(sc, "yellow", (food_pos[0] * cub_size, food_pos[1] * cub_size, cub_size - 1, cub_size - 1))
    elif food_type == "orange":
        pygame.draw.rect(sc, "orange", (food_pos[0] * cub_size, food_pos[1] * cub_size, cub_size - 1, cub_size - 1))

    pygame.display.flip()

    if alive:
        # Движение змеи
        new_pos = snake[0][0] + directions[direction][0], snake[0][1] + directions[direction][1]
        if not (0 <= new_pos[0] < MSIZE[0] and 0 <= new_pos[1] < MSIZE[1]) or new_pos in snake:
            alive = False
        else:
            snake.insert(0, new_pos)
            # Проверка на съеденную еду
            if new_pos == food_pos:
                if food_type == "apple":
                    score +=1
                if food_type == "banana":
                    score += 2
                if food_type == "orange":
                    score += 3
                FPS += 1
                food_type = select_food()
                food_pos = random.randint(0, MSIZE[0]-1), random.randint(0, MSIZE[1]-1)
                food_timer = 0
            else:
                snake.pop(-1)
            food_timer += 1
            # Генерация новой еды, если старая не съедена вовремя
            if food_timer > 50:
                food_type
