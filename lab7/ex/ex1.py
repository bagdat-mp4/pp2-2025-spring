import pygame
import datetime

# Pygame модулін инициализациялау
pygame.init()

# 📌 Суреттердің толық жолдары (path)
CLOCK_PATH = r"C:\Users\Администратор\Desktop\KBTUpp2\pp2-2025-spring\lab7\images\mickeyWithoutArms.png"  # Сағаттың суреті (фон)
LEFT_ARM_PATH = r"C:\Users\Администратор\Desktop\KBTUpp2\pp2-2025-spring\lab7\images\leftarm.png"         # Сол қол (секунд стрелка)
RIGHT_ARM_PATH = r"C:\Users\Администратор\Desktop\KBTUpp2\pp2-2025-spring\lab7\images\rightarm.png"       # Оң қол (минут стрелка)

# 📌 Экран параметрлері
WIDTH, HEIGHT = 450, 400            # Экран өлшемі
WHITE = (255, 255, 255)             # Ақ түс (фон үшін)

# 📌 Экран құру
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Экранды орнату
pygame.display.set_caption("Mickey Clock")         # Терезе атауын қою

# 📌 Суреттерді жүктеу
clock_img = pygame.image.load(CLOCK_PATH)
left_arm_img = pygame.image.load(LEFT_ARM_PATH)
right_arm_img = pygame.image.load(RIGHT_ARM_PATH)

# 📌 Суреттерді өлшемін өзгерту (масштабтау)
clock_img = pygame.transform.scale(clock_img, (clock_img.get_width() // 3, clock_img.get_height() // 3))
left_arm_img = pygame.transform.scale(left_arm_img, (20, left_arm_img.get_height() // 3 - 20))  # Сол қолды жіңішкерту
right_arm_img = pygame.transform.scale(right_arm_img, (right_arm_img.get_width() // 3, right_arm_img.get_height() // 3))

# 📌 Негізгі цикл (ойын терезесі жабылғанша жұмыс істейді)
running = True
while running:
    # 📌 Оқиғаларды тексеру (оқиғалар қатары)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Егер терезе жабылса
            running = False            # Циклды тоқтатамыз

    # 📌 Нақты уақытты алу
    minute = datetime.datetime.now().minute  # Қазіргі минут
    second = datetime.datetime.now().second  # Қазіргі секунд

    # 📌 Экранды ақ түспен бояу және сағат суретін қою
    screen.fill(WHITE)
    screen.blit(clock_img, (0, 0))  # Сағаттың фонын экранға орналастыру

    # 📌 Минут және секунд стрелкаларының бұрышын есептеу
    left_arm_angle = second * (-6)    # 1 секунд = 6° (-6° бұрышты солға айналдыру)
    right_arm_angle = minute * (-6)   # 1 минут = 6°

    # 📌 Сол қолды (секунд стрелка) айналдыру
    left_rotated = pygame.transform.rotate(left_arm_img, left_arm_angle)  # Секунд стрелканы бұру
    left_rect = left_rotated.get_rect(center=(230, 175))  # Центрін сағаттың ортасына қою

    # 📌 Оң қолды (минут стрелка) айналдыру
    right_rotated = pygame.transform.rotate(right_arm_img, right_arm_angle)  # Минут стрелканы бұру
    right_rect = right_rotated.get_rect(center=(230, 175))

    # 📌 Экранға айналдырылған стрелкаларды орналастыру
    screen.blit(left_rotated, left_rect.topleft)
    screen.blit(right_rotated, right_rect.topleft)

    # 📌 Экранды жаңарту
    pygame.display.update()

    # 📌 FPS орнату (кадрлар жылдамдығы) – 60 FPS
    pygame.time.delay(1000 // 60)

# 📌 Pygame жабу
pygame.quit()
