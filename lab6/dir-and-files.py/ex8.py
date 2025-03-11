import os  # os модулін импорттау (файлдар мен жүйелік операциялар үшін)

# ✅ Файлды жою функциясы
def delete_file(file_path):
    """Берілген файлды жою әрекетін орындайды."""
    
    # 1️⃣ Файлдың бар-жоғын тексеру
    if os.path.exists(file_path):  # Егер файл бар болса
       
        # 2️⃣ Файлды өшіруге рұқсат бар-жоғын тексеру
        if os.access(file_path, os.W_OK):  # Егер файлды жазу/өшіру рұқсаты болса
            try:
                os.remove(file_path)  # Файлды өшіру
                print(f"✅ File '{file_path}' has been deleted.")  
            except Exception as e:  # Қате болса, өңдеу
                print("❌ Error while deleting the file:", e)
        else:
            print("❌ You do not have write access to delete this file.")
    
    else:
        print(f"❌ File '{file_path}' does not exist.")  # Егер файл жоқ болса, хабарлау

# ✅ Пайдаланушыдан өшірілетін файлдың жолын сұрау
path_delete = str(input("Enter the file path to delete: "))

# ✅ Функцияны шақыру (Файлды өшіру)
delete_file(path_delete)
