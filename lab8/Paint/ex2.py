import pygame
import sys

pygame.init()  # Pygame кітапханасын инициализациялау

# Экранның өлшемдері мен түстер
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 20
WHITE = (255, 255, 255)  # Ақ түс
BLACK = (0, 0, 0)  # Қара түс
RED = (255, 0, 0)  # Қызыл түс
GREEN = (0, 255, 0)  # Жасыл түс
BLUE = (0, 0, 255)  # Көк түс
current_color = BLACK  # Бастапқы түс қара

# Экранды орнату
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Экранның өлшемдерін орнату
pygame.display.set_caption("Paint")  # Ойынның атын көрсету

# Шрифт орнату
font = pygame.font.SysFont("Times New Roman", 20)  # Шрифт және оның өлшемі

# Экранды ақ түспен толтыру
screen.fill(WHITE)

# Түсті таңдау батырмаларының өлшемдері
button_width = 50
button_height = 50

brush_size = 5  # Қылқаламның өлшемі
drawing = False  # Сурет салу басталғанын тексеретін айнымалы
last_pos = None  # Соңғы сурет салған орнын сақтау
mode = "brush"  # Бастапқы режим - қылқалам (brush)
start_pos = None  # Сурет салуды бастайтын орын

# Түстердің батырмаларының орналасу координаттары
color_buttons = {
    'red': (10, 10),
    'green': (70, 10),
    'blue': (130, 10),
    'black': (190, 10),
}

def draw_color_buttons():
    """Түстерді таңдау батырмаларын салу"""
    pygame.draw.rect(screen, RED, (color_buttons['red'][0], color_buttons['red'][1], button_width, button_height))  # Қызыл түсті батырма
    pygame.draw.rect(screen, GREEN, (color_buttons['green'][0], color_buttons['green'][1], button_width, button_height))  # Жасыл түсті батырма
    pygame.draw.rect(screen, BLUE, (color_buttons['blue'][0], color_buttons['blue'][1], button_width, button_height))  # Көк түсті батырма
    pygame.draw.rect(screen, BLACK, (color_buttons['black'][0], color_buttons['black'][1], button_width, button_height))  # Қара түсті батырма

while True:
    for event in pygame.event.get():  # Пайдаланушыдан оқиғаларды алу
        if event.type == pygame.QUIT:  # Егер терезеден шықса
            pygame.quit()  # Pygame кітапханасын жабу
            sys.exit()  # Бағдарламаны тоқтату

        if event.type == pygame.KEYDOWN:  # Егер пернелер басылса
            if event.key == pygame.K_e:  # Өшіргіш режиміне ауысу
                mode = "eraser"
            elif event.key == pygame.K_t:  # Қылқалам режиміне ауысу
                mode = "brush"
            elif event.key == pygame.K_c:  # Шеңбер салу режиміне ауысу
                mode = "circle"
            elif event.key == pygame.K_r:  # Тікбұрыш салу режиміне ауысу
                mode = "rect"

        if event.type == pygame.MOUSEBUTTONDOWN:  # Егер тышқан басылса
            drawing = True  # Сурет салу басталды
            start_pos = event.pos  # Сурет салуды бастайтын орын
            last_pos = event.pos  # Соңғы орын

            # Түстердің батырмаларына басылғанын тексеру
            if color_buttons['red'][0] < event.pos[0] < color_buttons['red'][0] + button_width and \
                    color_buttons['red'][1] < event.pos[1] < color_buttons['red'][1] + button_height:
                current_color = RED  # Қызыл түсті таңдау
            elif color_buttons['green'][0] < event.pos[0] < color_buttons['green'][0] + button_width and \
                    color_buttons['green'][1] < event.pos[1] < color_buttons['green'][1] + button_height:
                current_color = GREEN  # Жасыл түсті таңдау
            elif color_buttons['blue'][0] < event.pos[0] < color_buttons['blue'][0] + button_width and \
                    color_buttons['blue'][1] < event.pos[1] < color_buttons['blue'][1] + button_height:
                current_color = BLUE  # Көк түсті таңдау
            elif color_buttons['black'][0] < event.pos[0] < color_buttons['black'][0] + button_width and \
                    color_buttons['black'][1] < event.pos[1] < color_buttons['black'][1] + button_height:
                current_color = BLACK  # Қара түсті таңдау

        # Тышқанды босату кезінде орындалатын әрекеттер
        if event.type == pygame.MOUSEBUTTONUP:  
            if mode == "rect":  # Тікбұрыш салу
                end_pos = event.pos  # Суреттің соңғы орнын алу
                rect = pygame.Rect(min(start_pos[0], end_pos[0]), min(start_pos[1], end_pos[1]),  # Тікбұрыштың орнын және өлшемін есептеу
                                   abs(start_pos[0] - end_pos[0]), abs(start_pos[1] - end_pos[1]))
                pygame.draw.rect(screen, current_color, rect, width=2)  # Тікбұрышты салу

            elif mode == "circle":  # Шеңбер салу
                end_pos = event.pos  # Суреттің соңғы орнын алу
                radius = int(((start_pos[0] - end_pos[0]) ** 2 + (start_pos[1] - end_pos[1]) ** 2) ** 0.5)  # Шеңбердің радиусын есептеу
                pygame.draw.circle(screen, current_color, start_pos, radius, width=2)  # Шеңберді салу

            drawing = False  # Сурет салуды тоқтату

        # Тышқанды жылжыту кезінде сурет салу
        if event.type == pygame.MOUSEMOTION and drawing:
            if mode == "brush":  # Қылқалам режимі
                pygame.draw.line(screen, current_color, last_pos, event.pos, brush_size)  # Сызық салу
                last_pos = event.pos  # Соңғы орын ретінде ағымдағы орынды сақтау
            elif mode == "eraser":  # Өшіргіш режимі
                pygame.draw.line(screen, WHITE, last_pos, event.pos, brush_size * 2)  # Ақ түсті сызықпен өшіру
                last_pos = event.pos  # Соңғы орын ретінде ағымдағы орынды сақтау

    # Түстерді таңдау батырмаларын салу
    draw_color_buttons()
    pygame.display.update()  # Экранды жаңарту