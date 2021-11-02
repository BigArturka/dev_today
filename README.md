http://35.234.85.34/api/
# Тестовое задание
# API новостной доски.
stack: Python 3.6, Django 3.0, DRF 3.12, Docker, docker-compose.

## Start
* Перед началом установки и работы приложения, предпологается, что у вас установлен  и настроен 
следующий софт: Docker, docker-compose, python3+, PostgreSQL.
1) Склонируйте проект
Клонировать: **git clone  https://github.com/BigArturka/dev_today**  
2) Перейдите в каталог склонированного проекта, и запустите запустите следующую команду:   
Сбилдить: **docker-compose up --build** (Вам нужно находится в том каталоге, 
в котором находится Dockerfile и docker-compose.yml)

3) Создайте базу данных в PostgreSQL
4) Создайте .env-файл с переменными окружения и заполните по примеру файла '.env.example':
5) Зайдите в контейнер докера и проведите миграции:   
**docker exec -it api bash**    (Открываем контейнер в оболочке bash)
**./manage.py migrate**   (команды manage.py доступны только из корневого каталога, в нашем случае /news_board)

6) Восстановите фикстуры (json-файлы содержащие перечень тестовых данных, для проверки проекта) командой:     
**./manage.py loaddata fixtures/auth.json fixtures/dump.json**

7) Запустите приложение:   
**./manage.py runserver**

В фикстурах содержаться тестовые данные:

1)accounts:

Administrator:
- username: admin
- password: admin

Other user:
- username: user
- password: user

2)Тестовые статьи и комментарии.

## API

Приложение имеет 4 сущности:
######User 
######Post 
######Comment
######Vote

