from django.db.models.signals import pre_save, post_save, pre_delete, post_delete, m2m_changed
from django.core.signals import request_finished, request_started
from django.dispatch import receiver
import logging
from apps.books.models import Book, BooksInAuthor, PublishingHouse, Author
from apps.books.tasks import inform_new

count = 0

#Book
@receiver(pre_save, sender=Book)
def log_book_save_pre(instance, **kwargs):
    logging.info(f"pre_save - Пользователь пытается сохранить книгу: {instance.book_name}")
    print(f"pre_save - Пользователь пытается сохранить книгу: {instance.book_name}")

@receiver(post_save, sender=Book)
def log_book_save_post(instance, created, **kwargs):
    if created:
        global count
        count += 1
        logging.info(f"Количество сохранений книг: {count}")
        logging.info(f"post_save - Пользователь сохранил книгу:{instance.book_name}")
        print(f"Количество сохранений книг: {count}")
        print(f"post_save - Пользователь сохранил книгу:{instance.book_name}")

@receiver(pre_delete, sender=Book)
def save_delete_log_pre(instance, **kwargs):
    logging.info(f'pre_delete - Пользователь пытается удалить книгу: {instance.book_name}')
    print(f'pre_delete - Пользователь пытается удалить книгу: {instance.book_name}')

@receiver(post_delete, sender=Book)
def save_delete_log_post(instance, **kwargs):
    logging.info(f'post_delete - Пользователь удалил книгу: {instance.book_name}')
    print(f'post_delete - Пользователь удалил книгу: {instance.book_name}')

@receiver(request_started, sender=Book)
def my_callback_start(sender, **kwargs):
    logging.info(f"Запрос {sender} стартовал!")
    print(f"Запрос {sender} стартовал!")

@receiver(request_finished, sender=Book)
def my_callback_finish(sender, **kwargs):
    logging.info(f"Запрос {sender} окончен!")
    print(f"Запрос {sender} окончен!")

@receiver(m2m_changed, sender=BooksInAuthor)
def toppings_changed(sender, **kwargs):
    logging.info(f"Изменения в модели {sender}")
    print(f"Изменения в модели {sender}")


#PublishingHouse
@receiver(pre_save, sender=PublishingHouse)
def log_book_save_pre(instance, **kwargs):
    logging.info(f"pre_save - Пользователь пытается сохранить издательство: {instance.publishing_house_name}")
    print(f"pre_save - Пользователь пытается сохранить издательство: {instance.publishing_house_name}")

@receiver(post_save, sender=PublishingHouse)
def log_book_save_post(instance, created, **kwargs):
    if created:
        logging.info(f"post_save - Пользователь сохранил издательство:{instance.publishing_house_name}")
        print(f"post_save - Пользователь сохранил издательство:{instance.publishing_house_name}")

@receiver(pre_delete, sender=PublishingHouse)
def save_delete_log_pre(instance, **kwargs):
    logging.info(f'pre_delete - Пользователь пытается удалить издательство: {instance.publishing_house_name}')
    print(f'pre_delete - Пользователь пытается удалить издательство: {instance.publishing_house_name}')

@receiver(post_delete, sender=PublishingHouse)
def save_delete_log_post(instance, **kwargs):
    logging.info(f'post_delete - Пользователь удалил издательство: {instance.publishing_house_name}')
    print(f'post_delete - Пользователь удалил издательство: {instance.publishing_house_name}')

@receiver(request_started, sender=PublishingHouse)
def my_callback_start(sender, **kwargs):
    logging.info(f"Запрос {sender} стартовал!")
    print(f"Запрос {sender} стартовал!")

@receiver(request_finished, sender=PublishingHouse)
def my_callback_finish(sender, **kwargs):
    logging.info(f"Запрос {sender} окончен!")
    print(f"Запрос {sender} окончен!")

#Author
@receiver(pre_save, sender=Author)
def log_book_save_pre(instance, **kwargs):
    logging.info(f"pre_save - Пользователь пытается сохранить автора: {instance.last_name}")
    print(f"pre_save - Пользователь пытается сохранить автора: {instance.last_name}")

@receiver(post_save, sender=Author)
def log_book_save_post(instance, created, **kwargs):
    if created:
        logging.info(f"post_save - Пользователь сохранил автора:{instance.last_name}")
        print(f"post_save - Пользователь сохранил автора:{instance.last_name}")

@receiver(pre_delete, sender=Author)
def save_delete_log_pre(instance, **kwargs):
    logging.info(f'pre_delete - Пользователь пытается удалить автора: {instance.last_name}')
    print(f'pre_delete - Пользователь пытается удалить автора: {instance.last_name}')

@receiver(post_delete, sender=Author)
def save_delete_log_post(instance, **kwargs):
    logging.info(f'post_delete - Пользователь удалил автора: {instance.last_name}')
    print(f'post_delete - Пользователь удалил автора: {instance.last_name}')

@receiver(request_started, sender=Author)
def my_callback_start(sender, **kwargs):
    logging.info(f"Запрос {sender} стартовал!")
    print(f"Запрос {sender} стартовал!")

@receiver(request_finished, sender=Author)
def my_callback_finish(sender, **kwargs):
    logging.info(f"Запрос {sender} окончен!")
    print(f"Запрос {sender} окончен!")