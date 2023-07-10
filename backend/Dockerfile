FROM python:3.11-alpine

WORKDIR /src

RUN pip install --upgrade pip

COPY . /src

RUN pip install -r requirements.txt

ENV FLASK_APP=app

CMD ["python","backend/index.py"]