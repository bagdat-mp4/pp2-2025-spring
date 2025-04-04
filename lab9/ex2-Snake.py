import pygame
import random
import sys
import time

pygame.init()  # Pygame кітапханасын инициализациялау

# Экранның өлшемдері мен түстер
WIDTH, HEIGHT = 600, 600  # Экранның ұзындығы мен биіктігі
CELL_SIZE = 20  # Әрбір ұяшықтың өлшемі
WHITE = (255, 255, 255)  # Ақ түс
GREEN = (0, 255, 0)  # Змейканың түсі
BLACK = (0, 0, 0)  # Мәтіннің түсі
FPS = 10  # Ойынның жылдамдығы (фрейм/сек)

# Тағамның салмағына байланысты түстері
FOOD_COLORS = {
    1: (255, 0, 0),  # Қызыл түс - салмақ 1
    2: (255, 165, 0),  # Сары түс - салмақ 2
    3: (255, 255, 0)  # Жасыл түс - салмақ 3
}

# Экранды орнату
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Экранның өлшемдерін орнату
pygame.display.set_caption("Змейка")  # Ойынның терезесіне ат беру
font = pygame.font.SysFont("Times New Roman", 20)  # Шрифт орнату
clock = pygame.time.Clock()  # Часовой механизм (фреймдерді басқару)

# Змейканың бастапқы күйі
snake = [(100, 100), (80, 100), (60, 100)]  # Змейканың денесі
snake_dir = (20, 0)  # Змейканың бастапқы бағыты

# Тағамның бастапқы күйі
food_pos = None  # Тағамның бастапқы орны
food_weight = 1  # Тағамның бастапқы салмағы
food_spawn_time = 0  # Тағамның пайда болған уақыты

# Ойынның негізгі айнымалылары
score = 0  # Нәтиже
level = 1  # Деңгей
speed = 10  # Жылдамдық

# Тағамды кездейсоқ генерациялау функциясы
def generate_food():
    while True:  # Кездейсоқ тағам орындарын таңдауды қайталау
        x = random.randrange(0, WIDTH, CELL_SIZE)  # Кездейсоқ X координатасы
        y = random.randrange(0, HEIGHT, CELL_SIZE)  # Кездейсоқ Y координатасы
        if (x, y) not in snake:  # Егер тағам змейканың денесіне түссе, жаңа орын генерациялау
            return (x, y), random.choice([1, 2, 3])  # Тағамды кездейсоқ генерациялау, салмағын 1, 2 немесе 3

# Тағамды генерациялау және оның бастапқы күйін орнату
food_pos, food_weight = generate_food()  # Тағамның орны мен салмағын орнату
food_spawn_time = time.time()  # Тағамның пайда болған уақытын сақтау

# Ойын циклі
while True:
    for event in pygame.event.get():  # Пайдаланушының іс-әрекеттерін тексеру
        if event.type == pygame.QUIT:  # Егер терезе жабылса
            pygame.quit()  # Pygame кітапханасын жабу
            sys.exit()  # Бағдарламаны тоқтату

    # Змейканың бағытын өзгерту
    keys = pygame.key.get_pressed()  # Пайдаланушының басқан пернелерін тексеру
    if keys[pygame.K_UP] and snake_dir != (0, 20):  # Жоғары бағытта қозғалуға тексеру
        snake_dir = (0, -20)
    if keys[pygame.K_DOWN] and snake_dir != (0, -20):  # Төмен бағытта қозғалуға тексеру
        snake_dir = (0, 20)
    if keys[pygame.K_LEFT] and snake_dir != (20, 0):  # Солға бағытта қозғалуға тексеру
        snake_dir = (-20, 0)
    if keys[pygame.K_RIGHT] and snake_dir != (-20, 0):  # Оңға бағытта қозғалуға тексеру
        snake_dir = (20, 0)

    # Жаңа бастың позициясын есептеу
    new_head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])

    # Змейканың өзіне соқтығуын немесе экран шекарасынан шығуын тексеру
    if (
        new_head[0] < 0 or new_head[0] >= WIDTH or
        new_head[1] < 0 or new_head[1] >= HEIGHT or
        new_head in snake  # Змейка өзінің денесіне соғылғанда
    ):
        break  # Ойын тоқтатылады

    snake.insert(0, new_head)  # Жаңа бастың позициясын қосу

    # Егер змейка тағамды жесе
    if new_head == food_pos:
        score += food_weight  # Тағамның салмағына байланысты балл қосу
        food_pos, food_weight = generate_food()  # Жаңа тағам генерациялау
        food_spawn_time = time.time()  # Тағамның жаңа пайда болу уақытын сақтау
        if score // 4 + 1 > level:  # Деңгей өзгерісі
            level += 1
            speed += 2  # Жылдамдықты арттыру
    else:
        snake.pop()  # Змейканың соңғы бөлігін алып тастау (қозғалыс)

    # Егер тағам 5 секунд өткеннен кейін жоғалып кетсе
    if time.time() - food_spawn_time >= 5:
        food_pos, food_weight = generate_food()  # Жаңа тағам генерациялау
        food_spawn_time = time.time()  # Тағамның жаңа уақытын сақтау

    screen.fill(WHITE)  # Экранды тазарту

    # Змейканы экранда көрсету
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))  # Змейканы жасыл түспен көрсету

    # Тағамды экранда көрсету (түріне байланысты түсті көрсету)
    food_color = FOOD_COLORS[food_weight]  # Тағамның түсі салмағына байланысты
    pygame.draw.rect(screen, food_color, (food_pos[0], food_pos[1], CELL_SIZE, CELL_SIZE))  # Тағамды салу

    # Нәтижені және деңгейді экранға шығару
    score_text = font.render(f"Счет: {score}", True, BLACK)  # Нәтижені көрсету
    level_text = font.render(f"Уровень: {level}", True, BLACK)  # Деңгейді көрсету
    screen.blit(score_text, (10, 10))  # Нәтижені экранда шығару
    screen.blit(level_text, (10, 40))  # Деңгейді экранда шығару

    pygame.display.flip()  # Экранды жаңарту
    clock.tick(speed)  # Жылдамдықты бақылау (фреймдер/сек)
  







 #  Randomly generating food with different weights — Тағамды кездейсоқ салмақпен генерациялау, мұнда әрбір тағамның салмағы 1, 2 немесе 3 болады. Әр салмаққа сәйкес түрлі түстер таңдалады.

  #   Foods which are disappearing after some time(timer) — 5 секунд өткен соң тағам автоматты түрде жоғалып, жаңа тағам генерацияланады.