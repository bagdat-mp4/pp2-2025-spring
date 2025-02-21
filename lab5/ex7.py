import re  # Регулярлы өрнектер кітапханасы (RegEx)

# Snake_case -> CamelCase түріне ауыстыру функциясы
def snake_to_camel(snake_str):
    components = snake_str.split('_')  # "_" арқылы бөлінген сөздерді бөліп аламыз
    camel_case_str = components[0] + ''.join(word.capitalize() for word in components[1:])  
    # Бірінші сөз өзгермейді, қалған сөздердің бірінші әрпі үлкен болады
    return camel_case_str  # CamelCase түріндегі нәтижені қайтарамыз

# Тест үшін snake_case мәтіні
snake_case_string = "this_is_an_America"

# CamelCase-ке ауыстырамыз
camel_case_string = snake_to_camel(snake_case_string)

# Нәтижені шығару
print("Original:", snake_case_string)
print("Converted:", camel_case_string)
