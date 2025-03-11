import time
import math

# Пайдаланушыдан сан және кідіріс уақытын енгізу
x = int(input("Enter a number: "))
ms = int(input("Enter delay in milliseconds: "))

# Миллисекундты секундқа айналдыру (1000 мс = 1 секунд)
time.sleep(ms / 1000)

# Квадрат түбірді есептеу
sqrt_value = math.sqrt(x)

# Нәтижені шығару
print(f"Square root of {x} after {ms} milliseconds is {sqrt_value}")
