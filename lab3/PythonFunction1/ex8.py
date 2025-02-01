# Тізімде 007 тізбегін табу функциясы
def spy_game(nums):
    code = [0, 0, 7]  # Ізделетін тізбек
    index = 0  # Тізбектің индексі
    for num in nums:  # Тізім бойынша өту
        if num == code[index]:  # Егер сан тізбектегі санға сәйкес келсе
            index += 1  # Келесі санға өту
            if index == len(code):  # Егер тізбек табылса
                return True
    return False  # Егер тізбек табылмаса

# Мысал қолдану:
print(spy_game([1, 2, 4, 0, 0, 7, 5]))  # Шығару: True
print(spy_game([1, 0, 2, 4, 0, 5, 7]))  # Шығару: True
print(spy_game([1, 7, 2, 0, 4, 5, 0]))  # Шығару: False