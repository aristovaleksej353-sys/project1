import sqlite3


connection = sqlite3.connect('travel.db')
cursor = connection.cursor()

cursor.execute("PRAGMA foreign_keys = ON")

# Удаление старых таблиц
cursor.execute("DROP TABLE IF EXISTS travel_plans")
cursor.execute("DROP TABLE IF EXISTS countries")
cursor.execute("DROP TABLE IF EXISTS users")

# Создание таблиц
cursor.execute("""CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL  
)""")

cursor.execute("""CREATE TABLE countries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    users_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    best_season TEXT NOT NULL,
    has_sea INTEGER NOT NULL,
    FOREIGN KEY (users_id) REFERENCES users(id)
)""")

cursor.execute("""CREATE TABLE travel_plans (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    users_id INTEGER NOT NULL,
    country_id INTEGER NOT NULL,
    planned_year INTEGER NOT NULL,
    days_count INTEGER NOT NULL,
    date_returned TEXT,
    FOREIGN KEY (users_id) REFERENCES users(id),
    FOREIGN KEY (country_id) REFERENCES countries(id)
)""")

# Добавление пользователей
users_array = [
    ("Анна", 25), ("Петя", 17), ("Илья", 18), ("Надя", 19), ("Марина", 20),
    ("Олег", 30), ("Катя", 22), ("Дима", 28), ("Лена", 24), ("Саша", 26),
    ("Вероника", 19), ("Матвей", 20), ("Ева", 21), ("Давид", 22), ("София", 18),
    ("Мирон", 23), ("Агата", 20), ("Лев", 19), ("Злата", 22), ("Роберт", 21),
    ("Марта", 18), ("Глеб", 24), ("Оливия", 20), ("Тимофей", 19), ("Милана", 22),
    ("Арсений", 21), ("Варвара", 18), ("Серафим", 23), ("Эмилия", 20), ("Богдан", 19)
]

cursor.executemany("INSERT INTO users (name, age) VALUES (?, ?)", users_array)
print("30 пользователей добавлено")

# Добавление стран
countries_array = [
    (1, "Италия", "май-сентябрь", 1), (2, "Франция", "апрель-июнь", 1),
    (3, "Испания", "май-октябрь", 1), (4, "Греция", "июнь-сентябрь", 1),
    (5, "Турция", "май-октябрь", 1), (6, "Таиланд", "ноябрь-февраль", 1),
    (7, "Япония", "март-май", 1), (8, "Швейцария", "июнь-август", 0),
    (9, "Норвегия", "июнь-август", 1), (10, "Грузия", "май-сентябрь", 0),
    (11, "Египет", "ноябрь-февраль", 1), (12, "ОАЭ", "ноябрь-март", 1),
    (13, "Мальдивы", "ноябрь-апрель", 1), (14, "Португалия", "май-сентябрь", 1),
    (15, "Хорватия", "июнь-сентябрь", 1), (16, "Черногория", "июнь-сентябрь", 1),
    (17, "Кипр", "май-октябрь", 1), (18, "Мальта", "май-октябрь", 1),
    (19, "Исландия", "июнь-август", 1), (20, "Финляндия", "июнь-август", 1),
    (21, "Швеция", "июнь-август", 1), (22, "Дания", "июнь-август", 1),
    (23, "Нидерланды", "апрель-сентябрь", 1), (24, "Бельгия", "май-сентябрь", 1),
    (25, "Австрия", "май-сентябрь", 0), (26, "Чехия", "май-сентябрь", 0),
    (27, "Польша", "май-сентябрь", 0), (28, "Словакия", "май-сентябрь", 0),
    (29, "Словения", "май-сентябрь", 1), (30, "Болгария", "июнь-сентябрь", 1)
]

cursor.executemany("INSERT INTO countries (users_id, name, best_season, has_sea) VALUES (?, ?, ?, ?)", countries_array)
print("30 стран добавлено")

# Добавление планов
plans_array = [
    (1, 1, 2025, 7, "2025-06-15"), (2, 2, 2025, 10, "2025-04-20"),
    (3, 3, 2025, 6, "2025-08-10"), (4, 4, 2026, 7, None),
    (5, 5, 2025, 8, "2025-07-01"), (6, 6, 2026, 5, None),
    (7, 7, 2025, 9, "2025-03-15"), (8, 8, 2026, 6, None),
    (9, 9, 2025, 4, "2025-08-20"), (10, 10, 2026, 7, None),
    (11, 11, 2025, 10, "2025-02-10"), (12, 12, 2026, 5, None),
    (13, 13, 2025, 8, "2025-01-25"), (14, 14, 2026, 6, None),
    (15, 15, 2025, 7, "2025-09-05"), (16, 16, 2026, 5, None),
    (17, 17, 2025, 9, "2025-07-30"), (18, 18, 2026, 6, None),
    (19, 19, 2025, 5, "2025-08-12"), (20, 20, 2026, 7, None),
    (21, 21, 2025, 8, "2025-07-18"), (22, 22, 2026, 4, None),
    (23, 23, 2025, 6, "2025-06-25"), (24, 24, 2026, 5, None),
    (25, 25, 2025, 7, "2025-08-01"), (26, 26, 2026, 6, None),
    (27, 27, 2025, 5, "2025-09-10"), (28, 28, 2026, 4, None),
    (29, 29, 2025, 8, "2025-07-22"), (30, 30, 2026, 6, None)
]

cursor.executemany("INSERT INTO travel_plans (users_id, country_id, planned_year, days_count, date_returned) VALUES (?, ?, ?, ?, ?)", plans_array)
print("30 планов добавлено")

connection.commit()



cursor.execute("SELECT COUNT(*) FROM users")


cursor.execute("SELECT COUNT(*) FROM countries")

cursor.execute("SELECT COUNT(*) FROM travel_plans")



connection.close()
