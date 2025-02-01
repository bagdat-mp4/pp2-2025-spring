# Тізімдегі бірегей элементтерді қайтару функциясы
def unique_elements(lst):
    unique = []  # Бірегей элементтер тізімі
    for item in lst:  # Тізім бойынша өту
        if item not in unique:  # Егер элемент бірегей болса
            unique.append(item)  # Бірегей элементтер тізіміне қосу
    return unique

# Мысал қолдану:
print(unique_elements([1, 2, 2, 3, 4, 4, 5]))  # Шығару: [1, 2, 3, 4, 5]