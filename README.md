## Django-lat :parrot:

Проект на подобе информационного блога о странах.
Добавление информации по выбранной стране (регион, религия, население, фотографии);
Редактирование и удаление постов возможно только зарегестрированным пользователям;
Имеется капча, кеширование.


## Requirements
* Python 3.9
* Django 4.0
* PostgreSQL

## Installation
Use `pip`:
```
pip install -r requirements.txt
```

## Старт

#### Переименовать "api\api\.env copy" на "api\api\.env" и прописать свои настройки

    SECRET_KEY='django_key'
    DATABASES_USER='database user'
    DATABASES_PASSWORD='database password'
    DEBUG=True
    ALLOWED_HOSTS='127.0.0.1'
    INTERNAL_IPS=["127.0.0.1",]
    PORT:5432
 
 
## Запуск
```
python manage.py runserver
```
## Запуск docker
```
docker-compose up
```
