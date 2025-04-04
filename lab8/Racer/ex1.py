import pygame
from pygame.locals import *  # Барлық Pygame функцияларын импорттау
import random 
import time

pygame.init()  # Pygame кітапханасын инициализациялау

# Ойынның негізгі параметрлері
FPS = 120  # Ойынның кадр саны (Frames per second)
FramePerSec = pygame.time.Clock()  # FPS үшін уақытты бақылаушы объект
SCREEN_WIDTH = 400  # Экранның ені
SCREEN_HEIGHT = 600  # Экранның биіктігі
SPEED = 5  # Ойынның жылдамдығы
SCORE = 0  # Ойынның ағымдағы ұпайы
COINS_COLLECTED = 0  # Жиналған тиындар саны

coin_sound = pygame.mixer.Sound("lab8\Racer\sounds\звук монеты.mp3")  # Тиын жинаған кезде шығатын дыбыс

# Шрифттер
font = pygame.font.SysFont("Verdana", 60)  # Үлкен шрифт (ойынның соңындағы "Game Over")
font_small = pygame.font.SysFont("Times New Roman", 20)  # Кіші шрифт (негізгі ұпай мен тиын саны үшін)
game_over = font.render("Game Over", True, (0, 0, 0))  # "Game Over" мәтінін жасау

# Фонды жүктеу
background = pygame.image.load("lab8\Racer\images\street.png")

# Фондық музыка жүктеу және ойнату
pygame.mixer.music.load("lab8\Racer\sounds\Lectures_Lecture8_racer_resources_background.wav")
pygame.mixer.music.play(-1)  # Фондық музыка шексіз қайталанып ойналады

# Экранды дайындау
DISPLAY = pygame.display.set_mode((400, 600))  # Экран өлшемдерін орнату
DISPLAY.fill((255, 255, 255))  # Экранды ақ түспен толтыру
pygame.display.set_caption("GAME")  # Ойынның атауын көрсету

# Враг объектісін құру
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()  # Атасының (Sprite) __init__ конструкторын шақыру
        self.image = pygame.image.load("lab8\Racer\images\enemy.png")  # Враг суретін жүктеу
        self.image = pygame.transform.scale(self.image, (50, 100))  # Суреттің өлшемін өзгерту
        self.rect = self.image.get_rect()  # Суреттің шаршы тәрізді орнын алу
        self.rect.center = (random.randint(20, SCREEN_WIDTH - 20), 0)  # Врагтың бастапқы орны

    def move(self):
        global SCORE  # Глобальды SCORE айнымаласын пайдалану
        self.rect.move_ip(0, SPEED)  # Врагты төмен жылжыту
        if self.rect.bottom > 600:  # Егер враг экранның төменгі шегіне жетсе
            SCORE += 1  # Ұпайды бірден арттыру
            self.rect.top = 0  # Врагты қайта жоғарыдан бастап орнату
            self.rect.center = (random.randint(20, SCREEN_WIDTH - 20), 0)  # Врагтың жаңа орны

# Ойыншы объектісін құру
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("lab8\Racer\images\player.png")  # Ойыншы суретін жүктеу
        self.image = pygame.transform.scale(self.image, (50, 100))  # Суреттің өлшемін өзгерту
        self.rect = self.image.get_rect()  # Ойыншының орнын алу
        self.rect.center = (207, 520)  # Ойыншының бастапқы орнын орнату

    def move(self):
        pressed_keys = pygame.key.get_pressed()  # Қолданушы қандай пернелерді басқанын алу
        if self.rect.left > 0:  # Ойыншы экранның сол жақ шегінен шықпау үшін
            if pressed_keys[K_LEFT]:  # Солға жылжыту пернесі
                self.rect.move_ip(-5, 0)  # Солға 5 пиксель жылжу
        if self.rect.right < SCREEN_WIDTH:  # Ойыншы экранның оң жақ шегінен шықпау үшін
            if pressed_keys[K_RIGHT]:  # Оңға жылжыту пернесі
                self.rect.move_ip(5, 0)  # Оңға 5 пиксель жылжу

