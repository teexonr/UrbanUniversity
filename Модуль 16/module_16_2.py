from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


@app.get('/user/{user_id}')
async def user_page(user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID')]) -> str:
    return f'Вы вошли как пользователь № {user_id}'


@app.get('/user/{username}/{age}')
async def user_info(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username')],
                    age: Annotated[int, Path(ge=18, le=120, description='Enter age')]) -> str:
    return f'Информация о пользователе. Имя: {username}, Возраст: {age}'
