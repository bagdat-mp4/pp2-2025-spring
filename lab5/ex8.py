import re  # Регулярлы өрнектер (RegEx) кітапханасын жүктейміз

# Үлкен әріптер арқылы бөлінген сөздерді табу функциясы
def split_at_uppercase(text):
    words = re.split(r'([A-Z][a-z]*)', text)  # Үлкен әріптен басталып, кіші әріптермен жалғасатын үлгіні табамыз
    words = [word for word in words if word]  # Бос элементтерді алып тастаймыз
    return words  # Табылған сөздердің тізімін қайтарамыз

# Тест үшін мәтін
sample_text = "HelloWorldPythonProgram"

# Функцияны шақыру
result = split_at_uppercase(sample_text)

# Нәтижені шығару
print("Original String:", sample_text)
print("Split Result:", result)
