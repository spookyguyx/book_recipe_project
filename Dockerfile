FROM python:3.9

ENV PYTHONUNBUFFERED=1

RUN mkdir "app"

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

RUN python book_recipe/manage.py migrate
RUN python book_recipe/manage.py collectstatic --no-input

EXPOSE 8000

CMD ["python", "book_recipe/manage.py", "runserver", "0.0.0.0:8000"]

