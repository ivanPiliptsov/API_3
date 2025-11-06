from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from typing import List, Optional

app = FastAPI(title="User API", description="Простой REST API для управления пользователями")

# Модель данных с валидацией
class User(BaseModel):
    id: int
    name: str
    email: str

class UserCreate(BaseModel):
    name: str
    email: str

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None

# Простая база данных в памяти
users = [
    {"id": 1, "name": "Иван", "email": "ivan@example.com"},
    {"id": 2, "name": "Мария", "email": "maria@example.com"}
]

# Маршрут для главной страницы
@app.get("/")
async def home():
    return {"message": "Добро пожаловать в мой API!"}

# GET - получить всех пользователей
@app.get("/users", response_model=dict)
async def get_users():
    return {"users": users, "count": len(users)}

# GET - получить пользователя по ID
@app.get("/users/{user_id}", response_model=User)
async def get_user(user_id: int):
    user = next((u for u in users if u["id"] == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    return user

# POST - создать нового пользователя
@app.post("/users", response_model=User, status_code=201)
async def create_user(user_data: UserCreate):
    new_user = {
        "id": len(users) + 1,
        "name": user_data.name,
        "email": user_data.email
    }
    users.append(new_user)
    return new_user

# PUT - обновить пользователя
@app.put("/users/{user_id}", response_model=User)
async def update_user(user_id: int, user_data: UserUpdate):
    user = next((u for u in users if u["id"] == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    
    if user_data.name is not None:
        user['name'] = user_data.name
    if user_data.email is not None:
        user['email'] = user_data.email
    
    return user

# DELETE - удалить пользователя
@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    global users
    initial_count = len(users)
    users = [u for u in users if u["id"] != user_id]
    
    if len(users) == initial_count:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    
    return {"message": "Пользователь удален"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)