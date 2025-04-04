import pygame
import sys

pygame.init()  # Pygame кітапханасын инициализациялау

# Экранның өлшемдері мен түстер
screen = pygame.display.set_mode((800, 600))  # Экранды 800x600 пиксель өлшемінде орнату
pygame.display.set_caption("paint")  # Ойынның терезесіне "paint" деген ат беру
WHITE = (255, 255, 255)  # Ақ түс
BLACK = (0, 0, 0)  # Қара түс
RED = (255, 0, 0)  # Қызыл түс
GREEN = (0, 255, 0)  # Жасыл түс
BLUE = (0, 0, 255)  # Көк түс
current_color = BLACK  # Бастапқы түс қара

screen.fill(WHITE)  # Экранды ақ түспен толтыру


# Қылқаламның өлшемі мен басқа параметрлер
brush_size = 5  # Қылқаламның өлшемі
drawing = False  # Сурет салу басталғанын тексеретін айнымалы
last_pos = None  # Соңғы сурет салған орнын сақтау
mode = "brush"  # Бастапқы режим - қылқалам (brush)
start_pos = None  # Сурет салуды бастайтын орын

while True:
    for event in pygame.event.get():  # Пайдаланушыдан оқиғаларды алу
        if event.type == pygame.QUIT:  # Егер терезеден шықса
            pygame.quit()  # Pygame кітапханасын жабу
            sys.exit()  # Бағдарламаны тоқтату

        # Пернелерді басқан кезде орындалатын әрекеттер
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:  # Егер R пернесі басылса, түс қызыл болады
                current_color = RED
            elif event.key == pygame.K_g:  # Егер G пернесі басылса, түс жасыл болады
                current_color = GREEN
            elif event.key == pygame.K_b:  # Егер B пернесі басылса, түс көк болады
                current_color = BLUE
            elif event.key == pygame.K_e:  # Өшіргіш режиміне ауысу
                mode = "eraser"
            elif event.key == pygame.K_t:  # Қылқалам режиміне ауысу
                mode = "brush"
            elif event.key == pygame.K_c:  # Шеңбер салу режиміне ауысу
                mode = "circle"
            elif event.key == pygame.K_q:  # Тікбұрыш салу режиміне ауысу
                mode = "square"
            elif event.key == pygame.K_p:  # Тік бұрышты үшбұрыш салу режиміне ауысу
                mode = "right_triangle"
            elif event.key == pygame.K_e:  # Тең бүйірлі үшбұрыш салу режиміне ауысу
                mode = "equilateral_triangle"
            elif event.key == pygame.K_d:  # Ромб салу режиміне ауысу
                mode = "rhombus"
            elif event.key == pygame.K_l:  # Тікбұрыш салу режиміне ауысу
                mode = "rect"

        # Тышқанды басу оқиғасы (сурет салуды бастау)
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True  # Сурет салуды бастау
            start_pos = event.pos  # Сурет салуды бастайтын орын
            last_pos = event.pos  # Соңғы орын

        # Тышқанды босату оқиғасы (сурет салуды аяқтау)
        if event.type == pygame.MOUSEBUTTONUP:
            end_pos = event.pos  # Сурет салуды аяқтаған кезде, соңғы орынды алу

            if mode == "rect":  # Тікбұрыш салу
                # Тікбұрыштың орнын және өлшемін есептеу
                rect = pygame.Rect(min(start_pos[0], end_pos[0]), min(start_pos[1], end_pos[1]),
                                   abs(start_pos[0] - end_pos[0]), abs(start_pos[1] - end_pos[1]))
                pygame.draw.rect(screen, current_color, rect, width=2)  # Тікбұрышты салу

            elif mode == "circle":  # Шеңбер салу
                # Шеңбердің радиусын есептеу
                radius = int(((start_pos[0] - end_pos[0])**2 + (start_pos[1] - end_pos[1])**2) ** 0.5)
                pygame.draw.circle(screen, current_color, start_pos, radius, width=2)  # Шеңбер салу

            elif mode == "square":  # Тік төртбұрыш салу
                # Саңлақтың өлшемі ең үлкен өлшемнің арасында таңдалады (ен немесе биіктік)
                side = max(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1]))
                rect = pygame.Rect(start_pos[0], start_pos[1], side, side)  # Тік төртбұрыш
                pygame.draw.rect(screen, current_color, rect, width=2)  # Тік төртбұрыш салу

            elif mode == "right_triangle":  # Тік бұрышты үшбұрыш салу
                # Үшбұрыштың бұрыштарын есептеу
                x1, y1 = start_pos
                x2, y2 = end_pos
                points = [start_pos, (x1, y2), (x2, y2)]  # Үшбұрыштың үш бұрышын анықтау
                pygame.draw.polygon(screen, current_color, points, width=2)  # Үшбұрыш салу

            elif mode == "equilateral_triangle":  # Тең бүйірлі үшбұрыш салу
                # Тең бүйірлі үшбұрыштың биіктігін есептеу
                x1, y1 = start_pos
                x2, y2 = end_pos
                side = max(abs(x2 - x1), abs(y2 - y1))
                point1 = (x1, y1)
                point2 = (x1 + side, y1)
                point3 = (x1 + side / 2, y1 - (3**0.5/2)*side)  # Үшбұрыштың биіктігін анықтау
                pygame.draw.polygon(screen, current_color, [point1, point2, point3], width=2)  # Үшбұрыш салу

            elif mode == "rhombus":  # Ромб салу
                # Ромбтың бұрыштарын есептеу
                x1, y1 = start_pos
                x2, y2 = end_pos
                center_x = (x1 + x2) // 2  # Орталық x
                center_y = (y1 + y2) // 2  # Орталық y
                dx = abs(x2 - x1) // 2
                dy = abs(y2 - y1) // 2
                points = [
                    (center_x, center_y - dy),  # Ромбтың үстіңгі бұрышы
                    (center_x + dx, center_y),  # Оң жақ бұрышы
                    (center_x, center_y + dy),  # Төменгі бұрышы
                    (center_x - dx, center_y)  # Сол жақ бұрышы
                ]
                pygame.draw.polygon(screen, current_color, points, width=2)  # Ромб салу

            drawing = False  # Сурет салуды тоқтату

        # Тышқанды жылжыту кезінде сурет салу
        if event.type == pygame.MOUSEMOTION and drawing:
            if mode == "brush":  # Қылқалам режимі
                pygame.draw.line(screen, current_color, last_pos, event.pos, brush_size)  # Сызық салу
                last_pos = event.pos  # Соңғы орынды жаңарту
            elif mode == "eraser":  # Өшіргіш режимі
                pygame.draw.line(screen, WHITE, last_pos, event.pos, brush_size * 2)  # Ақ түсті сызықпен өшіру
                last_pos = event.pos  # Соңғы орынды жаңарту

    pygame.display.update()  # Экранды жаңарту























# Пернелер мен олардың функциялары:
# R – Қызыл түс таңдау
# G – Жасыл түс таңдау
# B – Көк түс таңдау
# E – Өшіргіш режимі (сурет өшіру)
# T – Қылқалам режимі (сурет салу)
# C – Шеңбер салу режимі
# Q – Тікбұрыш салу режимі
# P – Тік бұрышты үшбұрыш салу режимі
# E – Тең бүйірлі үшбұрыш салу режимі
# D – Ромб салу режимі
# L – Тікбұрыш салу режимі
