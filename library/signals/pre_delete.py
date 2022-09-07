from django.db.models.signals import pre_delete
from django.dispatch import receiver

from apps.books.models import Book

@receiver(pre_delete, sender=Book)
def save_delete_log(sender, instance, **kwargs):

    print(f'User try to delete object with instance: {instance}')
