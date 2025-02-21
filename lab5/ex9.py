import re  # Регулярлы өрнектер (RegEx) кітапханасын жүктейміз

# Үлкен әріптерден басталатын жерлерге бос орын қою функциясы
def insert_spaces(text):
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', text)  
    # (?<!^) -> Жолдың басында емес
    # (?=[A-Z]) -> Үлкен әріптен басталатын бөліктерге сәйкес келеді

# Тест үшін мәтін
text = "InsertSpacesBetweenWords"

# Функцияны шақыру
result = insert_spaces(text)

# Нәтижені шығару
print(result)  # "Insert Spaces Between Words"
