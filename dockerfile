#FROM python:3.9
#
#ENV PYTHONDONTWRITEBYTECODE 1
#ENV PYTHONUNBUFFERED 1
#
#WORKDIR /code
#
#COPY requirements.txt /code/
#
#RUN pip install -r requirements.txt
#
#COPY . /code/
#
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


#neva eva dockerfile
FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# RUN sed -i 's/deb.debian.org/mirror.yandex.ru/g' /etc/apt/sources.list
# RUN apt-get update && apt-get install -y librabbitmq-dev
WORKDIR /code

COPY requirements.txt /code/

RUN pip install -r requirements.txt

COPY . /code/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]