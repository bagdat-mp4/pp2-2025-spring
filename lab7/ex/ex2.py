import pygame  # Pygame кітапханасын қосамыз (ойын жасауға, графика және дыбыс ойнатуға арналған)
import os      # Операциялық жүйемен жұмыс істеу үшін os кітапханасын қосамыз

pygame.init()  # Pygame-ді инициализациялау (ішкі жүйелерін дайындау)

# Терезенің ені мен биіктігі
WIDTH, HEIGHT = 500, 500
# Негізгі экранды (терезені) орнатамыз
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# Терезенің атауын орнатамыз
pygame.display.set_caption("Music Player")

# Түстерді RGB форматында сипаттаймыз
black = (0, 0, 0)
white = (255, 255, 255)
gray = (200, 200, 200)

# Музыка файлдары орналасқан папканың жолы
MUSIC_FOLDER = r"C:\Users\Администратор\Desktop\KBTUpp2\pp2-2025-spring\lab7\sounds"

# Папканың бар-жоғын тексереміз
if not os.path.exists(MUSIC_FOLDER):
    print(f"Ошибка: Папка '{MUSIC_FOLDER}' не найдена!")
    exit()  # Егер жоқ болса, бағдарламаны жабамыз

# Папка ішіндегі барлық .mp3 файлдарын тізімге жинаймыз
sounds = [os.path.join(MUSIC_FOLDER, f) for f in os.listdir(MUSIC_FOLDER) if f.endswith(".mp3")]

# Егер ешқандай MP3-файл табылмаса, бағдарламаны жабамыз
if not sounds:
    print(f"Ошибка: В папке '{MUSIC_FOLDER}' нет MP3-файлов!")
    exit()

# Трек индексін (қай трек ойналып жатқанын) сақтайтын айнымалы
index = 0  
# Музыканың тоқтатылған/тоқтатылмағанын бақылайтын айнымалы
isPaused = False

# Шрифтті инициализациялау
pygame.font.init()
# Мәтінді шығару үшін 36 өлшемді шрифт қолданамыз
font = pygame.font.Font(None, 36)

def draw_button(text, x, y, width, height):
    """
    Берілген координаттар бойынша тікбұрышты батырма салып,
    оның ішіне мәтінді орналастырады. Пайдаланушы шертуді тексеру үшін
    осы батырманың Rect объектісін қайтарамыз.
    """
    rect = pygame.Rect(x, y, width, height)
    pygame.draw.rect(screen, gray, rect, border_radius=5)  # Батырманың сұр тікбұрышын салу
    text_surface = font.render(text, True, black)          # Батырмадағы мәтін
    screen.blit(text_surface, (x + 10, y + 10))            # Мәтінді батырманың үстіне орналастыру
    return rect                                           # Батырманың Rect объектісін қайтарамыз

def play_music():
    """
    Әлемдік (global) isPaused айнымалысын жаңартып,
    ағымдағы индекстегі (index) музыканы жүктеп, ойнатады.
    """
    global isPaused
    pygame.mixer.music.load(sounds[index])  # sounds тізімінен ағымдағы тректі жүктеу
    pygame.mixer.music.play()              # Ойнатуды бастау
    isPaused = False                       # Тоқтатылған емес күйге ауыстыру

running = True  # Негізгі цикл жалғасып тұрғанын білдіретін айнымалы
while running:
    screen.fill(black)  # Экранды қара түспен бояймыз
    
    # Батырмаларды саламыз
    play_btn = draw_button("Play", 50, 400, 100, 50)
    pause_btn = draw_button("Pause", 200, 400, 100, 50)
    next_btn = draw_button("Next", 350, 400, 100, 50)
    prev_btn = draw_button("Previous", 50, 300, 150, 50)

    # Оқиғаларды (event) тексереміз
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # Егер терезені жабу оқиғасы болса, негізгі циклді тоқтатамыз

        if event.type == pygame.MOUSEBUTTONDOWN:
            # Тышқан батырмасын басу оқиғасы
            if play_btn.collidepoint(event.pos):
                # Егер Play батырмасы басылса
                play_music()
            elif pause_btn.collidepoint(event.pos):
                # Егер Pause батырмасы басылса
                pygame.mixer.music.pause()  # Музыканы уақытша тоқтату
                isPaused = True
            elif next_btn.collidepoint(event.pos):
                # Егер Next батырмасы басылса, келесі трекке ауысу
                index = (index + 1) % len(sounds)
                play_music()
            elif prev_btn.collidepoint(event.pos):
                # Егер Previous батырмасы басылса, алдыңғы трекке ауысу
                index = (index - 1) % len(sounds)
                play_music()
    
    pygame.display.flip()  # Экранды жаңарту (бейнені көрсету)

pygame.quit()  # Негізгі циклден шыққан соң, Pygame-ді дұрыс жауып шығамыз
