FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /news_board

COPY requirements.txt /news_board/
RUN pip install -r requirements.txt
COPY . /news_board/
