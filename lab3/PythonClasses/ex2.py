class Shape:
    def area(self):
        return 0  # Пішіннің ауданы 0-ге тең

class Square(Shape):
    def __init__(self, length):
        self.length = length  # Шаршының ұзындығын инициализациялау

    def area(self):
        return self.length * self.length  # Шаршының ауданын есептеу

# Мысал қолдану:
square = Square(5)
print(square.area())  # Шығару: 25