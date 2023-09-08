FROM python:3.10-slim

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y python3-pip && \
    pip install --upgrade pip

COPY ./requirements/prodcution.txt .

RUN pip install --no-cache-dir -r prodcution.txt

WORKDIR /src

COPY . .

EXPOSE 8000

CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000" ]
