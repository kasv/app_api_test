# Система (демо)

## Запуск проекта
```$ docker-compose up -d --build```
```$ docker-compose run app_api_test python /opt/project/manage.py loaddata users applications```


## API методы
- [GET] `/api/` - получить список всех приложений
- [POST] `/api/` - создание нового приложения:
```json
{
  "name": "Some name for new app"
}
```

- [GET] `/api/<ID>` - получить данные приложения по ID
- [PUT] `/api/<ID>` - обновить имя приложения по ID:
```json
{
  "name": "New name for exist app"
}
```
- [DELETE] `/api/<ID>` - удалить приложение по ID

- [GET] `/api/test/<API_KEY>` - получить данные приложения по API_KEY


## Примеры запросов
Система требует basic-авторизацию, можно использовать следующие данные:
- логин: admin
- пароль: Aa123456

Для демонстрации запросов используется утилита `HTTPie` (`$ apt install httpie`)

### Получить список всех приложений
Запрос:
`$ http --auth admin:Aa123456 "http://127.0.0.1:5000/api/"`

Ответ (пример):
```json
[
    {
        "api_key": "1bc0e279-6b06-4f07-ba97-b0ae30b58613",
        "id": 5,
        "name": "app1"
    },
    {
        "api_key": "a2639be9-7ae6-4f40-8c2f-72945b94ab16",
        "id": 6,
        "name": "app2"
    }
]
```

### Создание нового приложения
Запрос:
`$ http --auth admin:Aa123456 "http://127.0.0.1:5000/api/" name=app3`

Ответ (пример):
```json
{
    "api_key": "24981fa2-40e0-4039-832c-c1fdbb601432",
    "id": 7,
    "name": "app3"
}
```

### Получить данные приложения по ID
Запрос:
`$ http --auth admin:Aa123456 "http://127.0.0.1:5000/api/6/"`

Ответ (пример):
```json
{
    "api_key": "a2639be9-7ae6-4f40-8c2f-72945b94ab16",
    "id": 6,
    "name": "app2"
}
```

### Обновить имя приложения по ID
Запрос:
`$ http --auth admin:Aa123456 PUT "http://127.0.0.1:5000/api/5/" name=app0`

Ответ (пример):
```json
{
    "api_key": "1bc0e279-6b06-4f07-ba97-b0ae30b58613",
    "id": 5,
    "name": "app0"
}
```

### Удалить приложение по ID
Запрос:
`$ http --auth admin:Aa123456 DELETE "http://127.0.0.1:5000/api/7/"`


### Получить данные приложения по API_KEY
Запрос:
`$ http --auth admin:Aa123456 "http://127.0.0.1:5000/api/test/a2639be9-7ae6-4f40-8c2f-72945b94ab16"`

Ответ (пример):
```json
{
    "api_key": "a2639be9-7ae6-4f40-8c2f-72945b94ab16",
    "id": 6,
    "name": "app2"
}
```