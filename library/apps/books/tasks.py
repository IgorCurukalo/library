from library.celery import app
import datetime
from django.db.models import Count
from apps.books.models import Book, CountBooks
import redis
from celery import shared_task


@app.task
def insert_count():
    #количествво книг
    count = len(Book.objects.annotate(Count("id")))
    print(f"Количество книг: {count}")
    #сохранение количества книг в базу
    new = CountBooks(count=count, date_add=datetime.datetime.now(), is_daleted=False)
    new.save()
    print(f"Данные внесены, количество: {count}")