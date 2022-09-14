import requests
from library.celery import app

@app.task(bind=True, name='update_novelties_set')
def inform_new(*args, **kwargs):
    print('В магазине появилась новинка')