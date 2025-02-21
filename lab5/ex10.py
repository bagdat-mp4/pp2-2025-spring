import re  # Регулярлы өрнектер (RegEx) кітапханасын жүктейміз

# CamelCase немесе PascalCase-ті snake_case-ке ауыстыру функциясы
def camel_to_snake(text):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', text).lower()  
    # (?<!^) -> Бірінші әріп болмаса ғана
    # (?=[A-Z]) -> Үлкен әріптің алдында болса, оның алдына "_" қоямыз

# Тест үшін camelCase мәтіні
camel_case_text = "convertCamelCaseToSnakeCase"

# Функцияны шақыру
snake_case_text = camel_to_snake(camel_case_text)

# Нәтижені шығару
print(snake_case_text)  # "convert_camel_case_to_snake_case"
