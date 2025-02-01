# Палиндромды тексеру функциясы
def is_palindrome(s):
    s = s.replace(" ", "").lower()  # Бос орындарды жою және барлық әріптерді кіші әріпке түрлендіру
    return s == s[::-1]  # Жолды керісінше тексеру

# Мысал қолдану:
print(is_palindrome("madam"))  # Шығару: True
print(is_palindrome("A man a plan a canal Panama"))  # Шығару: True
print(is_palindrome("hello"))  # Шығару: False