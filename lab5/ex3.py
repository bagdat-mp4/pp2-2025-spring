import re  # Регулярлы өрнектер (RegEx) кітапханасын жүктейміз

txt = "a_a_b_a"  # Берілген мәтін

# RegEx өрнегі:
# [a-z]+         -> Бір немесе одан көп кіші әріптерді табады.
# (?:_[a-z]+)+   -> Бір немесе одан көп "_әріп" үлгілерін іздейді. 
#                   ?: -> Бұл топтау (group) операциясы, бірақ есте сақтамай (non-capturing group) орындалады.

x = re.findall(r"[a-z]+(?:_[a-z]+)+", txt)  # RegEx өрнегі арқылы іздеу
print(x)  # Нәтижені шығару
