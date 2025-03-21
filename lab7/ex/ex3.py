import pygame  # Pygame кітапханасын қосамыз: графикалық интерфейс және оқиғаларды басқару үшін қажет

pygame.init()  # Pygame-ді инициализациялаймыз, барлық модульдерді іске қосамыз
screen = pygame.display.set_mode((500, 500))  # 500x500 өлшемді терезе жасаймыз
fon = (255, 255, 255)  # Ақ түс анықталды (RGB: 255, 255, 255)
screen.fill(fon)  # Терезені ақ түспен толтырамыз
isDone = True  # Негізгі циклдың жұмысын басқаратын айнымалы
mainCoordX = 250  # Шардың бастапқы X координатасы: экранның ортасы (500/2)
mainCoordY = 250  # Шардың бастапқы Y координатасы: экранның ортасы (500/2)

while isDone:  # Негізгі цикл: бағдарлама жұмыс істеп тұрғанша орындалады
    screen.fill(fon)  # Әр цикл сайын экранды ақ түспен қайта толтырамыз (ескі шарды жою үшін)
    
    # Қызыл шарды сызамыз: (mainCoordX, mainCoordY) - шардың ортасы, 25 - радиусы
    pygame.draw.circle(screen, 'Red', (mainCoordX, mainCoordY), 25)
    
    pygame.display.update()  # Экранды жаңартамыз: сызылған шар мен фон көрсетіледі
    
    # Оқиғаларды (event) тексеру:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Егер терезе жабылу оқиғасы болса
            isDone = False  # Негізгі циклді тоқтатамыз
            pygame.quit()  # Pygame-ді дұрыс жабамыз
        
        # Пернетақтадан батырма басылғанын тексереміз
        elif event.type == pygame.KEYDOWN:
            # Жоғары бағыт (UP) пернесі басылса
            if event.key == pygame.K_UP:
                # Шардың жоғарғы шеті экран шегінен аспауын тексереміз:
                # mainCoordY - 20 (қозғалыс қашықтығы) - 25 (радиус) >= 0
                if mainCoordY - 20 - 25 >= 0:
                    mainCoordY -= 20  # Шарды 20 пиксель жоғары жылжытамыз

            # Төмен бағыт (DOWN) пернесі басылса
            if event.key == pygame.K_DOWN:
                # Шардың төменгі шегі экран шегінен аспауын тексереміз:
                # mainCoordY + 20 (қозғалыс қашықтығы) + 25 (радиус) <= 500 (экран биіктігі)
                if mainCoordY + 20 + 25 <= 500:
                    mainCoordY += 20  # Шарды 20 пиксель төмен жылжытамыз

            # Оң бағыт (RIGHT) пернесі басылса
            if event.key == pygame.K_RIGHT:
                # Шардың оң жағы экран шегінен аспауын тексереміз:
                # mainCoordX + 20 (қозғалыс қашықтығы) + 25 (радиус) <= 500 (экран ені)
                if mainCoordX + 20 + 25 <= 500:
                    mainCoordX += 20  # Шарды 20 пиксель оңға жылжытамыз

            # Сол бағыт (LEFT) пернесі басылса
            if event.key == pygame.K_LEFT:
                # Шардың сол жағы экран шегінен аспауын тексереміз:
                # mainCoordX - 20 (қозғалыс қашықтығы) - 25 (радиус) >= 0
                if mainCoordX - 20 - 25 >= 0:
                    mainCoordX -= 20  # Шарды 20 пиксель солға жылжытамыз
