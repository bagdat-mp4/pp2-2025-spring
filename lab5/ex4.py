import re  # Регулярлы өрнектер (RegEx) кітапханасын жүктейміз

txt = "Bagdat, arman Lady"  # Берілген мәтін

# RegEx өрнегі:
# [A-Z]   -> Бір үлкен әріптен басталуы керек.
# [a-z]+  -> Кемінде бір кіші әріптен тұруы керек.

x = re.findall(r"[A-Z][a-z]+", txt)  # RegEx өрнегі арқылы іздеу
print(x)  # Нәтижені шығару
