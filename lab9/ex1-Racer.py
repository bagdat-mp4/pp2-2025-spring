import pygame
from pygame.locals import *
import random
import time

pygame.init()  # Pygame кітапханасын инициализациялау

# FPS (фреймдер саны) мен ойынның жылдамдығын орнату
FPS = 120
FramePerSec = pygame.time.Clock()

# Экранның өлшемдері мен жылдамдық
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5  # Жылдамдықты бастапқы мәнде орнату
SCORE = 0  # Бастапқы нәтиже
COINS_COLLECTED = 0  # Жиналған монеталар саны
PREV_MILESTONE = 0  # Алдыңғы шекті деңгей

# Тағамның дыбысы
coin_sound = pygame.mixer.Sound("lab8\Racer\sounds\звук монеты.mp3")

# Экранды орнату және фонын көрсету
DISPLAY = pygame.display.set_mode((400, 600))  # Экранның өлшемдері
DISPLAY.fill((255, 255, 255))  # Экранды ақ түспен толтыру
pygame.display.set_caption("GAME")  # Ойынның атауын орнату

# Шрифт орнату
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Times New Roman", 20)
game_over = font.render("Game Over", True, (0, 0, 0))

# Фонның суретін жүктеу
background = pygame.image.load("lab8\Racer\images\street.png")

# Фондық музыканы орнату және іске қосу
pygame.mixer.music.load("lab8\Racer\sounds\Lectures_Lecture8_racer_resources_background.wav")
pygame.mixer.music.play(-1)  # Музыканы қайталап ойнау

# Enemy (жау) класын анықтау
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()  # Sprite класынан тұқым қуалау
        self.image = pygame.image.load("lab8\Racer\images\enemy.png")  # Жау суретін жүктеу
        self.image = pygame.transform.scale(self.image, (50, 100))  # Жау суретін өлшемдеу
        self.rect = self.image.get_rect()  # Жау үшін тікбұрышты объект құру
        self.rect.center = (random.randint(20, SCREEN_WIDTH - 20), 0)  # Жауды экранда кездейсоқ орналастыру

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)  # Жау төмен жылжиды
        if self.rect.bottom > 600:  # Егер жау экраннан тыс түссе
            SCORE += 1  # Нәтижені арттыру
            self.rect.top = 0  # Жауды экранның жоғарғы жағынан қайта көрсету
            self.rect.center = (random.randint(20, SCREEN_WIDTH - 20), 0)  # Жауды жаңа орынға орналастыру

# Player (ойыншы) класын анықтау
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()  # Sprite класынан тұқым қуалау
        self.image = pygame.image.load("lab8\Racer\images\player.png")  # Ойыншының суретін жүктеу
        self.image = pygame.transform.scale(self.image, (50, 100))  # Ойыншының өлшемін өзгерту
        self.rect = self.image.get_rect()  # Ойыншы үшін тікбұрышты объект құру
        self.rect.center = (207, 520)  # Ойыншының бастапқы орны

    def move(self):
        pressed_keys = pygame.key.get_pressed()  # Қандай пернелер басылғанын тексеру
        if self.rect.left > 0 and pressed_keys[K_LEFT]:  # Солға жылжу
            self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH and pressed_keys[K_RIGHT]:  # Оңға жылжу
            self.rect.move_ip(5, 0)

# Coin (монета) класын анықтау
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.respawn()  # Монетаны қайта пайда ету

    def respawn(self):
        weights = [1, 2, 3]  # Монеталардың салмақтары
        self.weight = random.choice(weights)  # Монетаның салмағын кездейсоқ таңдау

        image_path = f"lab8\Racer\images\coin{self.weight}.jpg"  # Монетаның суреті
        self.original_image = pygame.image.load("lab8\Racer\images\coin1.png")  # Негізгі суретті жүктеу
        size = 30 + self.weight * 5  # Монетаның өлшемі салмаққа байланысты
        self.image = pygame.transform.scale(self.original_image, (size, size))  # Суретті өзгерту
        self.rect = self.image.get_rect()  # Тікбұрышты объект құру
        self.rect.center = (random.randint(20, SCREEN_WIDTH - 20), 0)  # Монетаның орны

    def move(self):
        self.rect.move_ip(0, SPEED // 2)  # Монетаның төмен жылжуы
        if self.rect.top > SCREEN_HEIGHT:  # Егер монета экранның төменгі шекарасына жетсе
            self.respawn()  # Монетаны қайта пайда ету

# Ойын объектілерін жасау
P1 = Player()  # Ойыншы объектісі
E1 = Enemy()  # Жау объектісі
C1 = Coin()  # Монета объектісі

# Sprite топтарын жасау
enemies = pygame.sprite.Group()
enemies.add(E1)

coins = pygame.sprite.Group()
coins.add(C1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1, E1, C1)

# Жылдамдықты арттыру үшін таймер орнату
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Ойынның басты циклі
while True:
    for event in pygame.event.get():  # Пайдаланушыдан оқиғаларды алу
        if event.type == INC_SPEED:
            SPEED += 0.3  # Жылдамдықты 0.3 арттыру
        if event.type == QUIT:
            pygame.quit()  # Ойынды жабу

    DISPLAY.blit(background, (0, 0))  # Фонды орнату

    # Нәтиже мен монеталарды көрсету
    scores = font_small.render(str(SCORE), True, (0, 0, 0))  # Нәтижені көрсету
    DISPLAY.blit(scores, (10, 10))
    coins_collected_text = font_small.render(f"Coins: {COINS_COLLECTED}", True, (0, 0, 0))  # Монеталар саны
    DISPLAY.blit(coins_collected_text, (300, 10))

    # Ойын объектілерін жылжыту және экранға шығару
    for entity in all_sprites:
        entity.move()  # Барлық объектілерді жылжыту
        DISPLAY.blit(entity.image, entity.rect)  # Ойынды көрсету

    # Егер ойыншы мен жау соқтығысса
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.music.stop()  # Музыканы тоқтату
        pygame.mixer.Sound("lab8\Racer\sounds\Lectures_Lecture8_racer_resources_crash.wav").play()  # Дауыс қосу
        time.sleep(0.7)  # Ойынды тоқтату
        DISPLAY.fill((255, 0, 0))  # Экранды қызыл түспен толтыру
        DISPLAY.blit(game_over, (30, 250))  # "Game Over" жазуын шығару
        pygame.display.update()  # Экранды жаңарту
        for entity in all_sprites:
            entity.kill()  # Барлық объектілерді жою
        time.sleep(1)  # 1 секунд күту
        pygame.quit()  # Oйынды жабу

    # Ойыншы монетаға соқтығысса
    if pygame.sprite.spritecollideany(P1, coins):
        COINS_COLLECTED += C1.weight  # Монетаның салмағына байланысты балл қосу
        coin_sound.play()  # Дауыс қосу
        C1.respawn()  # Жаңа монетаны генерациялау

        # Монеталар жинаған сайын жылдамдықты арттыру
        if COINS_COLLECTED // 10 > PREV_MILESTONE:
            SPEED += 0.5  # Жылдамдықты арттыру
            PREV_MILESTONE = COINS_COLLECTED // 10  # Алдыңғы шекті жаңарту

    pygame.display.update()  # Экранды жаңарту
    FramePerSec.tick(FPS)  # Жылдамдықты басқару








#Жолда әртүрлі салмақтары бар монеталарды кездейсоқ генерациялау

#Ойыншы N монета жинаған кезде жаудың жылдамдығын арттыру