# Тиын объектісін құру
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.original_image = pygame.image.load("lab8\Racer\images\photo_2025-04-04_14-15-14.jpg")  # Тиын суретін жүктеу
        self.image = pygame.transform.scale(self.original_image, (40, 40))  # Суреттің өлшемін өзгерту
        self.rect = self.image.get_rect()  # Тиынның орнын алу
        self.respawn()  # Тиынды қайта орналастыру

    def respawn(self):  # Тиынды кездейсоқ түрде экранның жоғарғы жағынан орналастыру
        self.rect.center = (random.randint(20, SCREEN_WIDTH - 20), 0)

    def move(self):
        self.rect.move_ip(0, SPEED // 2)  # Тиынды төмен жылжыту (жылдамдығы сәл төмен)
        if self.rect.top > SCREEN_HEIGHT:  # Егер тиын экранның төменгі шегіне жетсе
            self.respawn()  # Тиынды қайта орналастыру

# Ойын объектілерін құру
P1 = Player()  # Ойыншы объектісін құру
E1 = Enemy()  # Враг объектісін құру
C1 = Coin()  # Тиын объектісін құру

# Группалар құру
enemies = pygame.sprite.Group()  # Врагтарды топтау
enemies.add(E1)
coins = pygame.sprite.Group()  # Тиындарды топтау
coins.add(C1)
all_sprites = pygame.sprite.Group()  # Барлық спрайттарды топтау
all_sprites.add(P1, E1, C1)

# Ойын жылдамдығын уақыт өте өсіру үшін уақыт оқиғасын орнату
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:  # Ойын жылдамдығын арттыру
            SPEED += 0.3
        if event.type == QUIT:  # Ойыннан шығу
            pygame.quit()

    DISPLAY.blit(background, (0, 0))  # Фонды экранға қою

    # Ұпай мен тиындар санын көрсету
    scores = font_small.render(str(SCORE), True, (0, 0, 0))
    DISPLAY.blit(scores, (10, 10))
    coins_collected_text = font_small.render(f"Coins: {COINS_COLLECTED}", True, (0, 0, 0))
    DISPLAY.blit(coins_collected_text, (300, 10))

    # Барлық объектілерді экранға шығару және олардың қозғалысын басқару
    for entity in all_sprites:
        if isinstance(entity, Enemy) or isinstance(entity, Player) or isinstance(entity, Coin):
            entity.move()
        DISPLAY.blit(entity.image, entity.rect)

    # Ойыншы мен враг арасындағы соқтығысты тексеру
    if pygame.sprite.spritecollideany(P1, enemies):  # Егер ойыншы врагпен соқтығысса
        pygame.mixer.music.stop()  # Фондық музыканы тоқтату
        pygame.mixer.Sound("lab8\Racer\sounds\Lectures_Lecture8_racer_resources_crash.wav").play()  # Дыбыс ойнату
        time.sleep(0.7)  # Ойыннан кейін кідіріс
        DISPLAY.fill((255, 0, 0))  # Экранды қызыл түспен толтыру
        DISPLAY.blit(game_over, (30, 250))  # "Game Over" мәтінін шығару
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()  # Барлық объектілерді жою
        time.sleep(1)  # Ойынның бітуі
        pygame.quit()

    # Ойыншы мен тиын арасындағы соқтығысты тексеру
    if pygame.sprite.spritecollideany(P1, coins):  # Егер ойыншы тиынмен соқтығысса
        COINS_COLLECTED += 1  # Тиындар санына бір қосу
        coin_sound.play()  # Тиын дыбысын ойнату
        C1.respawn()  # Тиынды қайта орналастыру

    pygame.display.update()  # Экранды жаңарту
    FramePerSec.tick(FPS)  # FPS бойынша кадрларды бақылау
