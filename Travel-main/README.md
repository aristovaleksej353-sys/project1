Проект базы данных путешествий. Позволяет хранить информацию о пользователях, странах и планах поездок.

База данных состоит из 3 таблиц:
 1. Таблица users (пользователи)
- id — уникальный идентификатор
- name — имя пользователя
- age — возраст
 2. Таблица countries (страны)
- id — уникальный идентификатор
- users_id — ссылка на пользователя (FOREIGN KEY)
- name — название страны
- best_season — лучший сезон для поездки
- has_sea — наличие моря 
3. Таблица travel_plans (планы поездок)
- id — уникальный идентификатор
- users_id — ссылка на пользователя
- country_id — ссылка на страну
- planned_year — планируемый год поездки
- days_count — количество дней
  -date_returned — дата возвращения
Таблицы:
<img width="2133" height="2560" alt="photo2" src="https://github.com/user-attachments/assets/19dff371-2824-4942-b826-b1e0c950e809" />
<img width="2097" height="2560" alt="photo3" src="https://github.com/user-attachments/assets/e3c7c716-2c1f-4082-98d3-c4bba7960fe5" />
<img width="2154" height="2560" alt="photo 4" src="https://github.com/user-attachments/assets/afc8347b-603e-4011-9001-581dd520c528" />

