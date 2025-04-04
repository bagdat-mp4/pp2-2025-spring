import pygame
import random
import sys

pygame.init()  # Pygame кітапханасын инициализациялау

# Экранның өлшемдері мен клеткалардың өлшемі
WIDTH, HEIGHT = 600, 600  # Экранның ені мен биіктігі
CELL_SIZE = 20  # Әр клетканың өлшемі

# Түстер анықталады
WHITE = (255, 255, 255)  # Ақ түс
GREEN = (0, 255, 0)  # Жасыл түс (Змейканың түсі)
RED = (255, 0, 0)  # Қызыл түс (Тиынның түсі)
BLACK = (0, 0, 0)  # Қара түс (Шрифттің түсі)

# Экранды орнату
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Экранның өлшемдерін орнату
pygame.display.set_caption("Змейка")  # Ойынның атын көрсету

# Шрифт орнату
font = pygame.font.SysFont("Times New Roman", 20)  # Шрифт және оның өлшемі

# Сағат объектісі, ол FPS-ті басқару үшін қажет
clock = pygame.time.Clock()

# Змейканың бастапқы күйі
snake = [(100, 100), (80, 100), (60, 100)]  # Змейканың бастапқы денесі (жолдар)
snake_dir = (20, 0)  # Змейканың бастапқы бағыты (оңға қарай)
food_pos = (random.randrange(0, WIDTH, CELL_SIZE), random.randrange(0, HEIGHT, CELL_SIZE))  # Тиынның кездейсоқ орны
score = 0  # Ұпай саны
level = 1  # Ойынның деңгейі
speed = 10  # Змейканың жылдамдығы

# Тиынды кездейсоқ түрде экранға шығару
def generate_food():
    while True:
        x = random.randrange(0, WIDTH, CELL_SIZE)  # Клетканың х-координатын таңдау
        y = random.randrange(0, HEIGHT, CELL_SIZE)  # Клетканың y-координатын таңдау
        if (x, y) not in snake:  # Егер тиын змейканың ішінде болмаса
            return (x, y)  # Тиынды жаңа орнын қайтару

# Негізгі ойын циклі
while True:
    for event in pygame.event.get():  # Ойынның оқиғаларын өңдеу
        if event.type == pygame.QUIT:  # Егер ойыннан шығу туралы оқиға болса
            pygame.quit()  # Pygame кітапханасын жабу
            sys.exit()  # Бағдарламаны аяқтау

    # Пайдаланушыдан пернелерді басу жайлы ақпарат алу
    keys = pygame.key.get_pressed()  # Пернелердің басылып жатқанын тексеру
    if keys[pygame.K_UP] and snake_dir != (0, 20):  # Егер "UP" пернесі басылған болса және змейка төмен қарай қозғалып жатпаса
        snake_dir = (0, -20)  # Змейканы жоғары бағыттау
    if keys[pygame.K_DOWN] and snake_dir != (0, -20):  # Егер "DOWN" пернесі басылған болса және змейка жоғары қарай қозғалып жатпаса
        snake_dir = (0, 20)  # Змейканы төмен бағыттау
    if keys[pygame.K_LEFT] and snake_dir != (20, 0):  # Егер "LEFT" пернесі басылған болса және змейка оңға қарай қозғалып жатпаса
        snake_dir = (-20, 0)  # Змейканы солға бағыттау
    if keys[pygame.K_RIGHT] and snake_dir != (-20, 0):  # Егер "RIGHT" пернесі басылған болса және змейка солға қарай қозғалып жатпаса
        snake_dir = (20, 0)  # Змейканы оңға бағыттау

    # Змейканың жаңа басын есептеу
    new_head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])

    # Егер змейка экранның шегінен шықса, ойын тоқтайды
    if new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT:
        break  # Ойын аяқталады

    # Егер змейка өз денесімен соқтығысса, ойын тоқтайды
    if new_head in snake:
        break  # Ойын аяқталады

    # Змейканың басын денесінің алдына қосу
    snake.insert(0, new_head)

    # Егер змейка тиынды жесе
    if new_head == food_pos:
        score += 1  # Ұпайды арттыру
        food_pos = generate_food()  # Жаңа тиынның орнын генерациялау

        # Әрбір төртінші тиыннан кейін деңгей мен жылдамдықты арттыру
        if score % 4 == 0:
            level += 1  # Деңгейді арттыру
            speed += 2  # Жылдамдықты арттыру
    else:
        snake.pop()  # Змейканың соңғы сегментін өшіру (жылжуы)

    # Экранды тазалау (ақ түспен толтыру)
    screen.fill(WHITE)

    # Змейканың денесін салу
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))  # Әрбір сегмент үшін жасыл түспен төртбұрыш салу

    # Тиынның орнын салу
    pygame.draw.rect(screen, RED, (food_pos[0], food_pos[1], CELL_SIZE, CELL_SIZE))  # Тиынды қызыл түспен салу

    # Экранға ұпай мен деңгейді көрсету
    score_text = font.render(f"Счет: {score}", True, BLACK)  # Ұпайды текстке айналдыру
    level_text = font.render(f"Уровень: {level}", True, BLACK)  # Деңгейді текстке айналдыру
    screen.blit(score_text, (10, 10))  # Ұпайды экранға шығару
    screen.blit(level_text, (10, 40))  # Деңгейді экранға шығару

    # Экранды жаңарту
    pygame.display.flip()

    # FPS бақылау (ойынның жылдамдығы)
    clock.tick(speed)
