#show әдісі нүктенің координаттарын көрсету үшін
#move әдісі осы координаттарды өзгерту үшін
#dist әдісі екі нүкте арасындағы қашықтықты есептеу үшін
import math

class Point:
    def __init__(self, x, y):
        self.x = x  # Нүктенің x координаты
        self.y = y  # Нүктенің y координаты

    def show(self):
        print(f"Координаттар: ({self.x}, {self.y})")  # Координаттарды көрсету

    def move(self, new_x, new_y):
        self.x = new_x  # x координатын өзгерту
        self.y = new_y  # y координатын өзгерту

    def dist(self, other_point):
        # Екі нүкте арасындағы қашықтықты есептеу
        return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)

# Мысал қолдану:
p1 = Point(2, 3)
p2 = Point(5, 7)
p1.show()
p2.show()
print(p1.dist(p2))  # Шығару: 5.0