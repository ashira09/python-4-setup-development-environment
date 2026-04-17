# python-4-setup-development-environment
## Как запустить API
Для запуска API необходимо выполнить следующие действия:

1. Предварительно установить СУБД PostgreSQL.

2. Клонировать репозиторий командой:

    git clone https://github.com/ashira09/python-4-setup-development-environment.git

4. Заполнить файл ".env" актуальными данными.

3. Перейти в ветку task-6 командой:

    git checkout task-6

4. Создать окружение python командой:

    python -m venv venv

5. Актировать окружение командой:

    source ./venv/bin/activate

6. Установить зависимости:

    pip install -r requirements.txt

7. Перейти в папку "app" командой:

    cd app

8. Запустить сервер командой:

    uvicorn main:app --reload

9. Документация к API сервера доступна по адресу:

    http://127.0.0.1:8000/docs
