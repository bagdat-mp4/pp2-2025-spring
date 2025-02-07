from itertools import permutations  # Пермутацияларды (ауыстырып қоюларды) есептеу үшін қажетті модуль

# Берілген жолдың барлық пермутацияларын шығаратын функция
def print_permutations(s):
    perms = [''.join(p) for p in permutations(s)]  # Жолдың барлық пермутацияларын тізімге алу
    for perm in perms:  # Әрбір пермутацияны бөлек шығару
        print(perm)

# Мысал қолдану:
print_permutations("abc")  # "abc" жолының барлық пермутацияларын шығару