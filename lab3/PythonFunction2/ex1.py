# 1. Функция: Бір фильмнің IMDB рейтингі 5.5-тен жоғары ма?
def is_highly_rated(movie):
    return movie["imdb"] > 5.5

# 2. Функция: IMDB рейтингі 5.5-тен жоғары фильмдердің тізімін шығару
def highly_rated_movies(movies):
    return [movie for movie in movies if movie["imdb"] > 5.5]

# 3. Функция: Берілген категориядағы фильмдерді шығару
def movies_by_category(movies, category):
    return [movie for movie in movies if movie["category"] == category]

# 4. Функция: Барлық фильмдердің орташа IMDB рейтингін есептеу
def average_imdb(movies):
    return sum(movie["imdb"] for movie in movies) / len(movies)

# 5. Функция: Белгілі бір категориядағы фильмдердің орташа IMDB рейтингін есептеу
def average_imdb_by_category(movies, category):
    category_movies = movies_by_category(movies, category)
    if not category_movies:  # Егер категорияда фильмдер болмаса
        return 0
    return sum(movie["imdb"] for movie in category_movies) / len(category_movies)

# Мысал қолдану:
print(is_highly_rated(movies[0]))  # True немесе False
print(highly_rated_movies(movies))  # Жоғары рейтингті фильмдер
print(movies_by_category(movies, "Romance"))  # "Romance" жанрындағы фильмдер
print(average_imdb(movies))  # Барлық фильмдердің орташа рейтингі
print(average_imdb_by_category(movies, "Thriller"))  # "Thriller" жанрындағы фильмдердің орташа рейтингі
