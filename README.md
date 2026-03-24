# sibsutis-schedule-api

## Описание

"Данный проект является API для получения расписания из платформы sibsutis.ru"
"Для использовония в директории /parser необходимо создать файл private.py и добавить в него логин и пароль от платформы"
"Формат файла private.py: login = 'ваш логин' password = 'ваш пароль'"

## Быстрый старт PostgreSQL через Docker

1. Установите Docker и Compose:
   - `sudo apt update`
   - `sudo apt install -y docker.io docker-compose-v2`
2. Создайте `.env` на основе примера:
   - `cp .env.example .env`
3. Поднимите БД:
   - `docker compose up -d`
4. Проверьте, что контейнер работает:
   - `docker ps`
5. Подключитесь к БД:
   - `docker exec -it sibsutis_postgres psql -U postgres -d sibsutis_schedule`