def is_palindrome(text):
    return text == text[::-1]  # Жолды кері айналдырып, түпнұсқамен салыстырамыз

# Пайдаланушыдан мәтін енгізу
text = input("Enter a word: ")

# Нәтижені шығару
if is_palindrome(text):
    print("This is a palindrome!")
else:
    print("This is NOT a palindrome!")
