import sqlite3


# 1 Нормализовать базу данных относительно актеров.
# Выделить таблицу с актерами, а также таблицу многие-ко-многим
# `актер-фильм`. (Т.е. будут 3 таблицы: актеры, фильмы, актер-фильм).
# Сохранить новую бд как ‘task1.sqlite’.

netflix_connection = sqlite3.connect('netflix.sqlite')
netflix_cursor = netflix_connection.cursor()

task1_connection = sqlite3.connect('task1.sqlite')
task1_cursor = task1_connection.cursor()

# Таблица фильмов
task1_cursor.execute('''
    CREATE TABLE movies (
        show_id INTEGER PRIMARY KEY,
        type TEXT,
        title TEXT,
        director TEXT,
        cast TEXT,
        country TEXT,
        date_added TEXT,
        release_year INTEGER,
        rating TEXT,
        duration TEXT,
        listed_in TEXT,
        description TEXT
    )
''')

# Таблица актеров
task1_cursor.execute('''
    CREATE TABLE actors (
        actor_id INTEGER PRIMARY KEY,
        actor_name TEXT
    )
''')

# Таблица актер-фильм
task1_cursor.execute('''
    CREATE TABLE actor_movie (
        actor_id INTEGER,
        movie_id INTEGER,
        FOREIGN KEY (actor_id) REFERENCES actors (actor_id),
        FOREIGN KEY (movie_id) REFERENCES movies (movie_id),
        PRIMARY KEY (actor_id, movie_id)
    )
''')

# (Довольно громоздкий код, время работы +-полминуты)
actors_list = []  # Лист актёров, с помощью которого будем исключать их повторения в таблице актёров
netflix_cursor.execute('SELECT * FROM netflix_titles')
for netflix_title_data in netflix_cursor.fetchall():
    # Таблица кинокартин:
    movie_info = netflix_title_data[0:]
    task1_cursor.execute('INSERT INTO movies VALUES (?,?,?,?,?,?,?,?,?,?,?,?)', movie_info)
    # Таблица актёров
    cast_of_title = netflix_title_data[4]  # Сast в netflix_titles
    if cast_of_title:
        actors = [actor.strip() for actor in cast_of_title.split(',')]
        for actor in actors:
            if actors_list.count(actor) < 1:  # Параметр, исключающий повторение актёров в списке актёров
                actors_list.append(actor)
                task1_cursor.execute('INSERT INTO actors (actor_name) VALUES (?)', (actor,))
    # Актер-фильм
    actors_list_two = []
    show_id = netflix_title_data[0]
    for actor in actors:
        actor_info = task1_cursor.execute('SELECT actor_id FROM actors WHERE actor_name=?', (actor,))
        for _ in actor_info.fetchone():
            actor_id = _
            if actors_list_two.count(actor_id) < 1:
                actors_list_two.append(actor_id)
                task1_cursor.execute('INSERT INTO actor_movie VALUES (?, ?)', (actor_id, show_id))

task1_connection.commit()
netflix_connection.close()
task1_connection.close()


# 2 Исходя из этой таблицы, средствами SQL, вычислить
# наиболее часто работающую друг с другом пару актеров

connection = sqlite3.connect('task1.sqlite')
cursor = connection.cursor()

# Ищем часто работающую друг с другом пару актеров
query = '''
    SELECT a1.actor_name, a2.actor_name, COUNT(*) as movies_together
    FROM actor_movie am1
    JOIN actor_movie am2 ON am1.movie_id = am2.movie_id AND am1.actor_id < am2.actor_id
    JOIN actors a1 ON am1.actor_id = a1.actor_id
    JOIN actors a2 ON am2.actor_id = a2.actor_id
    GROUP BY a1.actor_name, a2.actor_name
    ORDER BY movies_together DESC
    LIMIT 1
'''

cursor.execute(query)
result = cursor.fetchone()

if result:
    first_actor, second_actor, movies = result
    print(f"Наиболее часто работают друг с другом: {first_actor} с {second_actor}. Парой участовали аж в {movies} фильмах.")

connection.close()