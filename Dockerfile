FROM python

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . src
WORKDIR /src

EXPOSE 8000

ENTRYPOINT [ "python", "book_recipe/manage.py" ]
CMD [ "runserver", "0.0.0.0:8000" ]
