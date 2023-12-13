FROM python:3.10

# Выбор папки, в которой будет вестись работа
WORKDIR /cart

# Установка зависимостей проекта

COPY ./requirements.txt /cart/
RUN pip install --no-cache-dir --upgrade -r /cart/requirements.txt

# Перенос проекта в образ
COPY ./app /cart/app

# Копирование файлов alembic
COPY ./alembic /cart/alembic
COPY ./alembic.ini /cart/alembic.ini


EXPOSE 80

CMD ["/bin/sh", "-c", \
    "uvicorn app.main:app --host 0.0.0.0 --port ${PORT}"]
