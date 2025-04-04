import pygame
from pygame.locals import *
import random
import time

pygame.init()
FPS = 120
FramePerSec = pygame.time.Clock()


SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COINS_COLLECTED = 0
PREV_MILESTONE = 0 


coin_sound = pygame.mixer.Sound("lab8\Racer\sounds\звук монеты.mp3")


DISPLAY = pygame.display.set_mode((400, 600))
DISPLAY.fill((255, 255, 255))
pygame.display.set_caption("GAME")

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Times New Roman", 20)
game_over = font.render("Game Over", True, (0, 0, 0))

background = pygame.image.load("lab8\Racer\images\street.png")
pygame.mixer.music.load("lab8\Racer\sounds\Lectures_Lecture8_racer_resources_background.wav")
pygame.mixer.music.play(-1)




class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("lab8\Racer\images\enemy.png")
        self.image = pygame.transform.scale(self.image, (50, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(20, SCREEN_WIDTH - 20), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.bottom > 600:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(20, SCREEN_WIDTH - 20), 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("lab8\Racer\images\player.png")
        self.image = pygame.transform.scale(self.image, (50, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (207, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0 and pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH and pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.respawn()

    def respawn(self):
        weights = [1, 2, 3]  
        self.weight = random.choice(weights) 

       
        image_path = f"lab8\Racer\images\coin{self.weight}.jpg"
        self.original_image = pygame.image.load("lab8\Racer\images\coin1.png")
        size = 30 + self.weight * 5 
        self.image = pygame.transform.scale(self.original_image, (size, size))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(20, SCREEN_WIDTH - 20), 0)

    def move(self):
        self.rect.move_ip(0, SPEED // 2)
        if self.rect.top > SCREEN_HEIGHT:
            self.respawn()


P1 = Player()
E1 = Enemy()
C1 = Coin()

enemies = pygame.sprite.Group()
enemies.add(E1)

coins = pygame.sprite.Group()
coins.add(C1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1, E1, C1)

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)


while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.3
        if event.type == QUIT:
            pygame.quit()

    DISPLAY.blit(background, (0, 0))

 
    scores = font_small.render(str(SCORE), True, (0, 0, 0))
    DISPLAY.blit(scores, (10, 10))
    coins_collected_text = font_small.render(f"Coins: {COINS_COLLECTED}", True, (0, 0, 0))
    DISPLAY.blit(coins_collected_text, (300, 10))

    
    for entity in all_sprites:
        entity.move()
        DISPLAY.blit(entity.image, entity.rect)

  
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.music.stop()
        pygame.mixer.Sound("lab8\Racer\sounds\Lectures_Lecture8_racer_resources_crash.wav").play()
        time.sleep(0.7)
        DISPLAY.fill((255, 0, 0))
        DISPLAY.blit(game_over, (30, 250))
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(1)
        pygame.quit()


    if pygame.sprite.spritecollideany(P1, coins):
        COINS_COLLECTED += C1.weight
        coin_sound.play()
        C1.respawn()

      
        if COINS_COLLECTED // 10 > PREV_MILESTONE:
            SPEED += 0.5
            PREV_MILESTONE = COINS_COLLECTED // 10

    pygame.display.update()
    FramePerSec.tick(FPS)










#Жолда әртүрлі салмақтары бар монеталарды кездейсоқ генерациялау

#Ойыншы N монета жинаған кезде жаудың жылдамдығын арттыру