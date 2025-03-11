import string  # 'string' модулін импорттау (латын алфавитін алу үшін)
def generate_files():
    for letter in string.ascii_uppercase:  # A-дан Z-ға дейінгі әріптер арқылы цикл
        filename = letter + ".txt"  # Файл атауын жасау (мысалы, "A.txt", "B.txt")
        
        with open(filename, 'w') as file:  # Файлды жазу ('w' - overwrite режимі) режимінде ашу
            file.write("hello world")  # Файлға "hello world" жазу
if __name__ == "__main__":  # Егер код тікелей орындалса
    generate_files()  # `generate_files()` функциясын шақыру
