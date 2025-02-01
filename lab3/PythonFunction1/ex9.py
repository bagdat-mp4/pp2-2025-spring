import math  # Математикалық функциялар үшін модуль

# Шардың көлемін есептеу функциясы
def sphere_volume(radius):
    return (4 / 3) * math.pi * (radius ** 3)  # Шар көлемінің формуласы

# Мысал қолдану:
print(sphere_volume(5))  # Шығару: 523.5987755982989