import os  # os модулін импорттау (файлдар мен папкалармен жұмыс істеу үшін)

def check_access(path):
    """ Бұл функция берілген жолдың (path) бар-жоғын тексеріп, 
    оған рұқсаттарды анықтайды (оқу, жазу, орындау). """
    
    # 1. Берілген жолдың бар-жоғын тексереміз
    if not os.path.exists(path):  
        print("path doesn't exist")  # Егер жол жоқ болса, хабарлама шығарамыз
        return  # Функцияны тоқтату
    else:
        print('path does exist')  # Егер жол бар болса, жалғастырамыз
    
        # 2. Файлды немесе папканы ОҚУҒА (READ) бола ма?
        if os.access(path, os.R_OK):
            print("readable")  # Егер оқуға рұқсат болса
        else:     
            print("don't readable")  # Егер оқуға рұқсат жоқ болса

        # 3. Файлды немесе папканы ЖАЗУҒА (WRITE) бола ма?
        if os.access(path, os.W_OK):
            print("writable")  # Егер жазуға рұқсат болса
        else:
            print("don't writable")  # Егер жазуға рұқсат жоқ болса

        # 4. Файлды немесе папканы ОРЫНДАУҒА (EXECUTE) бола ма?
        if os.access(path, os.X_OK):
            print("executable")  # Егер орындауға рұқсат болса
        else:
            print("don't executable")  # Егер орындауға рұқсат жоқ болса

# Негізгі код (тікелей орындалғанда ғана жұмыс істейді)
if __name__ == "__main__":  
    path_to_check = r"C:\Users\Администратор\Desktop\KBTUpp2\pp2-2025-spring"  # Тексерілетін жол
    
check_access(path_to_check)  # Функцияны шақыру
