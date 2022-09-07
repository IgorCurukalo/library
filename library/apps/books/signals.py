from django.db.models.signals import pre_save, post_save, pre_delete, post_delete, m2m_changed
from django.core.signals import request_finished, request_started
from django.dispatch import receiver
from apps.books.models import Book, BooksInAuthor

count = 0

@receiver(pre_save, sender=Book)
def log_book_save(instance, **kwargs):
        print(f"pre_save - Пользователь пытается сохранить книгу: {instance.book_name}")

@receiver(post_save, sender=Book)
def log_book_save(instance, created, **kwargs):
    if created:
        global count
        count += 1
        print(f"Количество сохранений книг: {count}")
        print(f"post_save - Пользователь сохранил книгу:{instance.book_name}")

@receiver(pre_delete, sender=Book)
def save_delete_log(instance, **kwargs):
    print(f'pre_delete - Пользователь пытается удалить: {instance.book_name}')

@receiver(post_delete, sender=Book)
def save_delete_log(instance, **kwargs):
    print(f'post_delete - Пользователь удалил книгу: {instance.book_name}')

@receiver(request_started, sender=Book)
def my_callback(sender, **kwargs):
    print(f"Запрос {sender} стартовал!")

@receiver(request_finished, sender=Book)
def my_callback(sender, **kwargs):
    print(f"Запрос {sender} окончен!")

@receiver(m2m_changed, sender=BooksInAuthor)
def toppings_changed(sender, **kwargs):
    print(f"Изменения в модели {sender}")
