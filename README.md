# _FOODGRAM - продуктовый помощник_ 

_Адрес сервиса_ - 130.193.43.250

_Доступ в админ панель:_
- логин: admin@gmail.com
- пароль: admin
____

![foodgram_workflow](https://github.com/Gorstka/foodgram-project-react/actions/workflows/foodgram_workflow.yml/badge.svg)

### _Описание проекта_

Это web-сервис с API для него, который позволяет пользователям публиковать рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.

### _Заполните файл переменных окружения(.env)_

- DB_NAME=<имя базы данных> 
- POSTGRES_USER=<имя пользователя БД> 
- POSTGRES_PASSWORD=<пароль> 
- DB_HOST=<хост БД> 
- DB_PORT=<порт БД> 

### _Инструкция по запуску_
```
docker-compose up (построение контейнеров и запуск)
docker-compose exec web python manage.py migrate (выполнить миграции)
docker-compose exec web python manage.py createsuperuser (создать суперпользователя)
docker-compose exec web python manage.py collectstatic --no-input (собрать статические файлы)
```

### _Технологии_

- Python 
- Django
- Django Rest Framework
- Docker
- Gunicorn
- Nginx
- PostgreSQL

### _Автор_

Горстка Сергей, github.com/Gorstka, gorstkasergei@gmail.com