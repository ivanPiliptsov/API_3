# Документация по учебному коду REST API на Python с использованием FastAPI

## Общая информация

### Базовый URL: `http://localhost:8000`
### Формат данных: JSON

## Эндпоинты API

1. Главная страница

* URL: `/`
* Метод: `GET`
* Описание: Возвращает приветственное сообщение
* Ответ: 

```json
{
    "message": "Добро пожаловать в мой API!"
}
```

2. Получить всех пользователей

* URL: `/users`
* Метод: `GET`
* Описание: Возвращает список всех пользователей
* Успешный ответ (200):

```json
{
  "users": [
    {
      "id": 1,
      "name": "Иван",
      "email": "ivan@example.com"
    },
    {
      "id": 2,
      "name": "Мария",
      "email": "maria@example.com"
    }
  ],
  "count": 2
}
```

3. Получить пользователя по ID

* URL: `/users/{user_id}`
* Метод: `GET`
* Параметры URL:
    * `user_id` (integer) - ID пользователя
* Успешный ответ(200)

```json
{
  "id": 1,
  "name": "Иван",
  "email": "ivan@example.com"
}
```
* Ошибка(404):

```json
{
  "error": "Пользователь не найден"
}
```

4. Создать нового пользователя

* URL: `/users`
* Метод: `POST`
* Тело запроса(JSON):

```json
{
  "name": "Новый пользователь",
  "email": "new@example.com"
}
```

* Обязательные поля: `name`, `email`
* Успешный ответ(201):

```json
{
  "id": 3,
  "name": "Новый пользователь",
  "email": "new@example.com"
}
```

5. Обновить пользователя

* URL: `/users/{user_id}`
* Метод: `PUT`
* Параметры URL:
  * `user_id`(integer) - ID пользователя
* Тело запроса(JSON):

```json
{
  "name": "Обновленное имя",
  "email": "updated@example.com"
}
```

* Поля для обновления(опционально): `name`, `email`
* Успешный ответ(200):

```json
{
  "id": 1,
  "name": "Обновленное имя",
  "email": "updated@example.com"
}
```

* Ошибка(404):

```json
{
  "error": "Пользователь не найден"
}
```

6. Удалить пользователя

* URL: `/users/{user_id}`
* Метод: `DELETE`
* Параметры URL:
  * `user_id`(integer) - ID пользователя
* Успешный ответ(200):

```json
{
  "message": "Пользователь удален"
}
```

* Ошибка(404):

```json
{
  "error": "Пользователь не найден"
}
```

## Примеры использования

### Получить всех пользователей

```bush
curl -X GET http://localhost:8000/users
```

### Создать нового пользователя

```bush
curl -X POST http://localhost:8000/users
  -H "Content-Type: application/json" \
  -d '{"name": "Алексей", "email": "alex@example.com"}'
```

### Обновить пользователя

```bush
curl -X PUT http://localhost:8000/users/1
  -H "Content-Type: application/json" \
  -d '{"name": "Иван Иванов", "email": "ivanov@example.com"}'
```

### Удалить пользователя

```bush
curl -X DELETE http://localhost:8000/users/1
```

### Коды состояния HTTP

* 200 - Успешный запрос
* 201 - Ресурс создан
* 404 - Ресурс не найден

### Примечания

* API использует in-memory базу данных, поэтому данные сбрасываются при перегрузке сервера
* ID пользователей генерируются автоматически
* Для запуска в продакшн режиме установите `debug=False`
