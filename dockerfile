FROM python:3.14-slim
WORKDIR /app
COPY . /app

RUN apt update -y && apt install ascii -y

RUN pip install -r requirements.txt

CMD ['PYTHON3','app.py']

