# Shape класын анықтау
class Shape:
    def area(self):
        return 0  # Пішіннің ауданы 0-ге тең

# Rectangle класын анықтау, ол Shape класынан мұраланады
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length  # Тіктөртбұрыштың ұзындығы
        self.width = width    # Тіктөртбұрыштың ені

    def area(self):
        return self.length * self.width  # Тіктөртбұрыштың ауданын есептеу

# Мысал қолдану
rectangle = Rectangle(4, 6)
print(rectangle.area())  # Шығару: 24