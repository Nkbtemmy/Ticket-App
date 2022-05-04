FROM python:3.10
RUN pip install pipenv
ENV PYTHONUMBUFFERED 1
WORKDIR /app
COPY Pipfile /app/Pipfile
RUN pipenv install --system --deploy
COPY . /app

CMD python manage.py runserver 0.0.0.0:8080