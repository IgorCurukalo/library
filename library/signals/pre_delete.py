from django.db.models.signals import pre_delete
from django.dispatch import receiver

@receiver(pre_delete)
def save_log():
    pass
