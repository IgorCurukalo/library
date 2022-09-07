from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.books.models import Book

count = 0

@receiver(post_save, sender=Book, )
def log_book_save(instance, created, **kwargs):
    if created:
        global count
        count += 1
        print(f"Count: {count}")
        print(f"Book {instance.book_name} is saved")

