# команда для сборки docker:  docker build . -t app
# команда для запуска docker: docker run -p 8000:8000 -it app bash


FROM python:3.9-buster

#создается рабочая папка, чтобы не работать в корневой
WORKDIR /app

RUN pip install --upgrade pip
RUN pip install poetry==1.2.0

#отключаем создание виртуального окружения для poetry (оно создается автоматически для установки зависимостей из
#файла poetry.lock, а в docker нам этого не нужно
RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock ./

RUN poetry install

#сначала скачиваем зависимости, затем копируем файлы
#в docker копируется в корневую папку не сама папка web-app, а ее содержимое полностью
COPY web-app .

EXPOSE 8000

CMD uvicorn main:app --host=0.0.0.0 --port=8000
