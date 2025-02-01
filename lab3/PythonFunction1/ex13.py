import random  # Кездейсоқ санды таңдау үшін модуль

# Санды табу ойыны
def guess_the_number():
    name = input("Hello! What is your name?\n")  # Пайдаланушының атын сұрау
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    number = random.randint(1, 20)  # 1-ден 20-ға дейін кездейсоқ сан таңдау
    guesses = 0  # Табуға жұмсалған әрекеттер саны

    while True:
        guess = int(input("Take a guess.\n"))  # Пайдаланушының болжамын енгізу
        guesses += 1  # Әрекеттер санын арттыру

        if guess < number:
            print("Your guess is too low.")  # Болжам төмен болса
        elif guess > number:
            print("Your guess is too high.")  # Болжам жоғары болса
        else:
            print(f"Good job, {name}! You guessed my number in {guesses} guesses!")  # Сан табылса
            break  # Ойынды аяқтау

# Мысал қолдану:
guess_the_number()