В приложении имеются endpoint-ы для следующий действий:  
(Здесь приведены примеры с ссылками на развернутое приложение, 
для локального тестирование замените url-адрес http://35.234.85.34/ на http://localhost:8000/)

Для запросов методами GET и POST не требуется авторизация.   
Для выполнения запроса на создание/редактирование/удаление  или голосования, требуется авторизация по токену   
(В зописании запросов на авторизацию, указано как верно нужно получать и использовать токен)


1)Регистрация/авторизация (Реализована простая регистарция по юзернейму и паролю)    
[http://35.234.85.34/auth/register/](http://35.234.85.34/auth/register/) {POST-запрос}   
[http://35.234.85.34/auth/login/](http://35.234.85.34/auth/login/) {POST-запрос}   
[http://35.234.85.34/auth/logout/](http://35.234.85.34/auth/logout/) {POST-запрос}     
Пример данных для отправки:   
```
{  
    "username":"user",
    "password":"user"  
}
```
После отправки данных для авторизации, в ответ придёт Token    
```
{
    "token": "ae4da8745d909cd0edf7436b76d3b0def669be7b"
}
```
Который требуется доабвить в 
Header запроса для выполнения авторизованных запросов, следующим образом:       
```
headers: {'Authorization': 'Token 754966ebf7a82daf397ae5da3111407566e64022'}
```

2)Получение всех имеющихся постов:   
[http://35.234.85.34/api/posts/](http://35.234.85.34/api/posts/) {GET}    
```
[
    {
        "id": 5,
        "title": "Whu is Mask???",
        "link": "https://twitter.com/nypost/status/1455152556133470213?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Etweet%7Ctwtr%5Etrue",
        "author": "Anonim",
        "created_at": "2021-11-02T13:14:54.248358+06:00",
        "vote_count": 0
    },
]
```
3)Получение одного поста по ID:   
[http://35.234.85.34/api/posts/{id желаемого поста}/](http://35.234.85.34/api/posts/1/) {GET}    
```
{
    "id": 1,
    "title": "Apple сократила производство iPad, чтобы сэкономить чипы для iPhone",
    "link": "https://www.it-world.ru/it-news/market/179455.html",
    "author": "Анна Савельева",
    "created_at": "2021-11-02T16:35:34.281271+06:00",
    "comments": [
        {
            "id": 1,
            "author": "Тот самый",
            "link": "Reaaly???",
            "created_at": "2021-11-02T16:38:05.004370+06:00",
            "article": 1
        },
        {
            "id": 2,
            "author": "Тот самый",
            "link": "Это опять я",
            "created_at": "2021-11-02T16:38:14.794885+06:00",
            "article": 1
        }
    ]
}
```
4)Создание поста:    
[http://35.234.85.34/api/posts/](http://35.234.85.34/api/posts/) {POST}      
Пример данных для отправки:    
```
{
    "title": "Whu is Mask???",
    "link": "https://twitter.com/nypost/status/1455152556133470213?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Etweet%7Ctwtr%5Etrue",
    "author": "Anonim"
}
```
5)Редактирование поста по ID:    
[http://35.234.85.34/api/posts/{id желаемого поста}](http://35.234.85.34/api/posts/1/) {PUT}      
Пример данных для отправки:     
```
{
    "title": "Whu is Mask???",
    "link": "https://twitter.com/nypost/status/1455152556133470213?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Etweet%7Ctwtr%5Etrue",
    "author": "Anonim"
}
```
6)Удаление поста по ID:    
[http://35.234.85.34/api/posts/{id желаемого поста}](http://35.234.85.34/api/posts/1/) {DELETE}      

Аналогичным образом реализован CRUD для комментариев:     
[http://35.234.85.34/api/comments/](http://35.234.85.34/api/comments/) {GET}  (Просмотр всех комментариев)        
[http://35.234.85.34/api/comments/{id желаемого комментария}/](http://35.234.85.34/api/comments/1/) {GET} (Детальный просмотр комментария)        
[http://35.234.85.34/api/comments/](http://35.234.85.34/api/comments/) {POST} (Создание комментария)    
Пример данных для отправки    (требуется отправить ID поста, к которому необходимо добавить комментарий):    
```
{
    "author": "Smith",
    "link": "HEEEEELP",
    "article": 4
}
```
[http://35.234.85.34/api/comments/{id желаемого комментария}](http://35.234.85.34/api/comments/1/) {PUT} (Редактирование комментария по ID)       
[http://35.234.85.34/api/comments/{id желаемого комментария}](http://35.234.85.34/api/comments/1/) {DELETE} (Удаление комментария по ID)      


Голосование за пост:    
В приложении так же имеется точка доступа для отправки голоса за определенную публикацию или отмена голоса, если голос уже был отдан.       
[http://35.234.85.34/api/post/{id желаемого поста}/vote/](http://35.234.85.34/api/post/1/vote/) {POST}    


[![Run in Postman](https://run.pstmn.io/button.svg)](https://god.gw.postman.com/run-collection/13063440-3a106d9c-2ddc-4bb3-b4af-e83cba3c717c?action=collection%2Ffork&collection-url=entityId%3D13063440-3a106d9c-2ddc-4bb3-b4af-e83cba3c717c%26entityType%3Dcollection%26workspaceId%3Dfc614439-c88b-4220-a74b-a575c0b2b132)    

[Развёрнутое приложение на сервере](http://35.234.85.34/api/) - 
[http://35.234.85.34/api/](http://35.234.85.34/api/)    

## Зависимости
- Django==3.0 (Веб-фреймворк Python.)
- pytz==2020.4 (Переносит базу данных Olson tz в Python. Эта библиотека позволяет выполнять точные и кросс-платформенные вычисления часовых поясов с использованием Python.)
- asgiref==3.3.1 (Содержит различные эталонные реализации ASGI.)
- sqlparse==0.4.1 (Обеспечивает поддержку синтаксического анализа, разделения и форматирования операторов SQL.)
- djangorestframework==3.12.1 (REST-api фреймворк, использовался для написания представлений на основе представления DRF APIView и сериализации данных для отправке при обращении к энд-поинтам.)
- django-cors-headers==3.10.0 (Добавляет в ответы заголовки Cross-Origin Resource Sharing (CORS). Это позволяет в браузере запрашивать ваше приложение Django из других источников)

## Поддержка

Если у вас возникли сложности или вопросы по использованию приложения,  
 напишите на электронную почту arturkrmnlv10@gmail.com.
 
 
