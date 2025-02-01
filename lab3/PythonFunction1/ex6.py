# Сөздерді кері тәртіпте қайтаратын функция
def reverse_sentence(sentence):
    words = sentence.split()  # Жолды бос орындар бойынша бөліп, сөздер тізімін алу
    reversed_sentence = ' '.join(reversed(words))  # Сөздерді кері тәртіпте қайтару
    return reversed_sentence

# Мысал қолдану:
print(reverse_sentence("We are ready"))  # Шығару: "ready are We"