#Класстың getString және printString әдістері:
class StringManipulator:
    def __init__(self):
        self.s = ""  # Бұл жерде біз бос жолды сақтайтын атрибутты инициализациялаймыз.

    def getString(self):
        self.s = input("Жолды енгізіңіз: ")  # Бұл әдіс пайдаланушыдан жолды енгізуді сұрайды және оны self.s атрибутына сақтайды.

    def printString(self):
        print(self.s.upper())  # Бұл әдіс сақталған жолды үлкен әріптерге түрлендіріп, экранға шығарады.

# Мысал қолдану:
sm = StringManipulator()  # StringManipulator класының объектісін жасаймыз.
sm.getString()  # Пайдаланушыдан жолды енгізуді сұраймыз.
sm.printString()  # Енгізілген жолды үлкен әріптермен шығарамыз.
