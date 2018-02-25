FROM python:3
ADD requirements.txt /app/requirements.txt
ADD ./celery_tasks/ /app/
WORKDIR /app/
RUN pip install -r requirements.txt
ENTRYPOINT celery -A celery_tasks worker --concurrency=20 --loglevel=info
