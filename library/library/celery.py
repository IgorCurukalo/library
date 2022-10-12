import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library.settings')

app = Celery('library')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send-every-1-minute': {
        'task': 'books.tasks.insert_count',
        'schedule': crontab(hour=14, minute=0),
    },
}


# @app.task(bind=True)
# def debug_task(self):
#     print(f'Request: {self.request!r}')