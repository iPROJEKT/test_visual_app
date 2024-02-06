# Тестовое задание

### Стек
* FastApi
* Alembic
* Uvicorn

### Как запустить?
1) Клонировать проект к себе на пк `git clone ...`
2) Поставить виртуальное окружение и накатить зависимости

* `python -m venv venv`
* `source venv\Scripts\activate `
* `pip install -r requirements.txt`

3) Создаем .env файл и записываем в него параметры для базы данных (.env.example)
4) Делаем миграции в базе, а так же принимаем их 
* `alembic revision --autogenerate -m "Name migr" `
* `alembic upgrade head `
5) Можно уже запускать `uvicorn run:app`
6) Преходим по ссылке `http://127.0.0.1:8000/docs/`

* Откроется интерактивная дока, по которой можно прозвонить url 